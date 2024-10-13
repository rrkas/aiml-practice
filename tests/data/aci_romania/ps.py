import random
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(project_root))

#################

from src.aci.classes import AbstractProblem, AbstractAction, AbstractState
import pandas as pd, numpy as np

_df = pd.read_csv("./aci_romania_map.csv")
_states = set([*_df["FROM"].unique(), *_df["TO"].unique()])

################


class RomaniaAction(AbstractAction):
    def __init__(self, state_name: str):
        super().__init__()
        self.state_name = state_name

    def __str__(self):
        return f"<{self.__class__.__name__} '{self.state_name}'>"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.state_name)

    def __eq__(self, value: "RomaniaAction"):
        return self.state_name == value.state_name


class RomaniaState(AbstractState):
    def __init__(self, state_name: str):
        super().__init__()
        self.state_name = state_name

    def __str__(self):
        return f"<{self.__class__.__name__} '{self.state_name}'>"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.state_name)

    def __eq__(self, value: "RomaniaState"):
        return self.state_name == value.state_name


class RomaniaProblem(AbstractProblem):

    def __init__(
        self,
        initial_state: RomaniaState,
        states: list[RomaniaState],
        goal: RomaniaState,
    ):
        super().__init__(initial_state, states)
        self.goal = goal

        self.transitions: dict[RomaniaState, dict[RomaniaState, float]] = {}
        for idx, row in _df.iterrows():
            from_, to = row["FROM"], row["TO"]
            self.transitions.setdefault(from_, {}).setdefault(to, row["COST"])

            if row["UNI_BI"] == "bi":
                self.transitions.setdefault(to, {}).setdefault(from_, row["COST"])

    def actions(self, s: RomaniaState):
        return self.transitions.get(s.state_name, {}).keys()

    def step_cost(self, s: RomaniaState, a: RomaniaAction):
        return self.transitions.get(s.state_name, {}).get(a.state_name, np.inf)

    def result(self, s: RomaniaState, a: RomaniaAction):
        if self.transitions.get(s.state_name, {}).get(a.state_name, np.inf) == np.inf:
            return None

        return [s2 for s2 in self.states if s2.state_name == a.state_name][0]

    def goal_test(self, state: RomaniaState):
        return self.goal.state_name == state.state_name


################

_state_objs = sorted(
    [RomaniaState(e) for e in _states],
    key=lambda x: x.state_name,
)
ps = RomaniaProblem(
    initial_state=_state_objs[0], states=_state_objs, goal=random.choice(_state_objs)
)
# print(ps.states)
# print(ps.transitions)
# print(_state_objs[0], _state_objs[-1], ps.step_cost(_state_objs[0], _state_objs[-1]))
# print(ps.result(_state_objs[0], RomaniaAction(_state_objs[0].state_name)))
# print(ps.result(_state_objs[0], RomaniaAction(_state_objs[-1].state_name)))
# print(ps.path_cost([RomaniaAction("Zerind"), RomaniaAction("Oradea")]))
