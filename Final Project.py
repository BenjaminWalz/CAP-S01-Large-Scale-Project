# Ben Walz
# Final Project



import pygame


# colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEAL = (0, 128, 128)
GRASS_GREEN = (126, 200, 80)
# Mechanics
WIDTH = 20
HEIGHT = 20
x_vel = 0
y_vel = 0
x = 240
y = 240
speed = 10


# Functions








# Initialization
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
clock.tick(30)


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

        
    x += x_vel
    y += y_vel
         
    screen.fill((GRASS_GREEN))
    pygame.draw.rect(screen, (TEAL), (x, y, WIDTH, HEIGHT))
    pygame.display.update() 
    
    clock.tick(30)
pygame.quit()