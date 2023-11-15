import pygame

from constants import BIRD_MIN_ANGLE, MIN_VSPEED, MAX_VSPEED, HEIGHT, BIRD_HIT_GROUND


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        self.original_image = pygame.transform.scale(pygame.image.load("images/bird.png"), (100, 100)).convert_alpha()
        self.image = self.original_image
        self.angle = BIRD_MIN_ANGLE
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottom = 100
        self.rect.left = 50
        self.vspeed = MIN_VSPEED

    def update(self):
        self.vspeed = min(MAX_VSPEED, self.vspeed + 1)
        self.rect.y = self.rect.y + self.vspeed

        # image rotation adapted from https://gamedev.stackexchange.com/questions/126353/how-to-rotate-an-image-in-pygame-without-losing-quality-or-increasing-size-or-mo
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle = max(BIRD_MIN_ANGLE, self.angle - 2) 

        if self.rect.bottom > HEIGHT:
            pygame.event.post(pygame.event.Event(BIRD_HIT_GROUND))


        if self.rect.top < 0:
            self.rect.top = 0
            self.vspeed = MIN_VSPEED
