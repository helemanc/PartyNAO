 #Import moves
from moves import *

# Import algorithm and classes (Node, Problem)
import search_algorithms_partyNAO
from search_algorithms_partyNAO import Problem

# Import utilities
from itertools import permutations
import time 

# Robot connection settings
ip = "127.0.0.1"
port = 65211 # virtual robot port

#--------------------------------------------------------------#
# Dictionary {key=module : value=move_name}
position_list_dictionary = {crouch: "OB_crouch", diagonal_left : "diagonal left", diagonalright:"diagonal right",
                            doublemovement:"double movement", move_forward : "move forward", 
                            movebackward:"move backward", right_arm:"right arm", 
                            rotation_foot_left_leg:"rotation foot left leg", rotation_foot_right_leg:"rotation foot right leg", 
                            rotationhandgun:"rotation handgun", sit:"OB_sit", sit_relax:"OB_sit relax", stand_init:"OB_stand init", 
                            stand_zero:"OB_stand zero", stand:"OB_stand", union_arms:"union arms", hello:"OB_hello", wipe_forehead: "OB_wipe forehead",  
                            new_speedy: "speedy", new_superman: "superman",
                            sprinkler : "sprinkler", sing_with_me : "sing with me", birthday_dance: "birthday dance", workout : "workout"}

# List of moves divided by "intensity"
list_slow_moves = ["OB_crouch", "double movement", "rotation foot left leg", "rotation foot right leg", "OB_sit", "OB_sit relax", "OB_wipe forehead"]
list_normal_moves = ["diagonal left", "diagonal right", "move forward", "move backward", "OB_hello", "sprinkler"]
list_fast_moves = ["right arm", "rotation handgun", "OB_stand init", "OB_stand zero", "OB_stand", "union arms", "superman", "sing with me", "birthday dance", "workout"]

#--------------------------------------------------------------#
# Prepare a list with all the position names in order to compute all the permutations
position_names = list(position_list_dictionary.values())

# Compute the duration in seconds between two consecutive moves
def calcTimeMove(position):
    start_time = time.time()
    position.main(ip,port)
    time_move = time.time() - start_time
    print("--- %s seconds ---" % (time_move))
    return time_move

#Create a dictionary {key=(start_move, end_move): value=duration}
def generateDictTimeMove(p_list):
    d = {}
    d1 = {v:k for k, v in position_list_dictionary.items()}
    for move in permutations(p_list,2):
        if(move[0]!= "sit" or move[0] != "sit_relax"):
            stand_init.main(ip, port)
        d1[move[0]].main(ip,port)
        timer = calcTimeMove(d1[move[1]])
        d[move] = timer
    return d

# The commented part below isn't executed every time, but only once at the beginning to
# generate a dictionary with the correspondences between pairs of moves
# and the relative time of execution and to write them into a file
'''
D=generateDictTimeMove(position_names)
print(D)
file1= open("permutationsFile.txt", "a")
stringa=""
for i in D.items():
    file1.write(str(i)+"\n")

'''
#--------------------------------------------------------------#
#partyNAO is the main class of the program and it inherits from the Problem class of @aima-python
class partyNAO(Problem):
    """How to represent the state?
       In our problem the state is represented by a string containing the name of the current 
       position. The goal is represented by one of the 6 mandatory intermediate position for 7 sub-problems. 
       The initial state is always represented by 'StandInit', the final goal is always represented by 'Crouch'
       The goal of one of the sub-problems becomes the initial state of the next sub-problem """

    '''
        Init parameters' explanation

            initial : initial state 
            goal : goal state
            dict_moves_time : dictionary with pair of moves and relative duration 
            min_max : tuple with the minimum and the maximum time to reach the current goal from each possible state 
            analized_song : list with values which represent the average intensity per second of the song 
            list_fast : list contanining fast moves 
            list_normal : list containing moves with normal speed 
            list_slow : list containing slow moves 
            increasing_time : amount of time passed from the start of the total sequence 

    '''
    def __init__(self, initial, goal, dict_moves_time, min_max, analized_song, list_fast, list_normal, list_slow,
                 increasing_time):
        """Constructor"""
        self.dict_moves_time = dict_moves_time
        self.min_max = min_max
        self.tot_time = 0
        self.analized_song = analized_song
        self.list_slow = list_slow
        self.list_normal = list_normal
        self.list_fast = list_fast
        self.increasing_time = increasing_time
        Problem.__init__(self, initial, goal)
        
    def actions(self, state):
        """The actions executable in this state."""
        result = []
        for key in self.dict_moves_time.keys():
            if key[0] = =state:
                result.append(key)
        return result
        
    def result(self, state, action):
        """The state that results from executing this action in this state."""
        self.time = self.dict_moves_time[action]
        return action[1]

    '''
        Explanation of value method

            The method value is used by the *simulated annealing algorithm* to evaluate how good is the chosen state. 
            We use a combination of two different criteria: 
                1. The distance in time between the chosen state and the goal state (we want to minimize this)
                2. How fit is the move in the current second of the song (the evaluation is done taking into account the type of the move (fast, normal, slow) 
                    and the intensity of the song in that second)
    '''

    def value(self, state):
        if self.goal_test(state):
            return 1 
        round_time = int(round(self.tot_time+self.increasing_time))
        if (round_time > 179): #sequences with time greater than 179 are not interesting 
            return "Fail"
        intensity = self.analized_song[round_time]
    
        if (state.state in list_fast_moves and intensity > 50) or (state.state in list_normal_moves and (intensity > 40 and intensity < 50)) or (state.state in list_slow_moves and intensity < 40):
            if (state.state in list_fast_moves and intensity > 50):
                val_move = 1.0
            else:
                val_move = 0.9
          
        elif (state.state in list_fast_moves and (intensity >40 and intensity < 50)) or (state.state in list_normal_moves and (intensity <40 or intensity > 50) or (state.state in list_slow_moves and (intensity > 40 and intensity<50))):
            val_move = 0.3
        elif (state.state in list_fast_moves and intensity < 40) or (state.state in list_slow_moves and intensity >50):
            val_move = 0.1
        else: 
            print("##########Error##################")
        max_time_relative = self.min_max[1] - self.min_max[0]
        val_time = 1-(((self.dict_moves_time[(state.state, self.goal)]-self.min_max[0])/max_time_relative))
        val = (val_move + val_time)/2
        #val = 0 -> bad state 
        #val = 1 -> good state
        return val
       

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor."""
        if isinstance(self.goal, list):
            if (state.state in self.goal):
                return True 
        else:
            return state.state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c (time) to get up to state1."""
        return self.dict_moves_time[action]

    """
        The following method is used to update the total time lof the current path 
    """
    def total_cost_time(self, c):
        self.tot_time += c
#--------------------------------------------------------------#