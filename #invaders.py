#invaders.py
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

# - Define class Enemy - Which is a sprite
class Enemy(pygame.sprite.Sprite):
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
        self.rect.y = height
        self.rect.x = random.randrange(0, 600)
    #End Procedure
    def update(self):
        if self.rect.y >= 0 and self.rect.y < 475:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = 0
        #endif
    #End Procedure
#End Class

# - Define class Player - Which is a sprite
class Player(pygame.sprite.Sprite):
    # Define constructor for Player
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = 440
        self.rect.x = 320
        self.player_speed = 0
    #End Procedure
    def update(self):
        if self.rect.x < 0 or self.rect.x > 600:
            if self.rect.x > 600:
                self.rect.x = 600
            elif self.rect.x < 0:
                self.rect.x = 0
        else:
            self.rect.x = self.rect.x + self.player_speed
            #End if
        #End if



    #End Procedure
#End Class

class Bullet(pygame.sprite.Sprite):
    # Define constructor for Player
    def __init__(self, color, width, height, speed, x, y):
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with color
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #Set the position of the Sprite
        self.rect = self.image.get_rect()
        self.rect.y = y - height
        self.rect.x = x
    #End Procedure
    def update(self):
        self.rect.y = self.rect.y - self.speed
  
        #endif 
    #End Procedure
#End Class

### -- Game Loop
class Game():
  ## -- GAME LOGIC

    def __init__(self):
        # Create a list of enemies
        self.enemy_group = pygame.sprite.Group()
        self.player_group =pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()

        #Create the enemies
        number_of_enemies = 10
        for x in range (number_of_enemies):
            my_enemy = Enemy(AQUA, 25, 25, 1)
            self.enemy_group.add (my_enemy)
            self.all_sprites_group.add (my_enemy)
        #Next x

        #Create the players
        self.my_player = Player(LILAC, 40, 40)
        self.player_group.add (self.my_player)
        self.all_sprites_group.add (self.my_player)
        #Next x

        #Create the bullets
        self.number_of_bullets = 0

    # End of constructor
        
    def game_run(self):

        self.all_sprites_group.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return True
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.my_player.player_speed = 5


                elif event.key == pygame.K_LEFT and self.my_player.rect.x > 0:
                    self.my_player.player_speed =-5


                elif event.key == pygame.K_UP:
                    self.number_of_bullets = self.number_of_bullets + 1
                    my_bullet = Bullet(WHITE, 5, 10, 2, self.my_player.rect.x + (self.my_player.width*0.5), 480 - self.my_player.height)
                    self.bullet_group.add (my_bullet)
                    self.all_sprites_group.add (my_bullet)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                    self.my_player.player_speed = 0
                


        # -- Screen background is GREY

        screen.fill (GREY)

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

    ret = g.game_run()

    if ret == True:
        done = True
#Endwhile - End of game loop

pygame.quit()