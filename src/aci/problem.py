"""
@book{aci-1,
    title={Book: Artificial Intelligence - A Modern Approach},
    author={{Stuart J. Russell and Peter Norvig}},
    year={2010},
    series={PRENTICE HALL SERIES IN ARTIFICIAL INTELLIGENCE},
    publisher={Pearson},
}
"""

import typing
from state import AbstractState
from action import AbstractAction


class AbstractProblem:
    def __init__(
        self,
        states: typing.List[AbstractState],
        initial_state: AbstractState,
        actions: typing.List[AbstractAction],
    ):
        self.states: typing.List[AbstractState] = states
        self.initial_state: AbstractState = initial_state
        self.actions: typing.List[AbstractAction] = actions

    def result(self, state: AbstractState, action: AbstractAction) -> AbstractState:
        """transition model"""
        raise NotImplementedError()

    def goal_test(self, state: AbstractState) -> bool:
        """check if state is goal state or not"""
        return NotImplementedError()

    def c(
        self,
        state: AbstractState,
        action: AbstractAction,
        next_state: AbstractState,
    ) -> float:
        """step cost: cost to move from state s to next_state s' using an action a c(s,a,s')"""
        return NotImplementedError()

    def path_cost(self, path: typing.List[AbstractAction]) -> float:
        """cost of path (list of actions)"""
        return NotImplementedError()
