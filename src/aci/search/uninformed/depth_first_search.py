import typing
from src.aci.classes import Node, AbstractProblem, AbstractState, Solution
from src.aci.utils import solution, child_node
from queue import LifoQueue


# mimicking Breadth-first search on a graph.
# function BREADTH-FIRST-SEARCH(problem) returns a solution, or failure
def depth_first_search(
    problem: AbstractProblem,
    debug=False,
) -> typing.Union[Solution, None]:
    """
    mimicking Breadth-first search on a graph.
    ------------------------------------------------
    title={Book: Artificial Intelligence - A Modern Approach},
    author={{Stuart J. Russell and Peter Norvig}},
    year={2010},
    series={PRENTICE HALL SERIES IN ARTIFICIAL INTELLIGENCE},
    publisher={Pearson},
    """
    # node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    for n in problem.nodes:
        if n.state == problem.initial_state and n.path_cost == 0:
            node = n

    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    if problem.goal_test(node.state):
        return solution(node)

    # frontier ← a FIFO queue with node as the only element
    frontier: LifoQueue[Node] = LifoQueue()
    frontier.put(node)

    # explored ← an empty set
    explored: typing.Set[AbstractState] = set()

    while True:
        if debug:
            print("\n" * 5)
            print("frontier:", frontier.queue)
            print("explored:", explored)

        # if EMPTY?(frontier) then return failure
        if frontier.empty():
            return None

        # node ← POP(frontier) /* chooses the shallowest node in frontier */
        node = frontier.get()

        if debug:
            print(node)

        # add node.STATE to explored
        explored.add(node.state)

        # for each action in problem.ACTIONS(node.STATE) do
        for action in problem.actions(node.state):
            # child ← CHILD-NODE(problem, node, action)
            child = child_node(problem, node, action)

            if debug:
                print(problem, node, action, child)

            # if child.STATE is not in explored or frontier then
            if child.state not in explored and child not in frontier.queue:
                # if problem.GOAL-TEST(child.STATE) then return SOLUTION(child)
                if problem.goal_test(child.state):
                    return solution(child)

                # frontier ← INSERT(child, frontier)
                frontier.put(child)
