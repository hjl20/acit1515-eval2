from constants import WIDTH, HEIGHT
import pygame
from screens import WelcomeScreen, GameScreen, GameOverScreen

def main():
    pygame.init()
    pygame.font.init()
    pygame.key.set_repeat(400, 400)
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    
    screens = {
        "welcome": WelcomeScreen,
        "game": GameScreen,
        "gameover": GameOverScreen,
    }
    current_screen = "welcome"
    persistent_data = None

    running = True
    while running:
        screen_class = screens[current_screen]
        screen = screen_class(window, persistent_data)
        screen.run()
        persistent_data = screen.persistent

        if screen.next_screen:
            current_screen = screen.next_screen
        else:
            running = False


if __name__ == "__main__":
    main()
