import typing
from src.aci.classes import (
    Node,
    AbstractProblem,
    AbstractState,
    AbstractAction,
    Solution,
)
from src.aci.utils import solution, child_node
from heapq import heapify, heappop, heappush


# function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
def uniform_cost_search(
    problem: AbstractProblem,
) -> typing.Union[Solution, None]:
    # node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    for n in problem.nodes:
        if n.state == problem.initial_state and n.path_cost == 0:
            node = n

    # frontier ← a priority queue ordered by PATH-COST, with node as the only element
    frontier: typing.List[typing.Tuple[float, Node]] = []
    heapify(frontier)

    # explored ← an empty set
    explored: set[AbstractState] = set()

    while True:
        # if EMPTY?(frontier) then return failure
        if frontier.empty():
            return None

        # node ← POP(frontier) /* chooses the lowest-cost node in frontier */
        node = heappop(frontier)
