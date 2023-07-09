import unittest
import searching


class TestSearching(unittest.TestCase):

    def test_linear_search(self):
        data = [0,1,2,3,4,5,6,7,8,9]

        for target in data:
            self.assertTrue(searching.linear_search(data, target))

    def test_binary_search(self):
        data = [0,1,2,3,4,5,6,7,8,9]

        for target in data:
            self.assertTrue(searching.binary_search(data, target))


if __name__ == "__main__":
    unittest.main()