import unittest, random


class TestAlgorithms(unittest.TestCase):
    def test_ucs(self):
        from .uninformed.test_uniform_cost_search import problem, uniform_cost_search

        sol = uniform_cost_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_ils(self):
        from .uninformed.test_iterative_lengthening_search import (
            problem,
            iterative_lengthening_search,
        )

        sol = iterative_lengthening_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_ids(self):
        from .uninformed.test_iterative_deepening_search import (
            problem,
            iterative_deepening_search,
        )

        sol = iterative_deepening_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_dls(self):
        from .uninformed.test_depth_limited_search import (
            problem,
            depth_limited_search,
        )

        limit = random.randint(1, len(problem.states) // 2)

        cutoff, sol = depth_limited_search(problem, limit)

        self.assertFalse(cutoff)
        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1 and len(sol) <= limit + 1)

    def test_dfs(self):
        from .uninformed.test_depth_first_search import (
            problem,
            depth_first_search,
        )

        sol = depth_first_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_bfs(self):
        from .uninformed.test_breadth_first_search import (
            problem,
            breadth_first_search,
        )

        sol = breadth_first_search(problem)

        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_gbfs(self):
        from .informed.test_greedy_best_first_search import (
            problem,
            greedy_best_first_search,
        )

        sol = greedy_best_first_search(problem)
        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_a_star(self):
        from .informed.test_a_star_search import (
            problem,
            a_star_search,
        )

        sol = a_star_search(problem)
        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_ida_star(self):
        from .informed.test_iterative_deepening_a_star_search import (
            problem,
            iterative_deepening_a_star_search,
        )

        sol = iterative_deepening_a_star_search(problem)

        print(problem.initial_node, problem.goal, len(sol), sol)

        # can result to cutoff and no result
        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)

    def test_rbfs(self):
        from .informed.test_recursive_best_first_search import (
            problem,
            recursive_best_first_search,
        )

        cutoff, sol = recursive_best_first_search(problem)

        # print(problem.initial_node, problem.goal, len(sol), sol)

        # can result to cutoff and no result
        self.assertIsNot(sol, None)
        self.assertTrue(len(sol) > 1)
