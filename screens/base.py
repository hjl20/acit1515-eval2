import pygame
from constants import BIRD_LIVES


class BaseScreen:
    def __init__(self, window, persistent=None):
        if persistent is None:
            self.persistent = {
                "lives": BIRD_LIVES,
                "high_score": 0,
                "level": 1
            }
        else:
            self.persistent = persistent

        if self.persistent["lives"] < 1: 
            self.persistent["lives"] = BIRD_LIVES
            
        self.window = window
        self.next_screen = None
        self.running = False

    def run(self):
        self.clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()
            for event in pygame.event.get():
                self.manage_event(event)

    def draw(self):
        pass

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
            self.next_screen = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.running = False
            self.next_screen = False

def create_text_surface(text, size=40):
    """This function creates a surface and renders the text argument in it"""

    # Get the default font for the system
    default_font = pygame.font.get_default_font()
    font = pygame.font.Font(default_font, size)
    text_surface = font.render(text, True, (0, 0, 0))

    return text_surface