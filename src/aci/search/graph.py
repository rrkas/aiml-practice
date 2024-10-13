import typing
from classes import AbstractProblem, Solution, Node
from utils import solution
from queue import Queue


def graph_search(problem: AbstractProblem) -> typing.Union[Solution, None]:
    frontier: Queue[Node] = Queue()
    explored = set()

    while True:
        if frontier.empty():
            return None

        node = frontier.get()

        if problem.goal_test(node):
            return solution(node)

        explored.add(node)

        for action in problem.actions:
            next_state = problem.result(node, action)
            if next_state not in frontier and next_state not in explored:
                frontier.put(next_state)
