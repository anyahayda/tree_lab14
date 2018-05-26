import copy, random
from board import Board


class Node:
    def __init__(self, parent=None, board=Board()):
        self.parent = parent
        self.children = {}
        self.board = board
        self.score = 0

    def add_score(self, value):
        self.score += value
        if self.parent:
            self.parent.add_score(value)

    def __str__(self):
        return str(self.score) + '\n' + str(self.board)

    def __getitem__(self, item):
        return self.children[item]


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
        for pos in parent.board.free_positions():
            child = Node(parent)
            child.board = copy.deepcopy(parent.board)
            child.board.turn(char, pos)
            parent.children[pos] = child
            build_tree_recursively(child, not is_nought)


def test():
    node = Node()
    build_tree_recursively(node)
    while node:
        print('---')
        print(node)
        if len(node.children) > 0:
            node = random.choice(list(node.children.values()))
        else:
            node = None
