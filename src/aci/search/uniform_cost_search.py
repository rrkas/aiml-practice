import typing
from src.aci.classes import Node, AbstractProblem, AbstractState, Solution
from src.aci.utils import solution, child_node
from heapq import heapify, heappop, heappush


# function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
def uniform_cost_search(
    problem: AbstractProblem,
    debug: bool = False,
) -> typing.Union[Solution, None]:
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
            return None

        # node ← POP(frontier) /* chooses the lowest-cost node in frontier */
        path_cost, node = heappop(frontier)

        # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        if problem.goal_test(node.state):
            return solution(node)

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
