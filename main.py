from Node import *
from RotationManager import *
from InsertionFixer import *
from TreeStats import *
from BSTInterface import *
from RedBlackTree import *
from FileLoader import *
from Dictionary import *

def show_menu():
    print("English Dictionary: ")
    print("1. Insert a new word")
    print("2. Look up a word")
    print("3. Show tree info")
    print("4. Exit")

if __name__ == "__main__":
    tree = RedBlackTree()
    loader = FileLoader("dictionary.txt")
    dictionary = Dictionary(tree, loader)

    loaded = dictionary.loadDictionary()
    print("Loaded", loaded, "words.")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            word = input("Enter the word to insert: ")
            success = dictionary.insertWord(word)

            if not success:
                print("ERROR: Word already exists")
            else:
                print("Inserted successfully!")
                stats = dictionary.getStats()
                print("Size:", stats["size"])
                print("Height:", stats["height"])
                print("Black Height:", stats["blackHeight"])

        elif choice == "2":
            word = input("Enter the word to look up: ")
            found = dictionary.lookupWord(word)

            if found:
                print("YES")
            else:
                print("NO")

        elif choice == "3":
            stats = dictionary.getStats()
            print("\nTree Information:")
            print("Size:", stats["size"])
            print("Height:", stats["height"])
            print("Black Height:", stats["blackHeight"])

        elif choice == "4":
            print("Goodbye")
            break

        else:
            print("Invalid choice.")