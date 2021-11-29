#snow.py
import pygame
import random
import math

from pygame.display import update
# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

#-- Title of new window/screen
pygame.display.set_caption("Snow")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# - Define class Snow - Which is a sprite
class Snow(pygame.sprite.Sprite):
    # Define constructor for Snow
    def __init__(self, color, width, height, speed):
        # Set speed of the sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        #Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(0, 400)
        self.rect.x = random.randrange(0, 600)
    #End Procedure
    def update(self):
        if self.rect.y >= 0 and self.rect.y < 475:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = 0
        #End While
        # 
    #End Procedure
#End Class



### -- Game Loop
class Game():
  ## -- GAME LOGIC

    def __init__(self):
        # Create a list of Snow blocks
        self.snow_group = pygame.sprite.Group()
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()

        #Create the snowflakes
        number_of_flakes = 50
        for x in range (number_of_flakes):
            my_snow = Snow(WHITE, 5, 5, 4)
            self.snow_group.add (my_snow)
            self.all_sprites_group.add (my_snow)
        #Next x
    # end of constructore

    def game_run(self):

        self.all_sprites_group.update()
        
        # -- Screen background is BLACK

        screen.fill (BLACK)

        # -- Draw here
        self.all_sprites_group.draw (screen)
        # -- Flip display to reveal new position of objects 
        pygame.display.flip()

        # - The clock ticks over
        clock.tick(60)

    # end of game run function
#End Class

g = Game()
while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True
        #Endif
    #Next event

    g.game_run()
#Endwhile - End of game loop

pygame.quit()