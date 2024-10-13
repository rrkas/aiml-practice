import typing
from classes import AbstractProblem, Solution, Node
from utils import solution
from queue import Queue


def tree_search(problem: AbstractProblem) -> typing.Union[Solution, None]:
    frontier: Queue[Node] = Queue()

    while True:
        if frontier.empty():
            return None

        node = frontier.get()

        if problem.goal_test(node):
            return solution(node)

        for action in problem.actions:
            frontier.put(problem.result(node, action))
