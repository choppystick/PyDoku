from SudokuBoard import *
from Timer import *
from constants import *


class SudokuGame:
    def __init__(self):
        self.board = None
        self.selected_cell = None
        self.timer = Timer()

    def start_new_game(self, nyt=False, difficulty='easy'):
        if nyt:
            self.board = SudokuBoard.get_nyt_board(difficulty)
            if not self.board:
                print(f"Failed to get NYT {difficulty} puzzle. Using generated puzzle instead.")
                self.board = SudokuBoard()
                self.board.generate()
        else:
            self.board = SudokuBoard()
            self.board.generate()
        self.timer.reset()

    def select_cell(self, pos):
        x, y = pos
        self.selected_cell = (y // CELL_SIZE, x // CELL_SIZE)

    def input_number(self, number):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.board.original_board[row][col] == 0:  # Only allow input for empty cells
                self.board.board[row][col] = number

    def delete_input(self):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.board.original_board[row][col] == 0:  # Only allow deletion for user inputs
                self.board.board[row][col] = 0

    def clear_board(self):
        self.board.clear_user_inputs()

    def get_hint(self):
        if self.selected_cell:
            row, col = self.selected_cell
            return self.board.get_hint(row, col)
        return None

    def is_completed(self):
        for row in self.board.board:
            if 0 in row:
                return False
        return True

    def toggle_pause(self):
        if self.timer.running:
            self.timer.pause()
        else:
            self.timer.resume()
