from random import choice
from time import time

from linkedbst import LinkedBST


# list of words from words.txt file
dictionary = []
with open("words.txt", encoding="UTF-8", errors="ignore") as file:
    dictionary += [i.strip() for i in file]

# 10000 randomly chosen words from the dictionary
words_to_be_found = [choice(dictionary) for i in range(10 ** 4)]

# BST created from words from words.txt file
bst = LinkedBST()
for j in set(dictionary):
    bst.add(j)



def dictionary_search():
    """Return time taken to find 10000 words in list, where they stored in
    alphabetical order."""
    start_time = time()
    for i in words_to_be_found:
        # searching words lineary
        dictionary.index(i)
    return time() - start_time


def bst_search():
    """Return time taken to find 10000 words in unbalanced binary tree"""
    start_time = time()
    for i in words_to_be_found:
        # binary search
        bst.find(i)
    return time() - start_time


def balanced_bst_search():
    """Return time taken to find 10000 words in balanced binary tree"""
    # rebalancing the existing binary tree
    bst.rebalance()
    start_time = time()
    for i in words_to_be_found:
        # the Big-O complexity of BSTree.find(item), when binary tree is balanced, is log(n)
        bst.find(i)
    return time() - start_time


def print_results():
    """Return None. Print the results of routines calls to stdout."""
    print("The time taken to search 10000 randomly generated words in: ")
    # print(f"Sorted dictionary, stored in list, using linear search algorithm is: {dictionary_search()} seconds")
    # print(f"Unbalanced BST is: {bst_search()} seconds.")
    print(f"Balanced BST is: {balanced_bst_search()} seconds.")


def main():
    """Main routine"""
    print_results()
    return 0


if __name__ == "__main__":
    main()