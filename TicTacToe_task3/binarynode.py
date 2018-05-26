import copy, random
from board import Board


class BinaryNode:
    def __init__(self, parent=None, left=None, right=None, board=Board()):
        self.parent = parent
        self.children = {}  # it will contains from 0 to 2 children
        self.board = board
        self.score = 0

    def add_score(self, value):
        self.score += value
        if self.parent:
            self.parent.add_score(value)

    def __str__(self):
        return str(self.score) + '\n' + str(self.board)


def build_tree_recursively(parent, is_nought=True):
    """
    Function for bulding a tree recursively
    """
    winner = parent.board.get_winner()
    if winner == 'X':
        parent.add_score(1)
    elif winner == '0':
        parent.add_score(-1)
    else:
        char = '0' if is_nought else 'X'
        free_positions = parent.board.free_positions()
        random_free_positions = random.sample(free_positions, min(2, len(free_positions)))
        for i in range(len(random_free_positions)):
            child = BinaryNode(parent)
            child.board = copy.deepcopy(parent.board)
            child.board.turn(char, random_free_positions[i])
            parent.children[random_free_positions[i]] = child
            build_tree_recursively(child, not is_nought)


def test():
    node = BinaryNode()
    build_tree_recursively(node)
    while node:
        print('---')
        print(node)
        node = node.left
