import unittest, os

os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

from tests.search.test_linear import TestLinearSearch
from tests.aci import TestAlgorithms

if __name__ == "__main__":
    unittest.main()
