import pygame
import random
import os
from settings import *


# set up assets folder

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "image")
class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        # this line is required to properly create the sprite
        pygame.sprite.Sprite.__init__(self)
        # create a plain rectangle for the sprite image
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(black)
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # center the sprite on the screen
        self.rect.center = (display_width / 2, display_height / 2)
        self.y_speed = 5


    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > display_height - 200:
            self.y_speed -= 5
        if self.rect.top < 200:
            self.y_speed += 5
        if self.rect.left > display_width:
            self.rect.right = 0
# initialize pygame and create window



player = Player()
all_sprites.add(player) #add in the player group
#game loop

running = True

while running:




    # update


    #draw render
    screen.fill(blue) #background color
    all_sprites.draw(screen)
    #after drawing everything, flip the display
    pygame.display.flip()
    # pygame.display.update()


pygame.quit()
