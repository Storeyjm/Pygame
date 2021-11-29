#template
import pygame
# -- Global Constants


# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)


# -- Initialise PyGame
pygame.init()

# Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# Title of new window/screen
pygame.display.set_caption("My window")
# Exit game flag set to false
done = False
# Object sizes
ball_width = 20
padd_width = 15
padd_length = 100
# Object starting positions
ball_x_val = 150
ball_y_val = 200
x_padd = 0
y_padd = 20
# Object directions
ball_x_direction = 2
ball_y_direction = 1
# Scorecards
score = 0
death = 0
# Manages how fast screen refreshes
clock = pygame.time.Clock()

## -- GAME CLASS
#class game()

while not done:

    # -- User input and controls

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True 
        #endif
    # end for
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y_padd >0:
         y_padd = y_padd - 5
    elif keys[pygame.K_DOWN] and y_padd <size[1] - padd_length:
        y_padd = y_padd + 5
    #endif
        

    # -- Game logic goes after this comment

    ball_x_val = ball_x_val + ball_x_direction
    ball_y_val = ball_y_val + ball_y_direction

    if ball_y_val == 0 or ball_y_val > size[1] - ball_width:
        ball_y_direction = (ball_y_direction + 1) * -1
    #endif
    elif ball_x_val > size [0] - ball_width:
        ball_x_direction = (ball_x_direction + 1) * -1
    #endif
    elif ball_x_val < padd_width and ball_y_val > y_padd and ball_y_val < y_padd + padd_length:
        ball_x_direction = (ball_x_direction + 1) * -1
        score = score + 1
    #endif
    elif ball_x_val <= 0:
        ball_x_val = 150
        ball_y_val = 200
        death = death + 1
        score = 0
        
    # -- Screen background is BLACK

    screen.fill (BLACK)

    # -- Draw here

    pygame.draw.rect(screen, RED, (ball_x_val,ball_y_val,ball_width,ball_width))
    pygame.draw.rect(screen, WHITE, (x_padd,y_padd,padd_width,padd_length))
    #def drawScore()
    # -- Flip display to reveal new position of objects 
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#Endwhile - End of game loop

pygame.quit()