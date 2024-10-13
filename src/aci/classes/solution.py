import typing
from action import AbstractAction

"""
A solution to a problem is an "action sequence" that leads from the initial state to a goal state.
------------------------------------------------
title={Book: Artificial Intelligence - A Modern Approach},
author={{Stuart J. Russell and Peter Norvig}},
year={2010},
series={PRENTICE HALL SERIES IN ARTIFICIAL INTELLIGENCE},
publisher={Pearson},
"""
Solution = typing.List[AbstractAction]
