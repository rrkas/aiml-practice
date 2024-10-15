import typing
from src.aci.classes import AbstractProblem, Solution
from .depth_limited_search import depth_limited_search


def iterative_deepening_search(
    problem: AbstractProblem,
    max_limit: int = 1000,
    debug: bool = False,
) -> typing.Tuple[bool, typing.Union[Solution, None]]:
    for depth in range(0, max_limit):
        cutoff, result = depth_limited_search(
            problem,
            depth,
            debug=debug,
        )

        if debug:
            print(depth, cutoff, result)

        if not cutoff:
            return result
