from Node import *
from RotationManager import *
from InsertionFixer import *
from TreeStats import *
from BSTInterface import *

class RedBlackTree(BSTInterface):
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = "BLACK"
        self.root = self.NIL
        self.rotationManager = RotationManager(self)
        self.insertionFixer = InsertionFixer(self, self.rotationManager)
        self.stats = TreeStats(self)
 
    def search(self, value):
        current = self.root
        while current != self.NIL:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
 
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.parent = None
        new_node.color = "RED"
        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            elif new_node.value > current.value:
                current = current.right
            else:
                return False
        new_node.parent = parent
        if parent is None:
            self.root = new_node
            self.root.color = "BLACK"
            return True
        if new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        if new_node.parent.parent is None:
            return True
        self.insertionFixer.fix(new_node)
        return True
 
    def getHeight(self):
        return self.stats.getHeight()
 
    def getBlackHeight(self):
        return self.stats.getBlackHeight()
 
    def getSize(self):
        return self.stats.getSize()