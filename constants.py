import pygame
import tomli

# get config.toml values if exists
try:
    with open('config.toml', 'rb') as f:
        config = tomli.load(f)
    MAX_LEVELS = config['game']['MAX_LEVELS']

    # Screen constants
    WIDTH = config['screen']['WIDTH']
    HEIGHT = config['screen']['HEIGHT']

    # Bird constants
    MIN_VSPEED = config['bird']['MIN_VSPEED']
    MAX_VSPEED = config['bird']['MAX_VSPEED']
    JUMP_BOOST = config['bird']['JUMP_BOOST']
    BIRD_MIN_ANGLE = config['bird']['BIRD_MIN_ANGLE']
    BIRD_MAX_ANGLE = config['bird']['BIRD_MAX_ANGLE']
    BIRD_LIVES = config['bird']['BIRD_LIVES']

    # Pipe constants
    PIPE_SPEED = config['pipe']['PIPE_SPEED']
    PIPE_WIDTH = config['pipe']['PIPE_WIDTH']
    
except FileNotFoundError:
    MAX_LEVELS = 9

    # Screen constants
    WIDTH = 800
    HEIGHT = 600

    # Bird constants
    MIN_VSPEED = 0
    MAX_VSPEED = 7.5
    JUMP_BOOST = 15
    BIRD_MIN_ANGLE = -15
    BIRD_MAX_ANGLE = 45
    BIRD_LIVES = 3

    # Pipe constants
    PIPE_SPEED = 7.5
    PIPE_WIDTH = 100

# Unable to put in toml
BGCOLOR = (200, 200, 200)
PLAY_BUTTON_HPOS = WIDTH/2.5
PLAY_BUTTON_VPOS = HEIGHT/2.5
PLAY_BUTTON_HSIZE = WIDTH/5
PLAY_BUTTON_VSIZE = HEIGHT/5

ALT_BUTTON_HPOS = WIDTH/2.5
ALT_BUTTON_VPOS = HEIGHT/1.5
ALT_BUTTON_HSIZE = WIDTH/5
ALT_BUTTON_VSIZE = HEIGHT/5

PIPE_COLOR = (0, 180, 0)
PIPE_WIDTH_RANGE = (50, 400)
PIPE_GAP_RANGE = (200, 400)

BIRD_HIT_GROUND = pygame.event.custom_type()
BIRD_HIT_PIPE = pygame.event.custom_type()
BIRD_CLEARED_PIPE = pygame.event.custom_type()
GAME_OVER = pygame.event.custom_type()
