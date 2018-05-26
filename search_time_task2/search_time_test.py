import time
import random
from linkedbst import LinkedBST

# Read words from words.txt file and make a list
words = list()
with open("words.txt", "r", encoding="utf-8", errors="ignore") as file:
    for i in file:
        words.append(i.strip())

# Make BST from words
bst = LinkedBST()
for elem in set(words):
    bst.add(elem)


def rand_words():
    """
    Returns 10000 random words from words.txt file
    """
    return [random.choice(words) for word in range(10000)]


def time_rand_words(rand):
    """
    Returns the search time of 10,000 random words in
    an ordered alphabetical dictionary.
    """
    start = time.time()
    [words.index(elem) for elem in rand]
    return time.time() - start


def bst_unbalanced(rand):
    """
    Returns the search time of 10,000 random
    words in the dictionary, which is represented
    as a binary search tree.
    """
    start = time.time()
    [bst.find(elem) for elem in rand]
    return time.time() - start


def bst_balanced(rand):
    """
    Returns the search time of 10,000 random
    words in the dictionary, which is represented
    as a balanced binary search tree.
    """
    bst.rebalance()
    start = time.time()
    [bst.find(elem) for elem in rand]
    return time.time() - start


if __name__ == "__main__":
    print("Please wait...")
    print("Time of 10,000 random words in an ordered "
          "alphabetical dictionary: ",
          time_rand_words(rand_words()))
    print("Time of 10,000 random words in the dictionary,"
          " which is represented as a binary search tree: ",
          bst_unbalanced(rand_words()))
    print("Time of 10,000 random words in the dictionary,"
          "which is represented as a balanced binary search tree: ",
          bst_unbalanced(rand_words()))
