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
SIZE = 50
x_vel = 0
y_vel = 0
x = 240
y = 240
speed = 10
s_width = 750
s_height = 750
rand_x = round(random.randrange(0, s_width - SIZE) / 10) * 10
rand_y = round(random.randrange(0, s_height - SIZE) / 10) * 10
score = 0
print(rand_x)
print(rand_y)


# Initialization
pygame.init()
screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
clock.tick(30)

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)##

# Functions
def message(msg, colour, pos_x, pos_y):
    mesg = font_style.render(msg, True, colour)
    screen.blit(mesg, [pos_x, pos_y])


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


    if x <= 0 or x >= s_width or y <= 0 or y >= s_height:
        run = False
    
    if x == rand_x and y == rand_y:
        print("Yummy")
        score = int(score)
        score += 1
        print(score)
        rand_x = round(random.randrange(0, s_width - SIZE) / 10) * 10
        rand_y = round(random.randrange(0, s_height - SIZE) / 10) * 10
 
    x += x_vel
    y += y_vel
    screen.fill((GRASS_GREEN))
    
    pygame.draw.rect(screen, (RED), (rand_x, rand_y, SIZE, SIZE))

    message('Score: ' + str(score), WHITE, 5, 0)
    pygame.draw.rect(screen, (TEAL), (x, y, SIZE, SIZE))
    pygame.display.update() 
    
    clock.tick(speed * 2)

message('You Lost', RED, 500, 250)
pygame.display.update()
time.sleep(1)
pygame.quit()