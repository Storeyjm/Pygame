#Snakes-ladders.py
import pygame
import random
import math

from pygame.display import update
# -- Global Constants


# -- Colours
GREY = (40, 40, 40)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
LILAC = (255, 153, 255)
AQUA = (26, 255, 255)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

#-- Title of new window/screen
pygame.display.set_caption("Invaders")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

## -- CLASSES
class Snakes_Ladders():
    def Snake_Move():
        #move down snake
    #End Procedure
    
    def Ladder_Move():
        #move up ladder
    #End Procedure
#End Class

class Players():
    def Move():
        #move
    #End Procedure
#End Class

class Dice():
    def Roll():
        #roll dice
    #End Function
#End Class

class Board():
    def Create_Board(self,size):
        #create board including how many snakes or ladders the players input
    #End Procedure
#End Class

class Game():
    ## -- GAME LOGIC
    def __init__(self):
        # Create a list of induvidual sprite groups
        self.player_group = pygame.sprite.Group()
        self.snakes_group = pygame.sprite.Group()
        self.ladders_group = pygame.sprite.Group()
        # Create a list of all sprite groups
        self.all_sprites_group = pygame.sprite.Group()

        #Create the Board
        board_length = 10
        board_width = 10
        for x in range(board_length):
            for x in range(board_width):
                


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