import typing
from state import AbstractState
from action import AbstractAction
from node import Node


class AbstractProblem:
    """
    A problem can be defined formally by five components:
    1. The **initial state** that the agent starts in.
    2. A description of the possible **actions** available to the agent.
    3. A description of what each action does; the formal name for this is the **transition model**, specified by a function `RESULT(s, a)` that returns the state that results from doing action `a` in state `s`.
    4. The **goal test**, which determines whether a given state is a goal state.
    5. A **path cost** function that assigns a numeric cost to each path.
    ------------------------------------------------
    title={Book: Artificial Intelligence - A Modern Approach},
    author={{Stuart J. Russell and Peter Norvig}},
    year={2010},
    series={PRENTICE HALL SERIES IN ARTIFICIAL INTELLIGENCE},
    publisher={Pearson},
    """

    def __init__(
        self,
        initial_state: AbstractState,
        states: typing.List[AbstractState],
    ):
        self.initial_state: AbstractState = initial_state
        self.nodes: typing.List[Node] = []
        self.states: typing.List[AbstractState] = states

    def actions(self, s: AbstractState) -> typing.List[AbstractAction]:
        """
        Given a particular state s, ACTIONS(s) returns the set of actions that can be executed in s.
        """
        raise NotImplementedError()

    def result(self, s: AbstractState, a: AbstractAction) -> AbstractState:
        """
        A description of what each action does; the formal name for this is the **transition model**, specified by a function `RESULT(s, a)` that returns the state that results from doing action `a` in state `s`.
        """
        raise NotImplementedError()

    def goal_test(self, state: AbstractState) -> bool:
        """
        The goal test, which determines whether a given state is a goal state.
        """
        return NotImplementedError()

    def step_cost(
        self,
        s: AbstractState,
        a: AbstractAction,
    ) -> float:
        """
        The step cost of taking action `a` in state `s` to reach state `s2` is denoted by `c(s, a, s2)`.
        """
        return NotImplementedError()

    def path_cost(self, path: typing.List[AbstractAction]) -> float:
        """
        A path cost function that assigns a numeric cost to each path.
        """
        return NotImplementedError()
