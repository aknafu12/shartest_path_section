# test case for the ShortestPath class to test the `dijkstra` function:
import unittest
from shortest_path_section import ShortestPath

class TestShortestPath(unittest.TestCase):
    def setUp(self):
        self.graph ={
            'A':{'B':2, 'C':5},
            'B':{'D':3},
            'C':{'D':1, 'E':6},
            'D':{'E':4},
            'E':{}
        }
        self.sp = ShortestPath(self.graph)
        def test_dijkstra(self):
            distances_from_A = self.sp.dijkstra('A')
            expected_distances ={'A':0,'B':2,'C':5,'D':5,'E':9}
            self.assertEqual(distances_from_A, expected_distances)


if __name__ == '__main__':
    unittest.main()

