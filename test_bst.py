import unittest
from bst import BST


class TestBST(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = BST(10)
        return super().setUp()

    def test_insert(self):
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 5)
        self.assertEqual(self.bst.left.left.value, 2)
        self.assertEqual(self.bst.left.right.value, 8)
        self.assertEqual(self.bst.right.value, 15)

    def test_min_max(self):
        self.assertEqual(self.bst.min(), 10)
        self.assertEqual(self.bst.max(), 10)

        self.bst.insert(5)

        self.assertEqual(self.bst.min(), 5)
        self.assertEqual(self.bst.max(), 10)

        self.bst.insert(15)

        self.assertEqual(self.bst.min(), 5)
        self.assertEqual(self.bst.max(), 15)

    def test_delete_leaf_node(self):
        """
            -> 15
        10 
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2
        """
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 5)
        self.assertEqual(self.bst.left.left.value, 2)
        self.assertEqual(self.bst.left.right.value, 8)
        self.assertEqual(self.bst.left.right.left.value, 6)
        self.assertEqual(self.bst.left.right.right.value, 9)
        self.assertEqual(self.bst.right.value, 15)

        self.bst.delete(2)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 5)
        self.assertIsNone(self.bst.left.left)
        self.assertEqual(self.bst.left.right.value, 8)
        self.assertEqual(self.bst.left.right.left.value, 6)
        self.assertEqual(self.bst.left.right.right.value, 9)
        self.assertEqual(self.bst.right.value, 15)

    def test_delete_inner_node_bypass(self):

        """
            -> 15
        10 
                    -> 9
                -> 8
                    -> 6
            -> 5
        """
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 5)
        self.assertEqual(self.bst.left.right.value, 8)
        self.assertEqual(self.bst.left.right.left.value, 6)
        self.assertEqual(self.bst.left.right.right.value, 9)
        self.assertEqual(self.bst.right.value, 15)

        self.bst.delete(5)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 8)
        self.assertEqual(self.bst.left.left.value, 6)
        self.assertEqual(self.bst.left.right.value, 9)
        self.assertEqual(self.bst.right.value, 15)

    def test_delete_inner_node_not_bypass(self):

        """
            -> 15
        10 
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2
        """
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 5)
        self.assertEqual(self.bst.left.left.value, 2)
        self.assertEqual(self.bst.left.right.value, 8)
        self.assertEqual(self.bst.left.right.left.value, 6)
        self.assertEqual(self.bst.left.right.right.value, 9)
        self.assertEqual(self.bst.right.value, 15)

        self.bst.delete(5)

        self.assertEqual(self.bst.value, 10)
        self.assertEqual(self.bst.left.value, 6)
        self.assertEqual(self.bst.left.left.value, 2)
        self.assertEqual(self.bst.left.right.value, 8)
        self.assertIsNone(self.bst.left.right.left)
        self.assertEqual(self.bst.left.right.right.value, 9)
        self.assertEqual(self.bst.right.value, 15)

    def test_preorder(self):

        """
            -> 15
        10 
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        preorder -> [10,5,2,8,6,9,15]
        """

        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertListEqual(self.bst.preorder(), [10,5,2,8,6,9,15])

    def test_postorder(self):
        """
            -> 15
        10 
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        postorder -> [2,6,9,8,5,15,10]
        """

        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertListEqual(self.bst.postorder(), [2,6,9,8,5,15,10])

    def test_inorder(self):
        """
            -> 15
        10 
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        postorder -> [2,5,6,8,9,10,15]
        """

        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertListEqual(self.bst.inorder(), [2,5,6,8,9,10,15])

    def test_search_inner_node(self):
        """
            -> 15
        10
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        """
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst.left.right, self.bst.search(8))

    def test_search_root_node(self):
        """
            -> 15
        10
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        """
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst, self.bst.search(10))

    def test_search_leaf_node(self):
        """
            -> 15
        10
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        """
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertEqual(self.bst.left.right.right, self.bst.search(9))

    def test_search_range(self):
        """
            -> 15
        10
                    -> 9
                -> 8
                    -> 6
            -> 5
                -> 2

        """

        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(2)
        self.bst.insert(8)
        self.bst.insert(6)
        self.bst.insert(9)

        self.assertListEqual([5, 2, 8, 6], [n.value for n in self.bst.search_range(2, 8)])
        self.assertListEqual([5, 8, 6], [n.value for n in self.bst.search_range(3, 8)])
        self.assertListEqual([], [n.value for n in self.bst.search_range(16, 19)])


if __name__ == "__main__":
    unittest.main()
