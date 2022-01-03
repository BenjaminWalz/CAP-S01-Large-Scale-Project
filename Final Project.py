# Ben Walz
# Final Project



import pygame


# colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Mechanics
WIDTH = 20
HEIGHT = 20
VEL = 5
x = 50
y = 50


# Functions








# Initialization
pygame.init()
screen = pygame.display.set_mode((500, 500))

run = True

while run == True:

    pygame.time.delay(10)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
    keys = pygame.key.get_pressed()
      

    if keys[pygame.K_LEFT] and x>0:
          x -= VEL
          

    if keys[pygame.K_RIGHT] and x<500-WIDTH:
        x += VEL
         
  
    if keys[pygame.K_UP] and y>0:
        y -= VEL
          
  
    if keys[pygame.K_DOWN] and y<500-HEIGHT:
        # increment in y co-ordinate
        y += VEL
         
              
    screen.fill((BLACK))
      

    pygame.draw.rect(screen, (255, 0, 0), (x, y, WIDTH, HEIGHT))
    
    pygame.display.update() 

pygame.quit()