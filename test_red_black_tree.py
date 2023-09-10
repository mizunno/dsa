import unittest
from red_black_tree import RBTree, RBNode


class TestRBT(unittest.TestCase):

    def test_only_root_without_parent(self):
        tree = RBTree(1)

        self.assertEqual(tree.root.key, 1)
        self.assertFalse(tree.root.red)

    def test_insert_empty(self):
        tree = RBTree()

        tree.insert(1)

        self.assertEqual(tree.root.key, 1)
        self.assertFalse(tree.root.red)

    def test_insert_node_on_left(self):
        tree = RBTree(1)

        self.assertEqual(tree.root.key, 1)

        tree.insert(0)

        # Check node keys
        self.assertEqual(tree.root.key, 1)
        self.assertEqual(tree.root.left.key, 0)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)

    def test_insert_node_on_right(self):
        tree = RBTree(1)

        self.assertEqual(tree.root.key, 1)

        tree.insert(2)

        # Check node keys
        self.assertEqual(tree.root.key, 1)
        self.assertEqual(tree.root.right.key, 2)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.right.red)

    def test_insert_duplicate(self):
        tree = RBTree(1)

        self.assertEqual(tree.root.key, 1)

        # Insert duplicate value
        tree.insert(1)

        # Check node keys
        self.assertEqual(tree.root.key, 1)
        self.assertEqual(tree.root.left, tree.NIL)
        self.assertEqual(tree.root.right, tree.NIL)

    def test_insert_case_1_left(self):
        tree = RBTree()

        tree.insert(3)
        tree.insert(5)
        tree.insert(1)
        tree.insert(2)

        # Check node keys
        self.assertEqual(tree.root.key, 3)
        self.assertEqual(tree.root.right.key, 5)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.left.right.key, 2)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertFalse(tree.root.right.red)
        self.assertFalse(tree.root.left.red)
        self.assertTrue(tree.root.left.right.red)

    def test_insert_case_1_right(self):
        tree = RBTree()

        tree.insert(3)
        tree.insert(1)
        tree.insert(5)
        tree.insert(4)

        # Check node keys
        self.assertEqual(tree.root.key, 3)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 5)
        self.assertEqual(tree.root.right.left.key, 4)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertFalse(tree.root.left.red)
        self.assertFalse(tree.root.right.red)
        self.assertTrue(tree.root.right.left.red)

    def test_insert_case_2_left(self):
        tree = RBTree()

        tree.insert(3)
        tree.insert(1)
        tree.insert(2)

        # Check node keys
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 3)

        self.assertEqual(tree.root.left.left, tree.NIL)
        self.assertEqual(tree.root.left.right, tree.NIL)
        self.assertEqual(tree.root.right.left, tree.NIL)
        self.assertEqual(tree.root.right.right, tree.NIL)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)
        self.assertTrue(tree.root.right.red)

    def test_insert_case_2_right(self):
        tree = RBTree()

        tree.insert(2)
        tree.insert(3)
        tree.insert(1)

        # Check node keys
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 3)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)
        self.assertTrue(tree.root.right.red)

    def test_insert_case_3_left(self):
        """
        Case 3 is also tested in case 2, but we write a specific test
        """
        tree = RBTree()

        tree.insert(3)
        tree.insert(2)
        tree.insert(1)

        # Check node keys
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 3)

        self.assertEqual(tree.root.left.left, tree.NIL)
        self.assertEqual(tree.root.left.right, tree.NIL)
        self.assertEqual(tree.root.right.left, tree.NIL)
        self.assertEqual(tree.root.right.right, tree.NIL)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)
        self.assertTrue(tree.root.right.red)

    def test_insert_case_3_right(self):
        """
        Case 3 is also tested in case 2, but we write a specific test
        """
        tree = RBTree()

        tree.insert(1)
        tree.insert(2)
        tree.insert(3)

        # Check node keys
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 3)

        self.assertEqual(tree.root.left.left, tree.NIL)
        self.assertEqual(tree.root.left.right, tree.NIL)
        self.assertEqual(tree.root.right.left, tree.NIL)
        self.assertEqual(tree.root.right.right, tree.NIL)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)
        self.assertTrue(tree.root.right.red)

    def test_delete_root(self):
        tree = RBTree()
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)

        tree.delete(2)

        self.assertEqual(tree.root.key, 3)
        self.assertEqual(tree.root.left.key, 1)
        # TODO: check colors

    def __create_tree(self):
        tree = RBTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(2)
        tree.insert(4)
        tree.insert(3)
        tree.insert(15)
        tree.insert(17)
        tree.insert(12)
        tree.insert(13)

        return tree

    def __check_tree(self, tree):
        # check nodes
        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.root.left.key, 3)
        self.assertEqual(tree.root.left.left.key, 2)
        self.assertEqual(tree.root.left.right.key, 4)
        self.assertEqual(tree.root.right.key, 15)
        self.assertEqual(tree.root.right.left.key, 12)
        self.assertEqual(tree.root.right.left.left.key, 10)
        self.assertEqual(tree.root.right.left.right.key, 13)
        self.assertEqual(tree.root.right.right.key, 17)

        # check colors
        self.assertFalse(tree.root.red)
        self.assertFalse(tree.root.left.red)
        self.assertTrue(tree.root.left.left.red)
        self.assertTrue(tree.root.left.right.red)
        self.assertTrue(tree.root.right.red)
        self.assertFalse(tree.root.right.left.red)
        self.assertTrue(tree.root.right.left.left.red)
        self.assertTrue(tree.root.right.left.right.red)
        self.assertFalse(tree.root.right.right.red)

    def test__is_left_child(self):
        tree = RBTree()
        parent = RBNode(1)
        left_child = RBNode(0)
        parent.left = left_child
        left_child.parent = parent

        self.assertTrue(tree._RBTree__is_left_child(left_child))

    def test__is_right_child(self):
        tree = RBTree()
        parent = RBNode(1)
        right_child = RBNode(0)
        parent.right = right_child
        right_child.parent = parent

        self.assertTrue(tree._RBTree__is_right_child(right_child))

    def test__is_not_left_child(self):
        tree = RBTree()
        parent = RBNode(1)
        left_child = RBNode(0)
        parent.right = left_child

        self.assertFalse(tree._RBTree__is_left_child(left_child))

    def test__is_not_right_child(self):
        tree = RBTree()
        parent = RBNode(1)
        right_child = RBNode(0)
        parent.left = right_child

        self.assertFalse(tree._RBTree__is_right_child(right_child))


if __name__ == "__main__":
    unittest.main()
