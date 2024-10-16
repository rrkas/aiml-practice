import typing
from src.aci.classes import Node, AbstractProblem, Solution
from src.aci.utils import solution, child_node


def iterative_deepening_a_star_search(
    problem: AbstractProblem,
    max_f_limit: float = 1000,
    debug: bool = False,
) -> typing.Union[Solution, None]:
    i = 1
    while (2**i) <= max_f_limit:

        cutoff, result = recursive_f_cost_limited_search(
            debug=debug,
            f_limit=2**i,
            problem=problem,
            node=problem.initial_node,
        )

        if debug:
            print(2**i, cutoff, result)

        if not cutoff:
            return result

        i += 1


# taking inspiration from DLS with limit on f-value instead of depth
def recursive_f_cost_limited_search(
    node: Node,
    problem: AbstractProblem,
    f_limit: int,
    debug: bool = False,
) -> typing.Tuple[bool, typing.Union[Solution, None]]:
    if debug:
        print(node, problem, f_limit)

    if problem.goal_test(node.state):
        return False, solution(node)

    elif node.path_cost + node.state.heuristic_value > f_limit:
        return True, solution(node)

    else:
        cutoff_occurred = False
        for action in problem.actions(node.state):

            child = child_node(problem, node, action)

            cutoff_occurred, result = recursive_f_cost_limited_search(
                node=child,
                debug=debug,
                problem=problem,
                f_limit=f_limit,
            )

            if not cutoff_occurred and result is not None:
                return False, result

        if cutoff_occurred:
            return True, solution(node)
        else:
            return False, None
