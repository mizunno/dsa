import unittest
import stack

class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = stack.Stack()
        return super().setUp()
    
    
    def test_push(self):
        self.stack.push(1)
        self.assertListEqual(self.stack.items, [1])

        self.stack.push(2)
        self.assertListEqual(self.stack.items, [1,2])


    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertListEqual(self.stack.items, [1,2,3])

        self.assertEqual(self.stack.pop(), 3)
        self.assertListEqual(self.stack.items, [1,2])

        self.assertEqual(self.stack.pop(), 2)
        self.assertListEqual(self.stack.items, [1])
        
        self.assertEqual(self.stack.pop(), 1)
        self.assertListEqual(self.stack.items, [])


    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertListEqual(self.stack.items, [1,2])

        self.assertEqual(self.stack.peek(), 2)
        self.assertListEqual(self.stack.items, [1,2])
        

    def test_len(self):
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1)

        self.stack.push(2)
        self.assertEqual(len(self.stack), 2)

        self.stack.push(3)
        self.assertEqual(len(self.stack), 3)

        self.stack.pop()
        self.assertEqual(len(self.stack), 2)

    
    def test_contains(self):
        item = 1
        self.assertFalse(item in self.stack)

        self.stack.push(1)
        self.assertTrue(item in self.stack)


if __name__ == "__main__":
    unittest.main()