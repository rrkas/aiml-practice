import typing
from . import AbstractProblem, AbstractAction, Node, Solution


def child_node(
    problem: AbstractProblem,
    parent: Node,
    action: AbstractAction,
) -> Node:
    """
    The function CHILD-NODE takes a parent node and an action and returns the resulting child node
    ------------------------------------------------
    title={Book: Artificial Intelligence - A Modern Approach},
    author={{Stuart J. Russell and Peter Norvig}},
    year={2010},
    series={PRENTICE HALL SERIES IN ARTIFICIAL INTELLIGENCE},
    publisher={Pearson},
    """
    # return a node with
    for node in problem.nodes:
        if (
            # STATE = problem.RESULT(parent.STATE,action)
            (node.state == problem.result(node.parent.state, action))
            # PARENT = parent
            and (node.parent == parent)
            # ACTION = action
            and (node.action == action)
            # PATH-COST = parent.PATH-COST + problem.STEP-COST(parent.STATE, action)
            and (
                node.path_cost
                == (
                    node.parent.path_cost
                    + problem.step_cost(
                        node.parent.state,
                        action,
                    )
                )
            )
        ):
            return node


def solution(node: Node) -> Solution:
    actions: AbstractAction = []
    n = node
    while n.parent is not None:
        actions.append(n.action)
        n = n.parent

    return actions[::-1]
