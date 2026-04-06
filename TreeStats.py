class TreeStats:
    def __init__(self, tree):
        self.tree = tree
 
    def getHeight(self):
        if self.tree.root == self.tree.NIL:
            return 0
        stack = []
        depthStack = []
        stack.append(self.tree.root)
        depthStack.append(1)
        maxHeight = 0
        while len(stack) > 0:
            node = stack.pop()
            depth = depthStack.pop()
            if depth > maxHeight:
                maxHeight = depth
            if node.left != self.tree.NIL:
                stack.append(node.left)
                depthStack.append(depth + 1)
            if node.right != self.tree.NIL:
                stack.append(node.right)
                depthStack.append(depth + 1)
        return maxHeight

#    def getBlackHeight(self):
#        count = 0
#        current = self.tree.root
#        while current != self.tree.NIL:
#            if current.color == "BLACK":
#                count = count + 1
#            current = current.left
#        return count
    
    def getBlackHeight(self):
        count = 0
        current = self.tree.root.left 
        while current != self.tree.NIL:
            if current.color == "BLACK":
                count += 1
            current = current.left
        return count


    def getSize(self):
        if self.tree.root == self.tree.NIL:
            return 0
        count = 0
        stack = []
        stack.append(self.tree.root)
        while len(stack) > 0:
            node = stack.pop()
            count = count + 1
            if node.left != self.tree.NIL:
                stack.append(node.left)
            if node.right != self.tree.NIL:
                stack.append(node.right)
        return count