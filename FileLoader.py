class FileLoader:
    def __init__(self, filename):
        self.filename = filename
 
    def loadWords(self):
        words = []
        try:
            file = open(self.filename, "r")
            lines = file.readlines()
            file.close()
            for line in lines:
                word = line.strip()
                if word != "":
                    words.append(word)
        except FileNotFoundError:
            print("No dictionary file found. Starting with empty dictionary.")
        return words
 
    def appendWord(self, word):
        file = open(self.filename, "a")
        file.write(word + "\n")
        file.close()