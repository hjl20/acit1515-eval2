import pygame
import random
import csv
from .pipe import Pipe
from constants import WIDTH, PIPE_GAP_RANGE, MAX_LEVELS


class Obstacles(pygame.sprite.Group):
    def __init__(self, level=None):
        super().__init__()
        self.level = level
        self.pipenum = 0
        if self.level <= MAX_LEVELS:
            with open(f"levels/{level}.csv") as file:
                reader = csv.DictReader(file)
                self.pipes = [row for row in reader]
        else:
            self.level = None
            self.add(Pipe(WIDTH))

    def update(self, *args, **kwargs):
        if not self.level:    
            if self.rightmost_pipe < WIDTH:
                pos = self.rightmost_pipe + random.randint(*PIPE_GAP_RANGE)
                inverted = False
                if (random.random() < 0.5):
                    inverted = True
                self.add(Pipe(position=pos, inverted=inverted))
        else:
            try:
                pipe = self.pipes[self.pipenum]
                self.add(Pipe(int(pipe['position']), int(pipe['width']), int(pipe['height']), pipe['inverted']))
                self.pipenum += 1
            except IndexError:
                pass
        return super().update(*args, **kwargs)
                

    @property
    def rightmost_pipe(self):
        return max([s.rect.right for s in self.sprites()])
    
    @property
    def last_pipe(self):
        if len(self.sprites()) > 0:
            return self.sprites()[-1]
