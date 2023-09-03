import unittest
from red_black_tree import RBTree


class TestRBT(unittest.TestCase):

    def setUp(self):
        pass

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

        self.assertEqual(tree.root.key, 1)
        self.assertFalse(tree.root.red)
        self.assertEqual(tree.root.left.key, 0)
        self.assertTrue(tree.root.left.red)

    def test_insert_node_on_right(self):
        tree = RBTree(1)

        self.assertEqual(tree.root.key, 1)

        tree.insert(2)

        self.assertEqual(tree.root.key, 1)
        self.assertFalse(tree.root.red)
        self.assertEqual(tree.root.right.key, 2)
        self.assertTrue(tree.root.right.red)

    def test_insert_duplicate(self):
        tree = RBTree(1)

        self.assertEqual(tree.root.key, 1)

        tree.insert(1)

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
        Case 3 is also tested in case 2, but we write
        """
        tree = RBTree()

        tree.insert(3)
        tree.insert(2)
        tree.insert(1)

        # Check node keys
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 3)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)
        self.assertTrue(tree.root.right.red)

    def test_insert_case_3_right(self):
        """
        Case 3 is also tested in case 2, but we write
        """
        tree = RBTree()

        tree.insert(1)
        tree.insert(2)
        tree.insert(3)

        # Check node keys
        self.assertEqual(tree.root.key, 2)
        self.assertEqual(tree.root.left.key, 1)
        self.assertEqual(tree.root.right.key, 3)

        # Check node colors
        self.assertFalse(tree.root.red)
        self.assertTrue(tree.root.left.red)
        self.assertTrue(tree.root.right.red)


if __name__ == "__main__":
    unittest.main()
