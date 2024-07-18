from Menu import *
from SudokuGame import *
from SudokuRenderer import *
from constants import *


class GameController:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku")
        self.game = SudokuGame()
        self.renderer = SudokuRenderer(self.screen)
        self.menu = Menu(self.screen)
        self.state = "menu"

    def run(self):
        running = True
        while running:
            if self.state == "menu":
                self.menu.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        action = self.menu.handle_click(event.pos)
                        if action == "play":
                            self.game.start_new_game()
                            self.state = "play"
                        elif action == "nyt_menu":
                            pass  # Stay in menu state, but show NYT difficulty submenu
                        elif action and action.startswith("nyt_"):
                            difficulty = action.split("_")[1]
                            self.game.start_new_game(nyt=True, difficulty=difficulty)
                            self.state = "play"
                        elif action == "exit":
                            running = False
                        elif action == "back_to_main":
                            pass

            elif self.state == "play":
                self.game.timer.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = event.pos
                        if y < HEIGHT - 60:  # Click on the board
                            self.game.select_cell(event.pos)
                        else:  # Click on the timer area
                            if WIDTH - 100 <= x <= WIDTH and HEIGHT - 50 <= y <= HEIGHT - 10:
                                self.game.toggle_pause()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.state = "menu"
                        elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                           pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                            self.game.input_number(int(pygame.key.name(event.key)))
                        elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                            self.game.delete_input()
                        elif event.key == pygame.K_c:
                            self.game.clear_board()
                        elif event.key == pygame.K_h:
                            hint = self.game.get_hint()
                            if hint:
                                print(f"Hint: {hint}")  # You can display this on the screen instead

                self.renderer.draw_board(self.game.board, self.game.selected_cell)
                self.renderer.draw_timer(self.game.timer.get_time_string(), not self.game.timer.running)
                self.renderer.update_display()

                if self.game.is_completed():
                    print("Congratulations! You've solved the puzzle!")
                    self.state = "menu"

        pygame.quit()


if __name__ == "__main__":
    controller = GameController()
    controller.run()
