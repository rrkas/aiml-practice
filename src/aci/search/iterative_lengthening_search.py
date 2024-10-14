import typing
from src.aci.classes import Node, AbstractProblem, AbstractState, Solution
from src.aci.utils import solution, child_node
from heapq import heapify, heappop, heappush

"""
The idea is to use increasing path-cost limits instead of increasing depth limits. The resulting algorithm, called "iterative lengthening search".
"""


def iterative_lengthening_search(
    problem: AbstractProblem,
    max_path_cost_limit: int = 10000,
    debug: bool = False,
) -> typing.Union[None, Solution]:
    i = 1
    while 2**i < max_path_cost_limit:
        cutoff, result = ucs_cost_limit_search(
            problem=problem,
            path_cost_limit=2**i,
            debug=debug,
        )

        if debug:
            print(2**i, cutoff, result)

        if not cutoff:
            return result

        i += 1


def ucs_cost_limit_search(
    problem: AbstractProblem,
    path_cost_limit: int,
    debug: bool = False,
) -> typing.Tuple[bool, typing.Union[None, Solution]]:
    # node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    for n in problem.nodes:
        if n.state == problem.initial_state and n.path_cost == 0:
            node = n

    # frontier ← a priority queue ordered by PATH-COST, with node as the only element
    frontier: typing.List[typing.Tuple[float, Node]] = [(0, node)]
    heapify(frontier)

    # explored ← an empty set
    explored: typing.Set[AbstractState] = set()

    while True:
        # if EMPTY?(frontier) then return failure
        if len(frontier) == 0:
            return False, None

        # if all paths are more than limit, cutoff
        # if at least one path is below limit, let's explore
        if all([e[0] > path_cost_limit for e in frontier]):
            return True, None

        # node ← POP(frontier) /* chooses the lowest-cost node in frontier */
        path_cost, node = heappop(frontier)

        # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        if problem.goal_test(node.state):
            return False, solution(node)

        # add node.STATE to explored
        explored.add(node.state)

        # for each action in problem.ACTIONS(node.STATE) do
        for action in problem.actions(node.state):
            # child ← CHILD-NODE(problem,node,action)
            child = child_node(problem, node, action)

            frontier_states = [e.state for (_, e) in frontier]

            # if child.STATE is not in explored or frontier then
            if child.state not in explored and child.state not in frontier_states:

                # frontier ← INSERT(child,frontier)
                heappush(frontier, (child.path_cost, child))

                # re-order priority queue
                heapify(frontier)

            # else if child.STATE is in frontier with higher PATH-COST then
            elif child.state in frontier_states:
                idx = frontier_states.index(child.state)
                frontier_node = frontier[idx][1]
                if frontier_node.path_cost > child.path_cost:

                    # replace that frontier node with child
                    frontier[idx] = (child.path_cost, child)

                    # re-order priority queue
                    heapify(frontier)
