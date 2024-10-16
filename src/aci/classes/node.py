import typing
from . import AbstractAction
from .state import AbstractState


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

        # can be path_cost, can be state.heuristic or can be something else
        self.f_value: float = None

    def __str__(self):
        return f"<{self.__class__.__name__} action={self.action} parent=self.parent path_cost={self.path_cost} f_value={self.f_value} state={self.state} {hash(self)}>"

    def __repr__(self):
        return str(self)

    def __gt__(self, other: "Node"):
        return self.f_value > other.f_value

    def __ge__(self, other: "Node"):
        return self.f_value >= other.f_value

    def __lt__(self, other: "Node"):
        return self.f_value < other.f_value

    def __le__(self, other: "Node"):
        return self.f_value <= other.f_value
