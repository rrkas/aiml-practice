import typing, operator
from src.aci.classes import Node, AbstractProblem, AbstractState, Solution
from src.aci.utils import solution, child_node
from heapq import heapify, heappop, heappush


def greedy_best_first_search(
    problem: AbstractProblem,
    debug: bool = False,
) -> typing.Union[Solution, None]:
    for n in problem.nodes:
        if n.state == problem.initial_state and n.path_cost == 0:
            node = n

    explored: typing.Set[AbstractState] = set()

    while True:
        if debug:
            print("node:", node)
            print("explored:", explored)

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node.state)

        children = []
        for action in problem.actions(node.state):
            child = child_node(problem, node, action)

            if child.state in explored:
                continue

            children.append((child.state.heuristic_value, child))

        if debug:
            print("children:", children)

        if len(children) == 0:
            return None

        heapify(children)

        node = children[0][1]
