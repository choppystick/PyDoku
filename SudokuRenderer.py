from constants import *


class SudokuRenderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.small_font = pygame.font.Font(None, 30)

    def draw_board(self, board, selected_cell):
        self.screen.fill(WHITE)
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(self.screen, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
                if board.board[i][j] != 0:
                    color = BLACK if board.original_board[i][j] != 0 else LIGHT_BLUE
                    text = self.font.render(str(board.board[i][j]), True, color)
                    self.screen.blit(text, (j * CELL_SIZE + 15, i * CELL_SIZE + 10))

        for i in range(0, WIDTH, 3 * CELL_SIZE):
            pygame.draw.line(self.screen, BLACK, (i, 0), (i, HEIGHT - 60), 3)
        for i in range(0, HEIGHT - 60, 3 * CELL_SIZE):
            pygame.draw.line(self.screen, BLACK, (0, i), (WIDTH, i), 3)

        if selected_cell:
            pygame.draw.rect(self.screen, RED,
                             (selected_cell[1] * CELL_SIZE, selected_cell[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)

    def draw_timer(self, time_string, is_paused):
        pygame.draw.rect(self.screen, WHITE, (0, HEIGHT - 60, WIDTH, 60))
        text = self.font.render(f"Time: {time_string}", True, BLACK)
        self.screen.blit(text, (10, HEIGHT - 50))

        pause_text = "Resume" if is_paused else "Pause"
        pause_button = pygame.Rect(WIDTH - 100, HEIGHT - 50, 90, 40)
        pygame.draw.rect(self.screen, LIGHT_BLUE, pause_button)
        pause_text_surf = self.small_font.render(pause_text, True, BLACK)
        self.screen.blit(pause_text_surf, (pause_button.x + 10, pause_button.y + 10))

    @staticmethod
    def update_display():
        pygame.display.flip()
