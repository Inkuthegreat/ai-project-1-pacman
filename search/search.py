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

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    stack=Stack()
    visit_node=set()
    start_st=problem.getStartState()
    stack.push((start_st,[]))
    while (len(stack.list)!=0):
        state,path=stack.pop()

        if (state in visit_node):
            continue
        visit_node.add(state)

        if (problem.isGoalState(state)):
            return path

        for succ,act,step_cost in problem.getSuccessors(state):
            if succ not in visit_node:
                    new_path=path+[act]
                    stack.push((succ,new_path))    

    return []


    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue=Queue()
    visit_node=set()
    start_st=problem.getStartState()
    queue.push((start_st,[]))
    while (len(queue.list)!=0):
        state,path=queue.pop()

        if (state in visit_node):
            continue
        visit_node.add(state)

        if (problem.isGoalState(state)):
            return path

        for succ,act,step_cost in problem.getSuccessors(state):
            if succ not in visit_node:
                    new_path=path+[act]
                    queue.push((succ,new_path))    

    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    p_queue=PriorityQueue()
    visit_node=dict()

    start_st=problem.getStartState()
    p_queue.push((start_st,[],0),0)

    while(len(p_queue.heap)!=0):
        state,path,current=p_queue.pop()

        if(state in visit_node and visit_node[state]<=current):
            continue
        visit_node[state]=current

        if(problem.isGoalState(state)):
            return path

        for succ,act,step_cost in problem.getSuccessors(state):
            t_cost=current+step_cost
            if (succ not in visit_node or t_cost< visit_node[succ]):
                p_queue.push((succ,path+[act],t_cost),t_cost)

    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    p_queue=PriorityQueue()
    visit_node=dict()
    
    start_st=problem.getStartState()
    p_queue.push((start_st,[],0),heuristic(start_st,problem))

    while(len(p_queue.heap)!=0):
        state,path,current=p_queue.pop()

        if(state in visit_node and visit_node[state]<=current):
            continue
        visit_node[state]=current

        if(problem.isGoalState(state)):
            return path

        for succ,act,step_cost in problem.getSuccessors(state):
            t_cost=current+step_cost
            if (succ not in visit_node or t_cost< visit_node[succ]):
                pirority=t_cost+heuristic(succ,problem)
                p_queue.push((succ,path+[act],t_cost),pirority)

    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
