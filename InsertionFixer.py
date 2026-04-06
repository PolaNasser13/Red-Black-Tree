class InsertionFixer:
    def __init__(self, tree, rotationManager):
        self.tree = tree
        self.rotationManager = rotationManager
 
    def fix(self, z):
        while z.parent != None and z.parent.color == "RED":
            if z.parent == z.parent.parent.left:
                uncle = z.parent.parent.right
                if uncle.color == "RED":
                    z.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotationManager.leftRotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.rotationManager.rightRotate(z.parent.parent)
            else:
                uncle = z.parent.parent.left
                if uncle.color == "RED":
                    z.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    z.parent.parent.color = "RED"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotationManager.rightRotate(z)
                    z.parent.color = "BLACK"
                    z.parent.parent.color = "RED"
                    self.rotationManager.leftRotate(z.parent.parent)
            if z == self.tree.root:
                break
        self.tree.root.color = "BLACK"