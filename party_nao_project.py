# -*- coding: UTF-8 -*-
from naoqi import ALProxy 

# Import moves
from moves import *

# Import algorithm and classes (Node, Problem)
import search_algorithms_partyNAO
from search_algorithms_partyNAO import Problem

# Import utilities
import time
import argparse
import operator
import math
import random
import glob, os 
import pydub 
import music_detection as md
from threading import Thread

# Import problem fot partyNAO
import party_nao_problem_def as pnp

# Robot connection settings
ip = "127.0.0.1"
port = 65211  #virtual robot port

#--------------------------------------------------------------#
# The following function and threads allow us to synchronize the execution of the choreography and the song


def execution_best_sequence(flat_list):
    d1 = {v: k for k, v in pnp.position_list_dictionary.items()}
    for el in flat_list:
        position = d1[el]
        position.main(ip, port)


class ThreadSong(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        md.play_song(song)


class ThreadDance(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        time.sleep(3.0)
        execution_best_sequence(flat_list)

#----------------------------MAIN------------------------------#

# Read from the file the pairs and fill a dictionary used during the execution


f = open("permutationsFile.txt", 'r')
dict_moves_time = {}
for line in f: 
    name_move = line[2:].split('),')
    ns = name_move[0].split(',')
    move1 = ns[0][1:-1]
    move2 = ns[1][2:-1]
    move = (move1, move2)
    timer = float(name_move[1][1:-3])
    dict_moves_time[move] = timer

#--------------------------------------------------------------#
# Select a random song and analyze the amplitude
song = md.random_song() 
analyzed_song = md.analyze_music(song)
#--------------------------------------------------------------#
print("Using simulated annealing algorithm to find the best sequence for the selected song...")
#--------------------------------------------------------------#
# For each move we extract the minimum and maximum time between the move and every possible goal
# Then we construct the dictionary {key=goal_move, value=(min_time, max_time)}
list_goals_with_crouch = ["OB_sit relax", "OB_sit", "OB_stand zero", "OB_stand", "OB_hello", "OB_wipe forehead",
                          "OB_crouch"]
d_min_max = {}
for el in list_goals_with_crouch:
    l = []
    for key in dict_moves_time:
        if key[1] == el:
            l.append(dict_moves_time[key])
    min_time_for_goal = min(l)
    max_time_for_goal = max(l)
    d_min_max[el] = (min_time_for_goal, max_time_for_goal)


times_indexes = []

while times_indexes == []:  # This while terminates when a sequence which respects all the constraints of the problem
                            # is found.
    used_intermediate_moves = []
    dict_totale = {}
    
    for i in range(20):  # This for allow us to generate 100 possible solutions in order to choose the best one
        used_intermediate_moves = []

        while len(used_intermediate_moves) <= 4:  # This while condition allows us to respect the constraint of
                                                  # the problem(" The algorithm A
                                                  # must use at least 5 different intermediate positions")
            used_intermediate_moves = []
            list_goals = ["OB_sit relax", "OB_sit", "OB_stand zero", "OB_stand", "OB_hello", "OB_wipe forehead"]
            total_solution = []
            next_initial_state = "OB_stand init"
            total_time = 0
            already_crouched = False

            while list_goals != []: # This while allow us to find a solution for each sub-problem
                dict_path_1 = {}
                dict_path_2 = {}

                for el in list_goals:  # For each goal we find a solution
                    problem = pnp.partyNAO(next_initial_state, el, dict_moves_time, d_min_max[el],
                                           analyzed_song, pnp.list_fast_moves, pnp.list_normal_moves, pnp.list_slow_moves,
                                           total_time)
                    sol = search_algorithms_partyNAO.simulated_annealing_full(problem)

                    for el in sol[1:-1]: 
                        if el not in used_intermediate_moves:
                            used_intermediate_moves.append(el)
                    dict_path_1[el] = sol
                    dict_path_2[el] = problem.tot_time
                
                dict_path_2_reversed = {v: k for k, v in dict_path_2.items()}
                # Add the computed sub_solution to the total_sequence
                total_solution.append(dict_path_1[dict_path_2_reversed[min(dict_path_2.values())]][:-1])
                next_initial_state = dict_path_1[dict_path_2_reversed[min(dict_path_2.values())]][-1]
                list_goals.remove(next_initial_state)
                total_time += min(dict_path_2.values())

                if list_goals == [] and already_crouched == False:
                    list_goals.append("OB_crouch")
                    already_crouched = True

        # We add the state "Crouch" to be sure that it's the las move (in order to respect the constraint of the problem)
        total_solution[-1].append("OB_crouch")
        tot_seq_len = 0

        for el in total_solution:  # Computing the length of the sequence
            tot_seq_len += len(el)
        dict_totale[(total_time, tot_seq_len)] = total_solution

    l_tempi = []
    l_seq = []
    times_indexes = []
    # We use the following cycle in order to scan the whole solutions dictionary and we select the best ones
    # (considering the constraint on time and number of moves, in order to create an artistic/complex choreography)
    for i in dict_totale.keys():
        l_tempi.append(i[0])
        if i[0] > 173 and i[0] < 175 and i[1] > 40 and i[1] < 46:
            times_indexes.append(i)  # salviamo la tupla con il tempo che ci piace
        l_seq.append(i[1])


#--------------------------------------------------------------#

# Extracting the best solution
print("Extracting the best solution...")
max_index = 0

for i in range(len(times_indexes)):
    if times_indexes[i][1] > max_index:
        max_index = i
print("TOTAL TIME: ", times_indexes[max_index])
best_sequence = dict_totale[times_indexes[max_index]]

flat_list = []
for sublist in best_sequence:
    for item in sublist:
        flat_list.append(item)

print("BEST SEQUENCE: ", flat_list, "NUMBER OF MOVES: ", len(flat_list))

#--------------------------------------------------------------#

# Execution of the best move and start the song.

t1 = ThreadSong()
t2= ThreadDance()
t2.start()
t1.start()

#--------------------------------------------------------------#
