import unittest
from ex_3_v2_classes import *
import ex_3_v2_sol

class TestEx_3(unittest.TestCase):

    def test_no1(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(1, 1, 1, [1, 1]), 1)

    def test_no2(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(1, 2, 1, [1, 1]), 2)

    def test_no3(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(2, 2, 2, [1, 1, 2, 2]), 2)

    def test_no4(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(2, 2, 1, [1, 1]), 3)

    def test_no5(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(3, 3, 1, [1, 1]), 5)

    def test_no6(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(3, 3, 3, [1, 1, 2, 2, 3, 3]), 3)

    def test_no7(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(3, 4, 2, [2, 2, 3, 4]), 3)

    def test_no8(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(3, 3, 6, [1, 1, 2, 2, 3, 3, 2, 2, 3, 3, 1, 1]), 3)

    def test_no9(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(4, 4, 1, [1, 1]), 7)

    def test_no10(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(4, 4, 3, [3, 1, 4, 4, 1, 4]), 3)

    def test_no11(self):
        self.assertEqual(ex_3_v2_sol.ConquestCampaign(5, 5, 5, [3, 3, 1, 1, 5, 2, 1, 1, 3, 3]), 5)


if __name__ == "__main__":
    unittest.main()
