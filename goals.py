from moves import *
import search_algorithms_partyNAO
from search_algorithms_partyNAO import Problem

import time
import argparse
from itertools import permutations

f = open("filePermutazioniNoSay.txt", 'r')
dict_moves_time = {}
for line in f: 
    name_move = line[2:].split('),')
    ns = name_move[0].split(',')
    move1 = ns[0][1:-1]
    move2 = ns[1][2:-1]
    move = (move1, move2)
    time = float(name_move[1][1:-3])
    dict_moves_time[move] = time

list_goals_con_crouch = ["OB_sit relax", "OB_sit", "OB_stand zero", "OB_stand", "OB_hello", "OB_wipe forehead",
                         "OB_crouch"]
d_min_max = {}
for el in list_goals_con_crouch:
    print("Elemento goal : " + el)
    l = []
    for key in dict_moves_time:
        # print("Chiave: " + key[0] + key [1])
        if key[1] == el:
            l.append(dict_moves_time[key])
    # print(l)
    min_time_for_goal = min(l)
    max_time_for_goal = max(l)
    d_min_max[el] = (min_time_for_goal, max_time_for_goal)
    # print("dizionario" , d_min_max)

print(d_min_max)
