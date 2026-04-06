class Dictionary:
    def __init__(self, tree, loader):
        self.tree = tree
        self.loader = loader
        
    def loadDictionary(self):
        words = self.loader.loadWords()
        for word in words:
            self.tree.insert(word)
        return len(words)

    def insertWord(self, word):
        word = word.strip().lower()
        if self.tree.search(word):
            return False  # already exists
        self.tree.insert(word)
        self.loader.appendWord(word)
        return True

    def lookupWord(self, word):
        word = word.strip().lower()
        return self.tree.search(word)

    def getStats(self):
        return {
            "size": self.tree.getSize(),
            "height": self.tree.getHeight(),
            "blackHeight": self.tree.getBlackHeight()
        }