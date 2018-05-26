import random


class Board:
    """
    Class for building a board
    """
    def __init__(self):
        self.data = [[' ' for x in range(3)] for y in range(3)]
        self.last_turn_char = None
        self.last_turn_pos = None

    def has_winner(self):
        """
        Function to determine a winner
        """
        if not self.last_turn_char:
            return False
        d = self.data
        x = self.last_turn_pos[0]
        y = self.last_turn_pos[1]

        if d[0][x] == d[1][x] == d[2][x]:
            return True
        if d[y][0] == d[y][1] == d[y][2]:
            return True
        if x == y and d[0][0] == d[1][1] == d[2][2]:
            return True
        if x + y == 2 and d[0][2] == d[1][1] == d[2][0]:
            return True
        return False

    def get_winner(self):
        """
        Returns determined winner
        """
        if self.has_winner():
            return self.last_turn_char

    def turn(self, char, pos):
        self.data[pos[1]][pos[0]] = char
        self.last_turn_char = char
        self.last_turn_pos = pos

    def free_positions(self):
        """
        Returns ' ' if position is empty
        """
        free_positions = set()
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] == ' ':
                    free_positions.add((x, y))
        return free_positions

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.data)
