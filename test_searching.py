import unittest
import searching


class TestSearching(unittest.TestCase):

    def test_linear_search(self):
        l = [0,1,2,3,4,5,6,7,8,9]

        for t in l:
            self.assertTrue(searching.linear_search(l, t))

    def test_binary_search(self):
        l = [0,1,2,3,4,5,6,7,8,9]

        for t in l:
            self.assertTrue(searching.binary_search(l, t))


if __name__ == "__main__":
    unittest.main()