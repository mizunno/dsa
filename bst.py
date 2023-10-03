
class BST:
    """
    Binary Search Tree (BST) data structure implementation.
    """

    def __init__(self, value):
        """
        Initialize a new instance of the BST class with the given value.
        """

        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Insert a new node with the given value into the BST.
        """

        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)

        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def min(self):
        """
        Return the minimum value in the BST.
        """

        if not self.left:
            return self.value

        return self.left.min()

    def max(self):
        """
        Find the maximum value in the BST.
        """

        if not self.right:
            return self.value

        return self.right.max()

    def delete(self, value):
        """
        Delete a node with the given value from the BST.
        Return the root node of the modified BST.
        """

        if not self.value:
            return

        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)

            return self

        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)

            return self

        else:
            if self.left is None:
                return self.right

            if self.right is None:
                return self.left

            min_greater_node = self.right
            while min_greater_node.left:
                min_greater_node = min_greater_node.left

            self.value = min_greater_node.value
            self.right = self.right.delete(min_greater_node.value)

            return self

    def preorder(self, visited = []):
        """
        Perform a preorder traversal of the BST and return
        the visited nodes as a list.
        """

        if self.value:
            visited.append(self.value)

        if self.left:
            visited = self.left.preorder(visited)

        if self.right:
            visited = self.right.preorder(visited)

        return visited

    def postorder(self, visited = []):
        """
        Perform a postorder traversal of the BST and return
        the visited nodes as a list.
        """

        if self.left:
            visited = self.left.postorder(visited)

        if self.right:
            visited = self.right.postorder(visited)

        if self.value:
            visited.append(self.value)

        return visited

    def inorder(self, visited = []):
        """
        Perform an inorder traversal of the BST and return
        the visited nodes as a list.
        """

        if self.left:
            visited = self.left.inorder(visited)

        if self.value:
            visited.append(self.value)

        if self.right:
            visited = self.right.inorder(visited)

        return visited

    def search(self, value):
        """
        Search a value in the BST and return the node that has
        the given value.
        """
        curr = self
        while curr:
            if curr.value == value:
                return curr
            elif curr.value > value:
                curr = curr.left
            else:
                curr = curr.right

        return None

    def search_range(self, lower, upper):
        """
        Return all the nodes between lower and upper bounds.
        """

        nodes = []

        if self.value >= lower and self.value <= upper:
            nodes.append(self)

        if self.left and self.value > lower:
            nodes.extend(self.left.search_range(lower, upper))

        if self.right and self.value < upper:
            nodes.extend(self.right.search_range(lower, upper))

        return nodes

    def __repr__(self) -> str:
        """
        Return a string representation of the node's value.
        """

        return str(self.value)
