# Game options
TITLE = "Jumpy"

WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.1
PLAYER_GRAV = 0.8
PLAYER_JUMP = 23
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0


# Game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
# starting platforms
PLATFORM_LIST = [(0, HEIGHT - 30),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]
# define color
dark_red = (82, 33, 54)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
light_red = (237, 0, 102)
green = (33, 176, 24)
blue = (51, 87, 255)
yellow = (255, 153, 0)
light_yellow = (224, 235, 0)
light_blue = (51, 183, 255)
light_green = (136, 255, 51)