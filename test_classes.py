import unittest
from ex_3_v2_classes import *


class TestSquare(unittest.TestCase):

    def setUp(self):
        self.free_neighbor = Square(4,2)
        self.captured_neighbor = Square(5,3)
        self.captured_neighbor.set_status(True)
        self.square = Square(5,2)
        self.square.set_neighbors([self.free_neighbor, self.captured_neighbor])

    def test_object_field_and_methods(self):
        self.assertEqual(self.square.get_id(), "h5w2")
        self.assertEqual(self.square.get_height(), 5)
        self.assertEqual(self.square.get_width(), 2)
        self.assertIs(self.square.get_status(), False)
        self.square.set_status(True)
        self.assertIs(self.square.get_status(), True)
        self.assertEqual(self.square.get_neighbors(), [self.free_neighbor, self.captured_neighbor])
        self.assertEqual(self.square.get_neighbors(True), [self.free_neighbor])


class TestCompaignMap1x1(unittest.TestCase):

    def setUp(self):
        self.map1x1 = CompaignMap()

    def test_object_fields(self):
        self.assertEqual(self.map1x1.height, 1)
        self.assertEqual(self.map1x1.width, 1)

    def test_get_squares_ids(self):
        squares_ids_correct = set(["h1w1"])
        squares_ids_test = self.map1x1.get_squares_ids()
        self.assertEqual(squares_ids_test, squares_ids_correct)

    def test_get_neighbors_squares_ids(self):
        neighbors_ids_correct = set()
        neighbors_ids_test = self.map1x1.get_square_neighbors_ids("h1w1")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)


class TestCompaignMap3x3(unittest.TestCase):

    def setUp(self):
        self.map3x3 = CompaignMap(3,3)

    def test_object_fields(self):
        self.assertEqual(self.map3x3.height, 3)
        self.assertEqual(self.map3x3.width, 3)

    def test_get_squares_ids(self):
        squares_ids_correct = set(["h1w1",
                                   "h2w1",
                                   "h3w1",
                                   "h1w2",
                                   "h2w2",
                                   "h3w2",
                                   "h1w3",
                                   "h2w3",
                                   "h3w3",])
        squares_ids_test = self.map3x3.get_squares_ids()
        self.assertEqual(squares_ids_test, squares_ids_correct)

    # id1 "h1w1";  ["h1w2", "h2w1",] 
    # id2 "h2w1" -- ["h1w1", "h2w2", "h3w1"]
    # id3 "h3w1" -- ["h2w1", "h3w2",]
    # id4 "h1w2" -- ["h1w1", "h2w2", "h1w2",]
    # id5 "h2w2" -- ["h2w1", "h1w2", "h2w3", "h3w2"]
    # id6 "h3w2" -- ["h3w1", "h2w2", "h3w3",]
    # id7 "h1w3" -- ["h1w2", "h2w3",]
    # id8 "h2w3" -- ["h1w3", "h2w2", "h3w3"]
    # id9 "h3w3" -- ["h3w2", "h2w3",]
    def test_get_neighbors_squares_ids__id1(self):
        neighbors_ids_correct = set(["h1w2", "h2w1",] )
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h1w1")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id2(self):
        neighbors_ids_correct = set(["h1w1", "h2w2", "h3w1"])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h2w1")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id3(self):
        neighbors_ids_correct = set(["h2w1", "h3w2",])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h3w1")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id4(self):
        neighbors_ids_correct = set(["h1w1", "h2w2", "h1w3",])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h1w2")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id5(self):
        neighbors_ids_correct = set(["h2w1", "h1w2", "h2w3", "h3w2"])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h2w2")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id6(self):
        neighbors_ids_correct = set(["h3w1", "h2w2", "h3w3",])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h3w2")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id7(self):
        neighbors_ids_correct = set(["h1w2", "h2w3",])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h1w3")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id8(self):
        neighbors_ids_correct = set(["h1w3", "h2w2", "h3w3"])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h2w3")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)
    def test_get_neighbors_squares_ids__id9(self):
        neighbors_ids_correct = set(["h3w2", "h2w3",])
        neighbors_ids_test = self.map3x3.get_square_neighbors_ids("h3w3")
        self.assertEqual(neighbors_ids_test, neighbors_ids_correct)


if __name__=="__main__":
    unittest.main()

