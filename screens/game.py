
import pygame
from constants import WIDTH, HEIGHT, PLAY_BUTTON_HSIZE, PLAY_BUTTON_VSIZE, BIRD_MAX_ANGLE, BIRD_HIT_GROUND, BIRD_HIT_PIPE, BIRD_CLEARED_PIPE, JUMP_BOOST, WIDTH, HEIGHT, GAME_OVER, MAX_LEVELS

from .base import BaseScreen
from components.bird import Bird
from components.obstacles import Obstacles
from components.textbox import Textbox


class GameScreen(BaseScreen):
    def __init__(self, window, persistent=None):
        super().__init__(window, persistent)
        # persistent["lives"] is an attribute
        self.highscore = persistent["high_score"]
        self.score = 0
        self.bird = Bird()
        self.obstacles = Obstacles(persistent["level"])
        self.lost = False
        self.won = False
        self.timer = 0
        
        self.scorebox = Textbox((75, 25), (255, 255, 255), (0, 0, 0), f"Score: {self.score}", font_size=20)
        self.scorebox.rect.topright = (WIDTH * 16 / 16, 0)
        self.highscorebox = Textbox((110, 25), (255, 255, 255), (0, 0, 0), f"High score: {self.highscore}", font_size=20)
        self.highscorebox.rect.topright = (WIDTH * 14 / 16, 0)
        self.livesbox = Textbox((75, 25), (255, 255, 255), (0, 0, 0), f"Lives: {self.persistent['lives']}", font_size=20)
        self.livesbox.rect.topright = (WIDTH * 11 / 16, 0)
        self.levelbox = Textbox((75, 25), (255, 255, 255), (0, 0, 0), f"Level: {self.persistent['level']}", font_size=20)
        self.levelbox.rect.topleft = (0, 0)
        self.timebox = Textbox((75, 25), (255, 255, 255), (0, 0, 0), f"Time: {self.timer}", font_size=20)
        self.timebox.rect.topleft = (WIDTH * 2 / 16, 0)

        self.lost_message = Textbox((PLAY_BUTTON_HSIZE, PLAY_BUTTON_VSIZE), (255, 0, 0), (0, 0, 0), "FAIL!", font_size=48)
        self.lost_message.rect.center = (WIDTH / 2, HEIGHT / 4)

    def update(self):
        self.bird.update()
        self.obstacles.update()
        
        self.timer += self.clock.get_time() / 1000
        print(self.timer)
        self.timebox.text = f"Time: {int(self.timer)}"

        if pygame.sprite.spritecollide(self.bird, self.obstacles, dokill=False, collided=pygame.sprite.collide_mask):
            pygame.event.post(pygame.event.Event(BIRD_HIT_PIPE))

    def manage_event(self, event):
        super().manage_event(event)

        if not self.lost:            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.bird.vspeed = -JUMP_BOOST
                self.bird.angle = BIRD_MAX_ANGLE

            if event.type in [BIRD_HIT_GROUND, BIRD_HIT_PIPE]:
                pygame.time.set_timer(GAME_OVER, 1000, loops=1)
                self.persistent["lives"] -= 1
                self.livesbox.text = f"Lives: {self.persistent['lives']}"
                self.lost = True

            if event.type == BIRD_CLEARED_PIPE:
                self.score += 1
                self.highscore = max(self.score, self.highscore)
                self.persistent["high_score"] = self.highscore
                self.scorebox.text = f"Score: {self.score}"
                self.highscorebox.text = f"High score: {self.highscore}"
                # check for level win
                try:
                    self.won = self.bird.rect.left >= self.obstacles.last_pipe.rect.right
                except AttributeError:
                    self.won = True

    def draw(self):
        if self.won:
            self.persistent["level"] += 1
            self.next_screen = "game"
            self.running = False
            
        if not self.lost:
            bg_img = pygame.transform.scale(pygame.image.load("images/background.png"), (WIDTH, HEIGHT)).convert_alpha()
            self.window.blit(bg_img, (0,0))
            self.obstacles.draw(self.window)
            
            if self.persistent["level"] > MAX_LEVELS:
                self.levelbox.text = "Endless"    
            self.draw_top_boxes()
            
        elif self.lost and self.persistent["lives"] > 0:
            self.next_screen = "game"
            self.running = False
            
        else:
            self.window.blit(self.livesbox.image, self.livesbox.rect)
            self.window.blit(self.lost_message.image, self.lost_message.rect)
            self.next_screen = "gameover"
            self.running = False

    def draw_top_boxes(self):
            self.window.blit(self.bird.image, self.bird.rect)
            self.window.blit(self.scorebox.image, self.scorebox.rect)
            self.window.blit(self.highscorebox.image, self.highscorebox.rect)
            self.window.blit(self.livesbox.image, self.livesbox.rect)
            self.window.blit(self.levelbox.image, self.levelbox.rect)
            self.window.blit(self.timebox.image, self.timebox.rect)