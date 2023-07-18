
class Queue:

    """
    Class that represents a Queue (FIFO) data structure
    """

    def __init__(self):
        self.items = []

    
    def push(self, value):
        """
        Add the given item to the queue
        """

        self.items.insert(0, value)


    def pop(self):
        """
        Pop the first (last on the list) element from the queue and return it
        """

        if self.items:
            return self.items.pop()


    def peek(self):
        """
        Return the first (last on the list) element from the queue but does not delete it
        """

        return self.items[-1]


    def __len__(self):
        return len(self.items)