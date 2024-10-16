import typing, numpy as np
from src.aci.classes import Node, AbstractProblem, Solution
from src.aci.utils import solution, child_node
from custom_logger import get_logger

_logger = get_logger("RBFS")


# function RECURSIVE-BEST-FIRST-SEARCH(problem) returns a solution, or failure
def recursive_best_first_search(
    problem: AbstractProblem,
    max_f_limit: float = 1000,
    debug: bool = False,
) -> typing.Union[Solution, None]:
    # return RBFS(problem, MAKE-NODE(problem.INITIAL-STATE),∞)
    problem.initial_node.f_value = (
        problem.initial_node.path_cost + problem.initial_node.state.heuristic_value
    )

    cutoff, result = rbfs(
        debug=debug,
        problem=problem,
        f_limit=max_f_limit,
        node=problem.initial_node,
    )

    if debug:
        _logger.debug(f"{cutoff} {result} {solution(result) if cutoff else None}")

    return cutoff, (solution(result) if result is not None else None)


# function RBFS(problem,node,f limit) returns a solution, or failure and a new f-cost limit
def rbfs(
    problem: AbstractProblem,
    node: Node,
    f_limit: float,
    debug: bool = False,
) -> typing.Tuple[bool, typing.Union[Node, None]]:
    if debug:
        _logger.debug(f"{problem} {node} {f_limit}")

    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    if problem.goal_test(node.state):
        return False, node

    # successors ← []
    successors: typing.List[Node] = []

    # for each action in problem.ACTIONS(node.STATE) do
    for action in problem.actions(node.state):
        if debug:
            _logger.debug(f"action: {node} {action}")

        # add CHILD-NODE(problem,node,action) into successors
        child = child_node(problem=problem, parent=node, action=action)
        child.f_value = child.path_cost + child.state.heuristic_value

        successors.append(child)

    successors.sort(key=lambda x: x.f_value)

    if debug:
        _logger.debug(f"{successors}")

    # if successors is empty then return failure, ∞
    if len(successors) == 0:
        return True, None

    # for each s in successors do /* update f with value from previous search, if any */
    for s in successors:
        # s.f ← max(s.g + s.h, node.f ))
        s.f_value = max(s.f_value, node.f_value)

    while True:
        if len(successors) == 0:
            return True, None

        # best ← the lowest f-value node in successors
        best = successors.pop(0)

        # if best.f > f limit then return failure, best.f
        if best.f_value > f_limit:
            return True, best

        # ADDITIONAL CONDITION
        # if no alternative successors are there, no solution
        if len(successors) == 0:
            return True, best

        # alternative ← the second-lowest f-value among successors
        alternative = successors.pop(0)

        # result,best.f ← RBFS(problem,best,min(f_limit, alternative))
        cutoff, best = rbfs(
            problem=problem,
            node=best,
            f_limit=min(f_limit, alternative.f_value),
        )

        # if result ̸= failure then return result
        if not cutoff:
            return False, best
