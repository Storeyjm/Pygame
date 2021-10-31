

import pygame
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
pygame.display.set_caption("My window")
# -- Exit game flag set to false
done = False

sun_x = 40

sun_y = 100

x_speed = sun_x = sun_x + 1

y_speed = sun_y = sun_y + 1
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop

while not done:

    # -- User input and controls

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        #Endif

    #Next event

    # -- Game logic goes after this comment

    

    x_speed
    
    if direction == "up":
        sun_y = sun_y - 1
    elif direction == "down":
        sun_y = sun_y + 1
    #endif

    while sun_y == 480 - 40:
        direction = "up"
    
    while sun_y == 40:
        direction = "down"

    while sun_x == 640 + 40:
        sun_x = -40

    while sun_x == -40:
        direction = "up"
    # -- Screen background is BLACK

    screen.fill (BLACK)

    # -- Draw here

    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)

    # -- Flip display to reveal new position of objects 
    pygame.display.flip()

    # - The clock ticks over
    clock.tick(60)

#Endwhile - End of game loop

pygame.quit()