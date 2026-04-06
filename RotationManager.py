class RotationManager:
    def __init__(self, tree):
        self.tree = tree
 
    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.tree.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.tree.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
 
    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.tree.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.tree.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y