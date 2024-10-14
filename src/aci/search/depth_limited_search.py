import typing
from src.aci.classes import Node, AbstractProblem, AbstractState, Solution
from src.aci.utils import solution, child_node


# function DEPTH-LIMITED-SEARCH(problem,limit) returns a solution, or failure/cutoff
def depth_limited_search(
    problem: AbstractProblem,
    limit: int = 1000,
    debug: bool = False,
) -> typing.Tuple[bool, typing.Union[Solution, None]]:

    # return RECURSIVE-DLS(MAKE-NODE(problem.INITIAL-STATE),problem,limit)
    return recursive_dls(
        node=problem.initial_node,
        problem=problem,
        limit=limit,
        debug=debug,
    )


# function RECURSIVE-DLS(node,problem,limit) returns a solution, or failure/cutoff
def recursive_dls(
    node: Node,
    problem: AbstractProblem,
    limit: int,
    debug: bool = False,
) -> typing.Tuple[bool, typing.Union[Solution, None]]:

    if debug:
        print(node, problem, limit)

    # if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
    if problem.goal_test(node.state):
        return False, solution(node)

    # else if limit = 0 then return cutoff
    elif limit == 0:
        return True, solution(node)

    else:
        cutoff_occurred = False
        # for each action in problem.ACTIONS(node.STATE) do
        for action in problem.actions(node.state):

            # child ← CHILD-NODE(problem,node,action)
            child = child_node(problem, node, action)

            # print(node, action, child)

            # result ← RECURSIVE-DLS(child,problem,limit − 1)
            # if result = cutoff then cutoff occurred? ← true
            cutoff_occurred, result = recursive_dls(
                child, problem, limit - 1, debug=debug
            )

            # else if result ̸= failure then return result
            if not cutoff_occurred and result is not None:
                return False, result

        # if cutoff occurred? then return cutoff else return failure
        if cutoff_occurred:
            return True, solution(node)
        else:
            return False, None
