import typing
from action import AbstractAction
from state import AbstractState


class Node:
    """
    node n of the tree have a structure that contains four components:
    1. n.STATE: the state in the state space to which the node corresponds
    2. n.PARENT: the node in the search tree that generated this node
    3. n.ACTION: the action that was applied to the parent to generate the node
    4. n.PATH-COST: the cost, traditionally denoted by g(n), of the path from the initial state to the node, as indicated by the parent pointers
    ------------------------------------------------
    title={Book: Artificial Intelligence - A Modern Approach},
    author={{Stuart J. Russell and Peter Norvig}},
    year={2010},
    series={PRENTICE HALL SERIES IN ARTIFICIAL INTELLIGENCE},
    publisher={Pearson},
    """

    def __init__(
        self,
        action: AbstractAction,
        parent: "Node",
        path_cost: float,
        state: AbstractState,
    ):
        self.action: AbstractAction = action
        self.parent: "Node" = parent
        self.path_cost: float = path_cost
        self.state: AbstractState = state
