import binarynode


class InvalidPossitionExcpetion(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class OutOfRangePositionException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class Game:
    def __init__(self):
        self.winner = None
        self.human_turn = True
        self.root_game_node = binarynode.BinaryNode()
        binarynode.build_tree_recursively(self.root_game_node)

    def play(self, human_first_turn=True):
        """
        Class for playing the game and processing errors
        """
        human_turn = human_first_turn
        game_node = self.root_game_node
        while len(game_node.children) > 0:
            children = game_node.children
            valid_turn_positions = set(children.keys())
            print('Current board:\n', game_node)
            print('Available turns: ', valid_turn_positions)
            if human_turn:
                error = True
                while error:
                    try:
                        pos = tuple(int(i) for i in input('Enter your turn: ').split())
                        if pos[0] < 0 or pos[0] > 2 or pos[1] < 0 or pos[1] > 2:
                            raise OutOfRangePositionException
                        if pos in valid_turn_positions:
                            game_node = children[pos]
                            error = False
                        else:
                            raise InvalidPossitionExcpetion
                    except OutOfRangePositionException:
                        print('Out of range position. Please enter free position from (0,0) to (2,2)')
                    except InvalidPossitionExcpetion:
                        print('Invalid position. Please enter position from available turns set')
                    except ValueError:
                        print('Inval213id position format. Please enter two numbers(1 2)')
            else:
                best_turn_pos = None
                for pos in valid_turn_positions:
                    if not best_turn_pos:
                        best_turn_pos = pos
                        continue
                    if children[pos].score > children[best_turn_pos].score:
                        best_turn_pos = pos

                print('Computer selected pos: ', best_turn_pos)
                game_node = children[best_turn_pos]
            human_turn = not human_turn
        print('Final board:\n', game_node)
        print('Winner: ', game_node.board.get_winner())


if __name__ == "__main__":
    g = Game()
    g.play()
