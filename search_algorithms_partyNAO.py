#Import utilities 
import math 
import sys
import random 

# ______________________________________________________________________________



def is_in(elt, seq):
        """Similar to (elt in seq), but compares with 'is', not '=='."""
        return any(x is elt for x in seq)

class Problem(object):
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

 

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


# ______________________________________________________________________________


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action,
                         problem.path_cost(self.path_cost, self.state,
                                           action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

# ______________________________________________________________________________
# Simulated annealing implementation inspired on @aima-python 
 
def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)

'''
    Choose of parameters
    We have chosen these parameters in order to obtain a probability of selecting 
    a worsening state similar to zero after 15 iterations.
'''
def exp_schedule(k=75, lam=0.5, limit=200): 
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)

def simulated_annealing_full(problem, schedule=exp_schedule()): 
    """ This version returns all the states encountered in reaching 
    the goal state."""
    states = []
    forbidden_states=["OB_crouch", "OB_sit relax", "OB_sit", "OB_stand init", "OB_stand zero", "OB_stand", "OB_hello", "OB_wipe forehead"]
    forbidden_states_no_goal=[el for el in forbidden_states if el != problem.goal]
    current = Node(problem.initial)
    t=1
    previuous_choice=""
    previous_val=problem.value(current)
    while problem.goal_test(current) != True: 
        if(current.state!=previuous_choice): #we don't want that the same state is repeated consecutively
            states.append(current.state)
            problem.total_cost_time(current.path_cost)
        T = schedule(t)
        if T == 0:  #limit reached 
            return states
        neighbors = current.expand(problem)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        
        '''
             Explanation of conditions of the 'if':
             1. next_choice.state in forbidden_states_no_goal -> it shouldn't be possible that the next state belongs to the list of goals
                (different from the goal selected for this sub-problem)
             2. next_choice.state == current.state -> it shouln't be possible that he same state is repeated consecutively
             3. len(states)==1 and (next_choice.state in forbidden_states) -> it shouldn't be possible that in the sequence appear two consecutive mandatory position 
             4. ((next_choice.state, problem.goal) not in problem.dict_moves_time.keys()) and (next_choice.state != problem.goal) -> it shouldn't be possible to select a move that is not linked to the goal 

             --The dictionary contains only the moves in which the robot doesn't fall down.
        '''
        if (next_choice.state in forbidden_states_no_goal) or (next_choice.state == current.state) or (len(states)==1 and (next_choice.state in forbidden_states)) or (((next_choice.state, problem.goal) not in problem.dict_moves_time.keys()) and (next_choice.state != problem.goal)):
             while  (next_choice.state in forbidden_states_no_goal) or (next_choice.state == current.state) or (len(states)==1 and (next_choice.state in forbidden_states)) or (((next_choice.state, problem.goal) not in problem.dict_moves_time.keys()) and (next_choice.state != problem.goal)):
                next_choice = random.choice(neighbors)
        next_val=problem.value(next_choice)
        if(next_val == "Fail"):
            next_choice=Node(problem.goal)
            delta_e=1
        else:
            delta_e = next_val - previous_val

        previuous_choice=current.state
        if delta_e > 0 or probability(math.exp(delta_e / T)):
            previous_val=problem.value(current)
            current = next_choice
        t+=1
        
    states.append(current.state)
    problem.total_cost_time(current.path_cost)
    return states