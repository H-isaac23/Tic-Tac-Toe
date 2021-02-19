import random


class TicTacToe:
    def __init__(self):
        self.slot_obj = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.input_counter = 0
        self.game_play = True
        self.digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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

    def game_start(self):
        while self.input_counter < 9 and self.game_play:

            if self.input_counter%2 == 0:

                print()
                slot = input("Please choose a slot to fill in: ")
                print()

                if slot not in self.digits:
                    print("Please choose from 1-9.")
                elif slot == "1":
                    if self.is_filled(self.slot_obj[0]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[0] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "2":
                    if self.is_filled(self.slot_obj[1]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[1] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "3":
                    if self.is_filled(self.slot_obj[2]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[2] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "4":
                    if self.is_filled(self.slot_obj[3]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[3] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "5":
                    if self.is_filled(self.slot_obj[4]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[4] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "6":
                    if self.is_filled(self.slot_obj[5]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[5] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "7":
                    if self.is_filled(self.slot_obj[6]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[6] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "8":
                    if self.is_filled(self.slot_obj[7]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[7] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
                elif slot == "9":
                    if self.is_filled(self.slot_obj[8]):
                        print("The slot if already filled in. Please choose another slot.")
                    else:
                        self.slot_obj[8] = 'x'
                        self.update_board()
                        self.input_counter += 1
                        self.draw_board()
            else:
                print("Opponent's move:")
                print()
                self.opponent_ai_move()

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
        return True

    def opponent_ai_move(self):
        for i in range(9):
            temp = self.slot_obj[i]
            self.slot_obj[i] = "o"
            if not self.check_win_status() and not self.is_filled(temp):
                self.slot_obj[i] = "o"
                self.input_counter += 1
                self.update_board()
                self.draw_board()
                break

            self.slot_obj[i] = "x"
            if not self.check_win_status() and not self.is_filled(temp):
                self.slot_obj[i] = "o"
                self.input_counter += 1
                self.update_board()
                self.draw_board()
                break
            elif i == 8:
                self.slot_obj[i] = temp
                self.random_slot_picker()
                break

            self.slot_obj[i] = temp

    def random_slot_picker(self):
        while True:
            num = random.randint(0, 8)
            if self.slot_obj[num] == " ":
                self.slot_obj[num] = "o"
                self.input_counter += 1
                self.update_board()
                self.draw_board()
                break


game = TicTacToe()
game.game_start()
