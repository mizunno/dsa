import unittest
import sorting


class TestSorting(unittest.TestCase):
    def random_list_sorting_test(self, sorting_func, case):
        with self.subTest(case=case + ' - Random List'):
            input_list = [3, 1, 2, 5, 9, 7, 8, 6, 4]
            expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            sorted_list = sorting_func(input_list)
            self.assertListEqual(expected_list, sorted_list)

            input_list = [1, 1, 2, 6, 4, 7, 8, 6, 2]
            expected_list = [1, 1, 2, 2, 4, 6, 6, 7, 8]
            sorted_list = sorting_func(input_list)
            self.assertListEqual(expected_list, sorted_list)


    def reversed_list_sorting_test(self, sorting_func, case):
        with self.subTest(case=case + ' - Reversed List'):
            input_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
            expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            sorted_list = sorting_func(input_list)
            self.assertListEqual(expected_list, sorted_list)


    def empty_list_sorting_test(self, sorting_func, case):
        with self.subTest(case=case + ' - Empty List'):
            input_list = []
            expected_list = []
            sorted_list = sorting_func(input_list)
            self.assertListEqual(expected_list, sorted_list)


    def one_element_list_sorting_test(self, sorting_func, case):
        with self.subTest(case=case + ' - One Element List'):
            input_list = [1]
            expected_list = [1]
            sorted_list = sorting_func(input_list)
            self.assertListEqual(expected_list, sorted_list)


    def test_sorting_functions(self):
        sorting_funcs = [(name,func) for name, func in sorting.__dict__.items() if callable(func)]
        for func_name, sorting_func in sorting_funcs:
            self.random_list_sorting_test(sorting_func, func_name)
            self.reversed_list_sorting_test(sorting_func, func_name)
            self.empty_list_sorting_test(sorting_func, func_name)
            self.one_element_list_sorting_test(sorting_func, func_name)


if __name__ == "__main__":
    unittest.main()