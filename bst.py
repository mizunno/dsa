

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



    def preorder(self):
        pass


    def postorder(self):
        pass


    def inorder(self):
        pass


    def __repr__(self) -> str:
        return str(self.value)
