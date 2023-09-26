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

    def delete(self, key):
        # find node to delete
        node_to_delete = None

        curr = self.root
        while curr != self.NIL:
            if curr.key == key:
                node_to_delete = curr
                break
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right

        # key not in tree
        if not node_to_delete:
            return

        y_original_color = node_to_delete.red

        if node_to_delete.left == self.NIL:
            x = node_to_delete.right
            self.__transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right == self.NIL:
            x = node_to_delete.left
            self.__transplant(node_to_delete, node_to_delete.left)
        else:
            y = node_to_delete.right
            while y.left != self.NIL:
                y = y.left

            y_original_color = y.red
            x = y.right

            if y.parent == node_to_delete:
                x.parent = y
            else:
                # transplant y with y.right (x)
                self.__transplant(y, y.right)
                y.right = node_to_delete.right
                y.right.parent = y

            # transplant node_to_delete with y
            self.__transplant(node_to_delete, y)
            y.left = node_to_delete.left
            y.left.parent = y
            y.red = node_to_delete.red

        if y_original_color is False:
            self.__fix_delete(x)

    def __transplant(self, x, y):
        # Transplant x with y
        if not x.parent:
            self.root = y
        elif self.__is_right_child(x):
            x.parent.right = y
        else:
            x.parent.left = y
        y.parent = x.parent

    def __fix_insert(self, node):
        """
        Balance the tree each time we insert or delete
        a node.
        """
        while node.parent and node.parent.red:
            uncle = None
            if self.__is_left_child(node.parent):
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
                if self.__is_right_child(node) and self.__is_left_child(node.parent):
                    self.__rotate_left(node.parent)
                    node = node.left
                # Case 2 right
                elif self.__is_left_child(node) and self.__is_right_child(node.parent):
                    self.__rotate_right(node.parent)
                    node = node.right
                # Case 3 left
                elif self.__is_left_child(node) and self.__is_left_child(node.parent):
                    self.__rotate_right(node.parent.parent)
                    node.parent.red = False
                    node.parent.right.red = True
                # case 3 right
                else:
                    self.__rotate_left(node.parent.parent)
                    node.parent.red = False
                    node.parent.left.red = True

        self.root.red = False

    def __fix_delete(self, x):
        while x != self.root and x.red is False:
            if self.__is_left_child(x):
                s = x.parent.right
                # Case 1: x's sibling (s) is red
                if s.red is True:
                    s.red = False
                    x.parent.red = True
                    self.__rotate_left(x.parent)
                    s = x.parent.right

                # Case 2: x's sibling (s) is black, and both of s's children
                # are black
                if s.left.red is False and s.right.red is False:
                    s.red = True
                    x = x.parent
                else:
                    # Case 3: x's sibling (s) is black, s's left child is red
                    # and s's right child is black
                    if s.right.red is False:
                        s.left.red = False
                        s.red = True
                        self.__rotate_right(s)
                        s = x.parent.right

                    # Case 4: x's sibling s is black, and s's right child is
                    # red
                    s.red = x.parent.red
                    x.parent.red = False
                    s.right.red = False
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                # Case 1: x's sibling (s) is red
                if s.red is True:
                    s.red = False
                    x.parent.red = True
                    self.__rotate_right(x.parent)
                    s = x.parent.left

                # Case 2: x's sibling (s) is black, and both of s's children
                # are black
                if s.right.red is False and s.left.red is False:
                    s.red = True
                    x = x.parent
                else:
                    # Case 3: x's sibling (s) is black, s's right child is red
                    # and s's left child is black
                    if s.left.red is False:
                        s.right.red = False
                        s.red = True
                        self.__rotate_left(s)
                        s = x.parent.left

                    # Case 4: x's sibling s is black, and s's left child is red
                    s.red = x.parent.red
                    x.parent.red = False
                    s.left.red = False
                    self.__rotate_right(x.parent)
                    x = self.root

        x.red = False

    def __rotate_left(self, pivot):
        # pivot must exist and have a right child
        if pivot == self.NIL or pivot.right == self.NIL:
            return

        y = pivot.right
        pivot.right = y.left

        # set pivot as parent of the left child of y
        if y.left != self.NIL:
            y.left.parent = pivot

        y.parent = pivot.parent

        # if pivot is root, set y as the new root
        if not pivot.parent:
            self.root = y
        # pivot is left child
        elif self.__is_left_child(pivot):
            pivot.parent.left = y
        # pivot is right child
        else:
            pivot.parent.right = y

        # y.parent = pivot.parent
        pivot.parent = y
        # pivot.right = self.NIL
        y.left = pivot

    def __rotate_right(self, pivot):
        # pivot must exist and have a left child
        if pivot == self.NIL or pivot.left == self.NIL:
            return

        y = pivot.left
        pivot.left = y.right

        # set pivot as parent of the right child of y
        if y.right != self.NIL:
            y.right.parent = pivot

        y.parent = pivot.parent
        # if pivot is root, set y as the new root
        if not pivot.parent:
            self.root = y
        # pivot is left child
        elif self.__is_left_child(pivot):
            pivot.parent.left = y
        # pivot is right child
        else:
            pivot.parent.right = y

        pivot.parent = y
        # pivot.left = self.NIL
        y.right = pivot

    def __is_left_child(self, node):
        if node.parent:
            return node.parent.left == node

        return False

    def __is_right_child(self, node):
        if node.parent:
            return node.parent.right == node

        return False
