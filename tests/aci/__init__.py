import unittest, random


class TestAlgorithms(unittest.TestCase):
    def test_ucs(self):
        from .test_uniform_cost_search import problem, uniform_cost_search

        sol = uniform_cost_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_ils(self):
        from .test_iterative_lengthening_search import (
            problem,
            iterative_lengthening_search,
        )

        sol = iterative_lengthening_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_ids(self):
        from .test_iterative_deepening_search import (
            problem,
            iterative_deepening_search,
        )

        sol = iterative_deepening_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_dls(self):
        from .test_depth_limited_search import (
            problem,
            depth_limited_search,
        )

        limit = random.randint(1, len(problem.states) // 2)

        sol = depth_limited_search(problem, limit)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1 and len(sol) <= limit + 1)

    def test_dfs(self):
        from .test_depth_first_search import (
            problem,
            depth_first_search,
        )

        sol = depth_first_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_bfs(self):
        from .test_breadth_first_search import (
            problem,
            breadth_first_search,
        )

        sol = breadth_first_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)
