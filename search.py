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
import random
import searchAgents


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
    "*** YOUR CODE HERE ***"
    # print ("Start:", problem.getStartState())
    # print ("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print ("Start's successors:", problem.getSuccessors(problem.getStartState()))
    state=problem.getStartState()
    # print("state",state)

    closed=[]
    fringe=[]

    fringe.append((state,[]))

    while fringe:
        node,actions=fringe.pop()

        if problem.isGoalState(node):
            return actions

        if node not in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                fringe.append((child[0],actions+[child[1]]))
    if not fringe:
        print("the fringe is empty cuz")


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    state=problem.getStartState()
    # print("state",state)

    closed=[]
    fringe=[]

    fringe.append((state,[]))

    while fringe:
        #This is the only change needed, Instead of taking the most recently added node from the stack
        # which would be the ones that are the deepest in the tree, it takes to oldest ones, which would
        # have been added first
        node,actions=fringe.pop(0)

        if problem.isGoalState(node):
            return actions

        if node not in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                fringe.append((child[0],actions+[child[1]]))
    if not fringe:
        print("the fringe is empty cuz")

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    state=problem.getStartState()
    # print("state",state)

    closed=[]
    fringe=[]

    fringe.append((state,[],0))

    # print("The min index is: ", popindex, "for the following item: ", fringe[popindex])

    while fringe:
        # print("The fringe is:", fringe)
        minimum = min(fringe, key=lambda x: x[2])
        popindex = fringe.index(minimum)
        # print("The minimum value is apparently:", minimum, " and it has the index in fringe of: ", popindex)
        node,actions,cost=fringe.pop(popindex)
        # print("This is what we chose to pop:", node,actions,cost)
        # input('')
        if problem.isGoalState(node):
            return actions

        if node not in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                fringe.append((child[0],actions+[child[1]],cost+child[2]))

    if not fringe:
        print("the fringe is empty cuz")

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    print("The problem is:", problem)
    closed=[]
    fringe=[]
    state=problem.getStartState()
    start_forward_Cost=searchAgents.manhattanHeuristic(state,problem)
    fringe.append((state,[],start_forward_Cost))

    # print("The min index is: ", popindex, "for the following item: ", fringe[popindex])

    while fringe:
        # print("The fringe is:", fringe)
        minimum = min(fringe, key=lambda x: x[2])
        popindex = fringe.index(minimum)
        # print("The minimum value is apparently:", minimum, " and it has the index in fringe of: ", popindex)
        node,actions,Back_Cost=fringe.pop(popindex)
        # print("This is what we chose to pop:", node,actions,cost)
        # input('')
        if problem.isGoalState(node):
            return actions

        if node not in closed:
            closed.append(node)
            for child in problem.getSuccessors(node):
                Forward_cost=searchAgents.manhattanHeuristic(child[0],problem)
                fringe.append((child[0],actions+[child[1]],Back_Cost+Forward_cost+child[2]))

    if not fringe:
        print("the fringe is empty cuz")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
