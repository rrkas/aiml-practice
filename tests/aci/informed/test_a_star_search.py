import random
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(project_root))

#################

import random, pandas as pd, numpy as np
from src.aci.search.informed.a_star_search import a_star_search
from tests.samples.aci_romania.ps import RomaniaProblem, RomaniaAction, RomaniaState

df = pd.read_csv(project_root / "tests/samples/aci_romania/aci_romania_map.csv")
df_heuristic = pd.read_csv(project_root / "tests/samples/aci_romania/h_sld.csv")

heuristic_map = {row["CITY"]: row["H_SLD"] for _, row in df_heuristic.iterrows()}

states = sorted(set([*df["FROM"].unique(), *df["TO"].unique()]))
state_objs = [
    RomaniaState(
        s,
        heuristic_value=heuristic_map.get(s, np.inf),
    )
    for s in states
]

start_state = random.choice([e for e in state_objs if e.heuristic_value != 0])
goal_state = random.choice([e for e in state_objs if e.heuristic_value == 0])


problem = RomaniaProblem(
    states=state_objs,
    initial_state=start_state,
    initial_action=RomaniaAction("__START__"),
    goal=goal_state,
    data=df,
)

if __name__ == "__main__":
    print(start_state, goal_state)

    sol = a_star_search(problem=problem, debug=True)
    print(sol)
    if sol:
        print(problem.path_cost(sol))
