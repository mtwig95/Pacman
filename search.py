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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):  # q1
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
    # using tree search version
    frontier = util.Stack()  # using a LIFO queue
    startState = problem.getStartState()
    explored = []
    frontier.push((startState, []))  # insert the first node (newState and no actions to the frontier)
    while not frontier.isEmpty():  # if its empty then return failure
        node, actions = frontier.pop()
        if node not in explored:
            if problem.isGoalState(node):
                return actions  # the solution
            else:
                explored.append(node)  # add current node to explored nodes
                successors = problem.getSuccessors(node)
                for newState, newAction, cost in successors:
                    updatedActions = actions + [newAction]
                    childNode = (newState, updatedActions)
                    frontier.push(childNode)  # push successor to the frontier
    return actions


def breadthFirstSearch(problem):  # q2
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()  # using a FIFO queue
    startState = problem.getStartState()
    startNode = (startState, [], 0)  # (state, actions, cost)
    frontier.push(startNode)
    explored = []  # an empty set
    frontier.push(startNode)  # insert the first node (newState and no actions and cost = 0 to the frontier)
    while not frontier.isEmpty():  # if its empty then return failure
        node, actions, cost = frontier.pop()  # choose the shallowest frontier
        if node not in explored:  # and newState not in frontier:
            explored.append(node)  # add current node to explored nodes
            if problem.isGoalState(node):
                return actions  # the solution
            else:
                successors = problem.getSuccessors(node)
                for newState, newAction, newCost in successors:
                    updatedActions = actions + [newAction]
                    updatedCost = cost + newCost
                    childNode = (newState, updatedActions, updatedCost)
                    frontier.push(childNode)  # insert the first node (newState and no actions to the frontier)
    return actions


def uniformCostSearch(problem):  # q3
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()  # using a FIFO queue
    startState = problem.getStartState()
    startNode = (startState, [], 0)  # (state, actions, cost)
    frontier.push(startNode, 0)
    explored = {}  # an empty set
    while not frontier.isEmpty():  # if its empty then return failure
        node, actions, cost = frontier.pop()  # choose the shallowest frontier
        if (node not in explored) or (cost < explored[node]):  # and newState not in frontier or cheaper:
            explored[node] = cost
            # //// explored.append(node)  # add current node to explored nodes
            if problem.isGoalState(node):
                return actions  # the solution
            else:
                successors = problem.getSuccessors(node)
                for newState, newAction, newCost in successors:
                    updatedActions = actions + [newAction]
                    updatedCost = cost + newCost
                    childNode = (newState, updatedActions, updatedCost)
                    frontier.update(childNode,
                                    updatedCost)  # insert the first node (newState and no actions to the frontier)
    return actions


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):  # q4
    """Search the node that has the lowest combined cost and heuristic first."""
    # to be explored (FIFO): takes in item, cost+heuristic
    frontier = util.PriorityQueue()
    exploredNodes = []  # holds (state, cost)
    startState = problem.getStartState()
    startNode = (startState, [], 0)  # (state, action, cost)
    frontier.push(startNode, 0)
    while not frontier.isEmpty():
        # begin exploring first (lowest-combined (cost+heuristic) ) node on frontier
        currentState, actions, currentCost = frontier.pop()
        # put popped node into explored list
        (currentState, currentCost)
        exploredNodes.append((currentState, currentCost))
        if problem.isGoalState(currentState):
            return actions
        else:
            # list of (successor, action, stepCost)
            successors = problem.getSuccessors(currentState)
            # examine each successor
            for succState, succAction, succCost in successors:
                newAction = actions + [succAction]
                newCost = problem.getCostOfActions(newAction)
                newNode = (succState, newAction, newCost)

                # check if this successor has been explored
                already_explored = False
                for explored in exploredNodes:
                    # examine each explored node tuple
                    exploredState, exploredCost = explored
                    if (succState == exploredState) and (newCost >= exploredCost):
                        already_explored = True
                # if this successor not explored, put on frontier and explored list
                if not already_explored:
                    frontier.push(newNode, newCost + heuristic(succState, problem))
                    exploredNodes.append((succState, newCost))
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
