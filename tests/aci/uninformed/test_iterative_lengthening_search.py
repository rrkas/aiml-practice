import random
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(project_root))

#################

import random, pandas as pd
from src.aci.search.uninformed.iterative_lengthening_search import (
    iterative_lengthening_search,
)
from tests.samples.aci_romania.ps import RomaniaProblem, RomaniaAction, RomaniaState

df = pd.read_csv(project_root / "tests/samples/aci_romania/aci_romania_map.csv")

states = sorted(set([*df["FROM"].unique(), *df["TO"].unique()]))
state_objs = [RomaniaState(s) for s in states]

start_state = random.choice(state_objs)
goal_state = random.choice([e for e in state_objs if e != start_state])


problem = RomaniaProblem(
    states=state_objs,
    initial_state=start_state,
    initial_action=RomaniaAction("__START__"),
    goal=goal_state,
    data=df,
)


if __name__ == "__main__":
    print(start_state, goal_state)

    sol = iterative_lengthening_search(problem=problem)
    print(sol)
    if sol:
        print(problem.path_cost(sol))
