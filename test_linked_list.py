import unittest
import linked_list


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = linked_list.LinkedList()

    def test_creation(self):
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)

        n1.next = n2
        self.ll.set_head(n1)
        self.assertEqual(self.ll.head, n1)

    def test_iter(self):
        n1 = linked_list.Node(1)
        n2 = linked_list.Node(2)
        n3 = linked_list.Node(3)

        n1.next = n2
        n2.next = n3

        self.ll.set_head(n1)

        for node_ll, node in zip(self.ll, [n1, n2, n3]):
            self.assertEqual(node_ll, node)

    def test_add_to_tail_empty(self):
        n = linked_list.Node("val_n")

        self.ll.add_to_tail(n)

        self.assertEqual(self.ll.head, n)

    def test_add_to_tail_not_empty(self):
        n1 = linked_list.Node("val_n1")

        self.ll.set_head(n1)

        n2 = linked_list.Node("val_n2")
        self.ll.add_to_tail(n2)

        self.assertEqual(self.ll.head, n1)
        self.assertEqual(self.ll.head.next, n2)

    def test_add_to_head_empty(self):
        n = linked_list.Node("val_n")

        self.ll.add_to_head(n)

        self.assertEqual(self.ll.head, n)

    def test_add_to_head_not_empty(self):
        n1 = linked_list.Node("val_n1")

        self.ll.set_head(n1)

        n2 = linked_list.Node("val_n2")
        self.ll.add_to_head(n2)

        self.assertEqual(self.ll.head.next, n1)
        self.assertEqual(self.ll.head, n2)


if __name__ == "__main__":
    unittest.main()
