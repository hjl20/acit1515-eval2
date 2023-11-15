import pygame
import random

from constants import BIRD_CLEARED_PIPE, HEIGHT, PIPE_SPEED, PIPE_WIDTH, PIPE_WIDTH_RANGE


class Pipe(pygame.sprite.Sprite):
    def __init__(self, position=None, width=None, height=None, inverted=False):
        super().__init__()
        if not width or not height:
            width = PIPE_WIDTH
            height = random.triangular(*PIPE_WIDTH_RANGE)
        self.image = pygame.transform.scale(pygame.image.load("images/pipe.png"), (int(width), int(height))).convert_alpha()
        
        # converts bool string to boolean
        inverted = inverted == 'True' or inverted == True
        
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT
        if inverted:
            self.rect.top = 0
            self.image = pygame.transform.rotate(self.image, 180)
            
        self.rect.left = int(position)

    def update(self):
        self.rect.x -= PIPE_SPEED
        if self.rect.right < 0:
            self.kill()
            pygame.event.post(pygame.event.Event(BIRD_CLEARED_PIPE))
