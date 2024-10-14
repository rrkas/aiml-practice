import typing, pandas as pd
from .state import AbstractState
from .action import AbstractAction
from .node import Node


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
        initial_action: AbstractAction,
        states: typing.Set[AbstractState],
        debug: bool = False,
    ):
        self.debug: bool = debug
        self.initial_state: AbstractState = initial_state
        self.nodes: typing.List[Node] = [
            Node(initial_action, None, 0, self.initial_state)
        ]
        self.states: typing.Set[AbstractState] = states

        assert all(isinstance(e, AbstractState) for e in states)
        assert self.initial_state in self.states

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
        cost = 0
        s = self.initial_state

        trace = []

        for a in path[1:]:
            c = self.step_cost(s, a)
            cost += c
            trace.append((s, a, c, cost))

            s = self.result(s, a)

        if self.debug:
            print(
                pd.DataFrame(
                    trace,
                    columns=["FROM", "TO", "COST", "CUMM_COST"],
                ).to_string()
            )

        return cost

    def __str__(self):
        return f"<{self.__class__.__name__} {hash(self)}>"

    def __repr__(self):
        return str(self)
