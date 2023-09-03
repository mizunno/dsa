class RBNode:

    """
    Class to represent a Node of a Red-Black Tree.
    """

    def __init__(self, key):
        self.red = False
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __eq__(self, o):
        return self.key == o.key

    def __gt__(self, o):
        return self.key > o.key

    def __repr__(self):
        return f"{self.key} [{'red' if self.red else 'black'}]"


class RBTree:
    """
    Red-Black Tree Properties.
    1. Red/Black property: every node is colored (red or black)
    2. Root property: root node is always black
    3. Leaf property: every leaf (NIL nodes) is black
    4. Red property: if a red node has children, the children are always black
    5. Depth property: for each node, any simple path from this node to any of
    its descendant leaf nodes has the same black-depth (number of black nodes)
    """

    def __init__(self, root_key=None):
        # NIL node for leaves
        self.NIL = RBNode(None)

        # Black - False
        # Red - True
        self.NIL.red = False
        self.NIL.left = None
        self.NIL.right = None

        self.root = self.NIL

        if root_key:
            self.root = RBNode(root_key)
            self.root.left = self.NIL
            self.root.right = self.NIL

    def insert(self, key):
        node = RBNode(key)
        # Insert new node as red
        node.red = True
        node.left = self.NIL
        node.right = self.NIL

        # Find parent
        parent = None
        curr = self.root

        while curr != self.NIL:
            parent = curr

            if node < curr:
                curr = curr.left
            elif node > curr:
                curr = curr.right
            else:
                # Node is already in the tree
                return

        # Tree is empty, new node is the new root
        if not parent:
            self.root = node
            self.root.red = False
            return

        # Set node's parent to the one found
        node.parent = parent

        if node < parent:
            parent.left = node
        elif node > parent:
            parent.right = node

        self.__fix_insert(node)

    def __fix_insert(self, node):
        """
        Method to balance the tree each time we insert or delete
        a node.
        """
        while node.parent and node.parent.red:
            uncle = None
            if node.parent.parent.left == node.parent:
                uncle = node.parent.parent.right
            else:
                uncle = node.parent.parent.left

            # Case 1
            if uncle.red:
                node.parent.parent.red = True
                node.parent.red = False
                uncle.red = False

                node = node.parent.parent
            else:
                # Case 2 left
                if node.parent.right == node and node.parent.parent.left == node.parent:
                    self.__rotate_left(node.parent)
                    node = node.left
                # Case 2 right
                elif node.parent.left == node and node.parent.parent.right == node.parent:
                    self.__rotate_right(node.parent)
                    node = node.right
                # Case 3 left
                elif node.parent.left == node and node.parent.parent.left == node.parent:
                    self.__rotate_right(node.parent.parent)
                    node.parent.red = False
                    node.parent.right.red = True
                # case 3 right
                else:
                    self.__rotate_left(node.parent.parent)
                    node.parent.red = False
                    node.parent.left.red = True

        self.root.red = False

    def __rotate_left(self, pivot):
        # pivot must exist and have a right child
        if pivot == self.NIL or pivot.right == self.NIL:
            return

        y = pivot.right

        # set pivot as parent of the left child of y
        if y.left != self.NIL:
            y.left.parent = pivot

        # if pivot is root, set y as the new root
        if not pivot.parent:
            self.root = y
        # pivot is left child
        elif pivot == pivot.parent.left:
            pivot.parent.left = y
        # pivot is right child
        else:
            pivot.parent.right = y

        y.parent = pivot.parent
        pivot.parent = y
        y.left = pivot

    def __rotate_right(self, pivot):
        # pivot must exist and have a left child
        if pivot == self.NIL or pivot.left == self.NIL:
            return

        y = pivot.left

        # set pivot as parent of the right child of y
        if y.right != self.NIL:
            y.right.parent = pivot

        # if pivot is root, set y as the new root
        if not pivot.parent:
            self.root = y
        # pivot is left child
        elif pivot == pivot.parent.left:
            pivot.parent.left = y
        # pivot is right child
        else:
            pivot.parent.right = y

        y.parent = pivot.parent
        pivot.parent = y
        y.right = pivot

    def delete(self, key):
        pass