"""
In search.py, you will implement generic search algorithms
"""

import util
import numpy as np


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

	print("Start:", problem.get_start_state().state)
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:", problem.get_successors(problem.get_start_state()))
    """
    return general_search(problem, util.Stack())


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    return general_search(problem, util.Queue())


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    def priority_func(node):
        return node.cost
    return general_search(problem, util.PriorityQueueWithFunction(priority_func))


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    def f(node):
        return node.cost + heuristic(node.value[0], problem=problem)

    return general_search(problem, util.PriorityQueueWithFunction(f))


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        if parent is not None:
            self.cost = parent.cost + value[2]
        else:
            self.cost = value[2]


def general_search(problem, fringe):
    """
    implementation of the general search algorithm.
    the function gets a problem and a fringe (different data-structures)
    and returns a list of actions that reaches the goal.
    """
    start_state = problem.get_start_state()
    root = Node((start_state, None, 0))
    fringe.push(root)
    if start_state.__hash__ is None:
        is_hash = False
        closed = list()
    else:
        is_hash = True
        closed = set()
    while not fringe.isEmpty():
        current = fringe.pop()
        if problem.is_goal_state(current.value[0]):
            # create the solution - going back from the solution to the root
            solution = []
            while current is not root:
                solution.append(current.value[1])
                current = current.parent
            return solution[::-1]
        else:
            if current.value[0] not in closed:
                next_successors = problem.get_successors(current.value[0])
                for successor in next_successors:
                    fringe.push(Node(successor, parent=current))  # update the tree and the fringe
                if is_hash:
                    closed.add(current.value[0])
                else:
                    closed.append(current.value[0])
    return []  # no solution


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
