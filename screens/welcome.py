
import pygame
from constants import WIDTH, HEIGHT, PLAY_BUTTON_HPOS, PLAY_BUTTON_VPOS, PLAY_BUTTON_HSIZE, PLAY_BUTTON_VSIZE, ALT_BUTTON_HPOS, ALT_BUTTON_HSIZE, ALT_BUTTON_VPOS, ALT_BUTTON_VSIZE

from .base import BaseScreen, create_text_surface

class WelcomeScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window, persistent)
        
    def manage_event(self, event):
        super().manage_event(event)

        if event.type == pygame.KEYDOWN and event.key in [pygame.K_SPACE, pygame.K_RETURN]:
            self.next_screen = "game"
            self.running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_btn.collidepoint(event.pos):
                self.next_screen = "game"
                self.running = False
            elif self.alt_btn.collidepoint(event.pos):
                self.next_screen = None
                # self.next_screen = "settings"
                self.running = False

    def draw(self):
        bg_img = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT)).convert_alpha()
        self.window.blit(bg_img, (0, 0))
        
        self.window.blit(pygame.image.load("images/logo.png"), (WIDTH/18, HEIGHT/8))

        # Menu buttons
        surf = pygame.Surface((PLAY_BUTTON_HSIZE, PLAY_BUTTON_VSIZE))
        surf.fill((255, 255, 255))
        surf.blit(create_text_surface('PLAY'), (PLAY_BUTTON_HSIZE/6, PLAY_BUTTON_VSIZE/3))
        self.window.blit(surf, (PLAY_BUTTON_HPOS, PLAY_BUTTON_VPOS))
        self.play_btn = pygame.draw.rect(self.window, (0, 0, 0), (PLAY_BUTTON_HPOS, PLAY_BUTTON_VPOS, PLAY_BUTTON_HSIZE, PLAY_BUTTON_VSIZE), 3)

        surf = pygame.Surface((ALT_BUTTON_HSIZE, ALT_BUTTON_VSIZE))
        surf.fill((255, 255, 255))
        surf.blit(create_text_surface('QUIT'), (ALT_BUTTON_HSIZE/6, ALT_BUTTON_VSIZE/3))
        # surf.blit(create_text_surface('SETTINGS', 24), (ALT_BUTTON_HSIZE/8, ALT_BUTTON_VSIZE/2.5))
        self.window.blit(surf, (ALT_BUTTON_HPOS, ALT_BUTTON_VPOS))
        self.alt_btn = pygame.draw.rect(self.window, (0, 0, 0), (ALT_BUTTON_HPOS, ALT_BUTTON_VPOS, ALT_BUTTON_HSIZE, ALT_BUTTON_VSIZE), 3)


        