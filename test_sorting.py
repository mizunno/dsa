import unittest
from sorting import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_random_list(self):
        sorted_list = bubble_sort([3,1,2,5,9,7,8,6,4])
        self.assertEqual([1,2,3,4,5,6,7,8,9], sorted_list)

    def test_reversed_list(self):
        sorted_list = bubble_sort([9,8,7,6,5,4,3,2,1])
        self.assertEqual([1,2,3,4,5,6,7,8,9], sorted_list)

    def test_empty_list(self):
        sorted_list = bubble_sort([])
        self.assertEqual([], sorted_list)

    def test_one_element_list(self):
        sorted_list = [1]
        self.assertEqual([1], sorted_list)


if __name__ == "__main__":
    unittest.main()