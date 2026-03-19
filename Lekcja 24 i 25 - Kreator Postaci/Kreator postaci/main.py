import os
os.chdir(os.path.dirname(__file__))
import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background_img = pygame.image.load("images/background.png")
base_img = pygame.image.load("images/base.png") # !!!!!
clock = pygame.time.Clock()

game_status = True
while game_status:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game_status = False

    screen.blit(background_img, (0,0))
    screen.blit(base_img, (270, 130)) # !!!
    pygame.display.flip() # .update()

    clock.tick(60)
    pass
pygame.quit()
quit()
