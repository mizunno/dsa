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


    def preorder(self):
        pass

    def postorder(self):
        pass

    def inorder(self):
        pass

if __name__ == "__main__":
    unittest.main()