import random
import requests
import re
import json


class SudokuBoard:
    def __init__(self, board=None):
        if board:
            self.board = board
            self.original_board = [row[:] for row in board]
        else:
            self.board = [[0 for _ in range(9)] for _ in range(9)]
            self.original_board = [[0 for _ in range(9)] for _ in range(9)]

    def generate(self):
        self.solve()
        self._remove_numbers()
        self.original_board = [row[:] for row in self.board]

    def solve(self, i=0, j=0):
        if i == 9:
            i, j = 0, j + 1
            if j == 9:
                return True

        if self.board[i][j] != 0:
            return self.solve(i + 1, j)

        for num in random.sample(range(1, 10), 9):
            if self._is_valid(num, (i, j)):
                self.board[i][j] = num
                if self.solve(i + 1, j):
                    return True
                self.board[i][j] = 0

        return False

    def _is_valid(self, num, pos):
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        box_x, box_y = pos[1] // 3, pos[0] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def _remove_numbers(self):
        for _ in range(40):  # Adjust this number to change difficulty
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            self.board[row][col] = 0

    def clear_user_inputs(self):
        self.board = [row[:] for row in self.original_board]

    def get_hint(self, row, col):
        if self.original_board[row][col] == 0:
            for num in range(1, 10):
                if self._is_valid(num, (row, col)):
                    return num
        return None

    @staticmethod
    def get_nyt_board(difficulty):
        url = f"https://www.nytimes.com/puzzles/sudoku/{difficulty}"
        if difficulty not in ["easy", "medium", "hard"]:
            return None

        try:
            response = requests.get(url)
            if response.status_code == 200:
                pattern = (r'<script type="text\/javascript">window\.gameData = (.+)<\/script><\/div><div '
                           r'id="portal-editorial-content">')
                match = re.search(pattern, response.text)

                if match:
                    data = json.loads(match.group(1))

                    puzzle = data[difficulty]['puzzle_data']['puzzle']
                    board = [puzzle[i:i + 9] for i in range(0, len(puzzle), 9)]

                    return SudokuBoard(board)

            else:
                print("Failed to fetch NYT puzzle")
                return None

        except Exception as e:
            print(f"Error fetching NYT puzzle: {e}")
            return None
