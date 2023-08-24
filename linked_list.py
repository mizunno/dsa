
class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, next):
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def set_head(self, head):
        self.head = head

    def __iter__(self):
        curr = self.head

        while curr:
            yield curr
            curr = curr.next

    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return

        curr = self.head

        while curr:
            if curr.next:
                curr = curr.next

            break

        curr.next = node

    def add_to_head(self, node):
        if not self.head:
            self.head = node
            return

        node.set_next(self.head)
        self.head = node

    def __repr__(self):
        return " -> ".join([str(node.value) for node in self])
