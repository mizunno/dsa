import unittest
import queue_

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = queue_.Queue()
        return super().setUp()
    

    def test_push(self):
        self.assertListEqual(self.queue.items, [])

        self.queue.push(1)
        self.assertListEqual(self.queue.items, [1])

        self.queue.push(2)
        self.assertListEqual(self.queue.items, [2,1])

        self.queue.push(3)
        self.assertListEqual(self.queue.items, [3,2,1])


    def test_pop(self):
        self.assertListEqual(self.queue.items, [])
        self.assertIsNone(self.queue.pop())

        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)

        self.assertListEqual(self.queue.items, [3,2,1])

        self.assertEqual(self.queue.pop(), 1)
        self.assertListEqual(self.queue.items, [3,2])

        self.assertEqual(self.queue.pop(), 2)
        self.assertListEqual(self.queue.items, [3])

        self.assertEqual(self.queue.pop(), 3)
        self.assertListEqual(self.queue.items, [])


    def test_peek(self):
        self.assertListEqual(self.queue.items, [])

        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)
        
        self.assertListEqual(self.queue.items, [3,2,1])

        self.assertEqual(self.queue.peek(), 1)
        self.assertListEqual(self.queue.items, [3,2,1])


    def test_len(self):
        self.assertEqual(len(self.queue), 0)

        self.queue.push(1)
        self.assertEqual(len(self.queue), 1)

        self.queue.push(2)
        self.assertEqual(len(self.queue), 2)

        self.queue.push(3)
        self.assertEqual(len(self.queue), 3)


if __name__ == "__main__":
    unittest.main()