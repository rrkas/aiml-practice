import random
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.absolute()
sys.path.insert(0, str(project_root))

#################

import random, pandas as pd
from src.aci.search.depth_limited_search import depth_limited_search
from src.aci.search.depth_first_search import depth_first_search
from tests.samples.aci_romania.ps import RomaniaProblem, RomaniaAction, RomaniaState

df = pd.read_csv("../samples/aci_romania/aci_romania_map.csv")

states = sorted(set([*df["FROM"].unique(), *df["TO"].unique()]))
state_objs = [RomaniaState(s) for s in states]

start_state = random.choice(state_objs)
goal_state = random.choice(state_objs)

print(start_state, goal_state)

problem = RomaniaProblem(
    states=state_objs,
    initial_state=start_state,
    initial_action=RomaniaAction("__START__"),
    goal=goal_state,
    data=df,
    debug=True,
)

limit = 5
# for limit in range(5,20,5):
cutoff, sol = depth_limited_search(problem=problem, limit=limit)
print(limit, cutoff, sol)
if sol:
    print(problem.path_cost(sol))


sol = depth_first_search(problem=problem)
print(sol)
if sol:
    print(problem.path_cost(sol))
