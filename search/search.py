# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem): 
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    explored = [] #list of all explored nodes
    actions = recursive_dfs(problem.getStartState(),problem,explored,1) #The actions to take for reaching the goal state
    #print "Number of  actions: ",len(actions)
    return actions
    
def recursive_dfs(state,problem,explored,reverse):
	"""
	state has the start state. Problem has information regarding the problem. explored has explored nodes. reverse is intialized to 0 if it's 1 add the nodes in reverse order.
	"""
	
	if (problem.isGoalState(state)):  #if it's goal state
		return []
		
	explored.append(state) #i.e update the explored list.
	
	if (reverse):  #Add the sucessors in the reverse order
		reverse_insertion = list(problem.getSuccessors(state))
		reverse_insertion.reverse()
		for successor,direction,cost in reverse_insertion: #All successors
			if successor not in explored:
				action= recursive_dfs(successor,problem,explored,reverse)
			
				if (action != False):
					return [direction] + action
				
		return False
		
	else:
		for successor,direction,cost in problem.getSuccessors(state): #All successors
			if successor not in explored:
				action= recursive_dfs(successor,problem,explored,reverse)
			
				if (action != False):
					return [direction] + action
				
		return False
	

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    frontier = util.Queue()                			# This is for the Frontier Queue
    frontier.push(problem.getStartState()) 			# Adding initial state to frontier Queue
    explored = []                          			# Initialising empty explored list
    parent = {}                            			# Dictionary mapping successor to it's parent state and action

    while True:
        
        if frontier.isEmpty():
            return None                                         # No Solution found

        state = frontier.pop() 					# Get an element from frontier

        if problem.isGoalState(state): 				# If goal tests passes return list of actions
            sequence_of_states = [] 				# Initialise list of actions of list of actions
            while state != problem.getStartState():
                a, b = parent[state] 				# a = parent state, b = action leading to state
                sequence_of_states.insert(0,a)
                state = b
            return sequence_of_states 				# Returning sequence of actions

        explored.append(state) 					# Goal test failed,adding the node to the explored states

        """children"""
        for successor, action, stepCost in  problem.getSuccessors(state):
            if successor not in explored + frontier.list: 	# Add to frontier if not in explored or frontier
                frontier.push(successor)
                parent[successor] = (action, state)


def uniformCostSearch(problem):
	"""Search the node of least total cost first."""

	return aStarSearch(problem, nullHeuristic)  #since UCS is same as A* Search with nullHeuristic.   

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
	"""Search the node that has the lowest combined cost and heuristic first."""

	start_state = problem.getStartState()  #start state of problem
	frontier = util.PriorityQueue() #frontier queue
	G_value = {start_state:0}  #g(n) for any node n.
	explored = [] #all explored nodes
	parent = {} #for getting the solution back.
	frontier.push (start_state, 0 + heuristic(start_state, problem)) #update frontier. Since G_value at start will be zero.

	while True:
		
		if frontier.isEmpty(): #couldn't find any solution
			return None

		temp_state = frontier.pop() #get a state.

		if (problem.isGoalState(temp_state)): # Got the solution and returns it
			
			result = [] #return the result

			while (temp_state != start_state):
				parent_state, direction = parent[temp_state]
				result.insert(0,direction) #keep adding it to start for correct directions
				temp_state = parent_state
			return result

		explored.append(temp_state) #update explored list

		frontier_list = []  #Get all the nodes in frontier in a list as a iterable.

		for index, (p, c, i) in enumerate(frontier.heap):  #used from util.py file
			frontier_list.append(i)

		for successor, direction, cost in problem.getSuccessors(temp_state): 					
			
			if successor not in explored and successor not in frontier_list:  #inserting
				G_value[successor] = G_value[temp_state] + cost
				frontier.push(successor, G_value[successor] + heuristic(successor, problem))
				parent[successor] = (temp_state, direction)

			if successor in frontier_list and G_value[successor] > G_value[temp_state] + cost:  #updating if already present and less cost.
				G_value[successor] = G_value[temp_state] + cost
				frontier.update(successor, G_value[successor] + heuristic(successor, problem))
				parent[successor] = (temp_state, direction) 

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
