class TicTacToe:
    def __init__(self):
        self.player_inputs = []
        self.input_counter = 0
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
        print()

    def is_filled(self, slot):
        if slot != " ":
            return True
        return False

    def fill_slot(self):
        while self.input_counter < 9:

            print()
            slot = int(input("Please choose a slot to fill in: "))
            print()

            if slot == 1:
                if self.is_filled(self.tl):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.tl = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 2:
                if self.is_filled(self.t):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.t = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 3:
                if self.is_filled(self.tr):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.tr = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 4:
                if self.is_filled(self.ml):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.ml = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 5:
                if self.is_filled(self.m):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.m = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 6:
                if self.is_filled(self.mr):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.mr = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 7:
                if self.is_filled(self.dl):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.dl = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 8:
                if self.is_filled(self.d):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.d = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 9:
                if self.is_filled(self.dr):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.dr = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()

    def update_board(self):
        self.board = [[f" {self.tl} |", f" {self.t} |", f" {self.tr} "],
                      [f" {self.ml} |", f" {self.m} |", f" {self.mr} "],
                      [f" {self.dl} |", f" {self.d} |", f" {self.dr} "]]


game = TicTacToe()
# game.draw_board()
game.fill_slot()
# game.draw_board()

