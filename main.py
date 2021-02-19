import random


class TicTacToe:
    def __init__(self):
        self.slot_obj = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.input_counter = 0
        self.game_play = True
        self.slot_obj[0] = " "
        self.t = " "
        self.tr = " "
        self.ml = " "
        self.m = " "
        self.mr = " "
        self.dl = " "
        self.d = " "
        self.dr = " "
        self.board = [[f" {self.slot_obj[0]} |", f" {self.slot_obj[1]} |", f" {self.slot_obj[2]} "],
                      [f" {self.slot_obj[3]} |", f" {self.slot_obj[4]} |", f" {self.slot_obj[5]} "],
                      [f" {self.slot_obj[6]} |", f" {self.slot_obj[7]} |", f" {self.slot_obj[8]} "]]

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
        while self.input_counter < 9 and self.game_play:

            print()
            slot = int(input("Please choose a slot to fill in: "))
            print()

            if slot == 1:
                if self.is_filled(self.slot_obj[0]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[0] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 2:
                if self.is_filled(self.slot_obj[1]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[1] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 3:
                if self.is_filled(self.slot_obj[2]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[2] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 4:
                if self.is_filled(self.slot_obj[3]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[3] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 5:
                if self.is_filled(self.slot_obj[4]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[4] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 6:
                if self.is_filled(self.slot_obj[5]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[5] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 7:
                if self.is_filled(self.slot_obj[6]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[6] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 8:
                if self.is_filled(self.slot_obj[7]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[7] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()
            if slot == 9:
                if self.is_filled(self.slot_obj[8]):
                    print("The slot if already filled in. Please choose another slot.")
                else:
                    self.slot_obj[8] = 'x'
                    self.update_board()
                    self.input_counter += 1
                    self.draw_board()

            self.game_play = self.check_win_status()

    def update_board(self):
        self.board = [[f" {self.slot_obj[0]} |", f" {self.slot_obj[1]} |", f" {self.slot_obj[2]} "],
                      [f" {self.slot_obj[3]} |", f" {self.slot_obj[4]} |", f" {self.slot_obj[5]} "],
                      [f" {self.slot_obj[6]} |", f" {self.slot_obj[7]} |", f" {self.slot_obj[8]} "]]

    def check_win_status(self):
        if ((self.slot_obj[0] == self.slot_obj[1] and self.slot_obj[1] == self.slot_obj[2] and self.slot_obj[0] != " ")
           or(self.slot_obj[3] == self.slot_obj[4] and self.slot_obj[4] == self.slot_obj[5] and self.slot_obj[5] != " ")
           or(self.slot_obj[6] == self.slot_obj[7] and self.slot_obj[7] == self.slot_obj[8] and self.slot_obj[7] != " ")
           or(self.slot_obj[0] == self.slot_obj[3] and self.slot_obj[3] == self.slot_obj[6] and self.slot_obj[0] != " ")
           or(self.slot_obj[1] == self.slot_obj[4] and self.slot_obj[4] == self.slot_obj[7] and self.slot_obj[7] != " ")
           or(self.slot_obj[2] == self.slot_obj[5] and self.slot_obj[5] == self.slot_obj[8] and self.slot_obj[8] != " ")
           or(self.slot_obj[0] == self.slot_obj[4] and self.slot_obj[4] == self.slot_obj[8] and self.slot_obj[0] != " ")
        or(self.slot_obj[2] == self.slot_obj[4] and self.slot_obj[4] == self.slot_obj[6] and self.slot_obj[6] != " ")):
            return False

    def opponent_ai(self):
        for i in range(9):
            self.slot_obj[i] = "x"
            if not self.check_win_status():
                self.slot_obj[i] = "o"
                self.input_counter += 1
                break
            elif i == 8:
                self.random_slot_picker()
            self.slot_obj[i] = " "

    # def random_slot_picker(self):
    #     while True:
    #         num = random.randint(0, 8)
    #         if self.slot_obj[num] == " ":
    #             self.slot_obj[num] = "o"
    #             self.input_counter += 1
    #             break



game = TicTacToe()
# game.draw_board()
game.fill_slot()
# game.draw_board()
