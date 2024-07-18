from constants import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.state = "main"  # Can be "main" or "nyt_difficulty"

    def draw(self):
        self.screen.fill(WHITE)
        if self.state == "main":
            self._draw_main_menu()
        elif self.state == "nyt_difficulty":
            self._draw_nyt_difficulty_menu()
        pygame.display.flip()

    def _draw_main_menu(self):
        title = self.font.render("Sudoku", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        buttons = [
            "Play Game",
            "Play game from NYT",
            "Exit Game"
        ]

        for i, text in enumerate(buttons):
            button_rect = pygame.Rect(WIDTH // 4, 200 + i * 100, WIDTH // 2, 80)
            pygame.draw.rect(self.screen, LIGHT_BLUE, button_rect)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2)
            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)

    def _draw_nyt_difficulty_menu(self):
        title = self.font.render("Choose NYT Puzzle Difficulty", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

        buttons = ["Easy", "Medium", "Hard", "Back"]

        for i, text in enumerate(buttons):
            button_rect = pygame.Rect(WIDTH // 4, 150 + i * 100, WIDTH // 2, 80)
            pygame.draw.rect(self.screen, LIGHT_BLUE, button_rect)
            pygame.draw.rect(self.screen, BLACK, button_rect, 2)
            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=button_rect.center)
            self.screen.blit(text_surface, text_rect)

    def handle_click(self, pos):
        if self.state == "main":
            return self._handle_main_menu_click(pos)
        elif self.state == "nyt_difficulty":
            return self._handle_nyt_difficulty_click(pos)
        return None  # If state is neither "main" nor "nyt_difficulty"

    def _handle_main_menu_click(self, pos):
        buttons = [
            pygame.Rect(WIDTH // 4, 200 + i * 100, WIDTH // 2, 80)
            for i in range(3)
        ]

        for i, button in enumerate(buttons):
            if button.collidepoint(pos):
                if i == 0:
                    return "play"
                elif i == 1:
                    self.state = "nyt_difficulty"
                    return "nyt_menu"
                elif i == 2:
                    return "exit"
        return None  # Click was outside any button

    def _handle_nyt_difficulty_click(self, pos):
        buttons = [
            pygame.Rect(WIDTH // 4, 150 + i * 100, WIDTH // 2, 80)
            for i in range(4)
        ]

        for i, button in enumerate(buttons):
            if button.collidepoint(pos):
                if i == 3:  # "Back" button
                    self.state = "main"
                    return "back_to_main"
                else:
                    difficulty = ["easy", "medium", "hard"][i]
                    self.state = "main"
                    return f"nyt_{difficulty}"
        return None  # Click was outside any button