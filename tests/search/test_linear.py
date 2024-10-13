import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.absolute()

sys.path.insert(0, str(project_root))

###############

import unittest, random
from src.search.linear import *


class TestLinearSearch(unittest.TestCase):
    _list = list(range(100)) + [80]
    _e1 = 80
    _e2 = 5000
    _pos = None

    @classmethod
    def setUpClass(cls):
        random.shuffle(cls._list)
        cls._pos = cls._list.index(cls._e1)

    def test_list(self):
        self.assertEqual(linear_search_optimal(self._list, self._e1), self._pos)
        self.assertEqual(linear_search_scratch(self._list, self._e1), self._pos)

        self.assertEqual(linear_search_optimal(self._list, self._e2), None)
        self.assertEqual(linear_search_scratch(self._list, self._e2), None)

    def test_np(self):
        _np_array = np.array(self._list)
        self.assertEqual(linear_search_optimal(_np_array, self._e1), self._pos)
        self.assertEqual(linear_search_scratch(_np_array, self._e1), self._pos)
        self.assertEqual(linear_search_optimal(_np_array, self._e2), None)
        self.assertEqual(linear_search_scratch(_np_array, self._e2), None)

    def test_torch(self):
        _torch_tensor = torch.tensor(self._list)
        self.assertEqual(linear_search_optimal(_torch_tensor, self._e1), self._pos)
        self.assertEqual(linear_search_scratch(_torch_tensor, self._e1), self._pos)
        self.assertEqual(linear_search_optimal(_torch_tensor, self._e2), None)
        self.assertEqual(linear_search_scratch(_torch_tensor, self._e2), None)

    def test_tf(self):
        _tf_tensor = tf.convert_to_tensor(self._list)
        self.assertEqual(linear_search_optimal(_tf_tensor, self._e1), self._pos)
        self.assertEqual(linear_search_scratch(_tf_tensor, self._e1), self._pos)
        self.assertEqual(linear_search_optimal(_tf_tensor, self._e2), None)
        self.assertEqual(linear_search_scratch(_tf_tensor, self._e2), None)
