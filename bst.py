

class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
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
        if not self.left:
            return self.value
        
        return self.left.min()

    def max(self):
        if not self.right:
            return self.value
        
        return self.right.max()

    def delete(self, value):
        pass

    def preorder(self):
        pass

    def postorder(self):
        pass

    def inorder(self):
        pass

    def __repr__(self) -> str:
        pass