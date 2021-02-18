class TicTacToe:
    def __init__(self):
        self.player_inputs = []
        self.tl = " "
        self.t = " "
        self.tr = " "
        self.ml = " "
        self.m = " "
        self.mr = " "
        self.dl = " "
        self.d = " "
        self.dr = " "
        self.board = [[f" {self.tl} |", f" {self.t} |", f" {self.tr} "],
                      [f" {self.ml} |", f" {self.m} |", f" {self.mr} "],
                      [f" {self.dl} |", f" {self.d} |", f" {self.dr} "]]

    def draw_board(self):
        for i in range(3):
            for col in self.board[i]:
                print(col, end="")
            print()
            if i < 2:
                print(11 * '-')

    def is_filled(self, slot):
        if slot != " ":
            print("The slot if already filled in.")
            return False
        return True



game = TicTacToe()
game.draw_board()
# game.is_filled(game.tl)
