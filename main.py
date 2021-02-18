class TicTacToe:
    def __init__(self):
        self.board = []
        self.player_inputs = []

    def draw_board(self):
        for i in range(2):
            print(2 * '   |')
            print(2 * '   |')
            print(2 * '   |')
            print(3 * '----')
        print(2 * '   |')
        print(2 * '   |')
        print(2 * '   |')

game = TicTacToe()
game.draw_board()