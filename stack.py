
class Stack:

    """
    Class that represents a Stack (LIFO) data structure
    """

    def __init__(self):
        self.items = []


    def push(self, item):
        """
        Add the given item to the stack
        """
        self.items.append(item)


    def pop(self):
        """
        Pop the last element from the stack and return it
        """
        if self.items:
            return self.items.pop()


    def peek(self):
        """
        Return the last element from the stack but does not delete it
        """
        if self.items:
            return self.items[-1]


    def __len__(self) -> int:
        """
        Return the number of elements in the stack
        """
        return len(self.items)