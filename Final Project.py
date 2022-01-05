# Ben Walz
# Final Project



import pygame
import time
import random

# colours
RED = (255, 8, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (0, 128, 128)
GRASS_GREEN = (126, 200, 80)
# Mechanics
SIZE = 10
x_vel = 0
y_vel = 0
x = 240
y = 240
speed = 10
s_width = 500
s_height = 500
rand_x = round(random.randrange(0, s_width - SIZE) / 10) * 10
rand_y = round(random.randrange(0, s_height - SIZE) / 10) * 10
score = 0


# Initialization
pygame.init()
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
clock.tick(30)
font_style = pygame.font.SysFont(None, 50)


# Functions
def message(msg, colour):
    mesg = font_style.render(msg, True, colour)
    screen.blit(mesg, [s_width/2, s_height/2])


def food():
    pygame.draw.rect(screen, (RED), (rand_x, rand_y, SIZE, SIZE))





# Loop
run = True

while run == True:
    
    pygame.time.delay(10)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_vel = -speed
                y_vel = 0
            elif event.key == pygame.K_RIGHT:
                x_vel = speed
                y_vel = 0
            elif event.key == pygame.K_UP:
                y_vel = -speed
                x_vel = 0
            elif event.key == pygame.K_DOWN:
                y_vel = speed
                x_vel = 0
            if x == rand_x and y == rand_y:
                run = False
    
    if x <= 0 or x >= s_width or y <= 0 or y >= s_height:
        run = False
    if x == rand_x and y == rand_y:
        print("Yummy")
    
    x += x_vel
    y += y_vel
    screen.fill((GRASS_GREEN))
    food()
    pygame.draw.rect(screen, (TEAL), (x, y, SIZE, SIZE))
    pygame.display.update() 
    
    clock.tick(30)

message('You Lost', RED)
pygame.display.update()
time.sleep(1)
pygame.quit()