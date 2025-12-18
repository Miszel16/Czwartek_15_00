# Kalkulator RGB
# https://www.w3schools.com/colors/colors_rgb.asp

# GITHUB
# https://github.com/Miszel16/Czwartek_15_00

import pygame
import os
os.chdir(os.path.dirname(__file__))
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pierwsza gra")


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)
    surface = image.convert()
    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)
    rect = surface.get_rect(center = position)
    return [image, surface, rect] #oryginalny, gotowy do wyświetlenia, rozmiar i pozycje

def print_image(img_list: list):
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass

# ----------------------------------------------
def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]
# ----------------------------------------------

def calculate_player_movement(keys):
    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_a]:
        delta_x -= speed
    if keys[pygame.K_d]:
        delta_x += speed
    if keys[pygame.K_s]:
        delta_y += speed

    return [delta_x, delta_y]
    

player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player_path = r"grafiki\player.png" #!!!!!!!!!
player = load_image(player_path, player_pos)

background_color = [178, 221, 242] #!!!!!!!!1

clock = pygame.time.Clock()
game_status = True

while game_status:
    events = pygame.event.get()

    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            game_status = False
        pass

    pressed_keys = pygame.key.get_pressed()
    delta_x, delta_y = calculate_player_movement(pressed_keys)
    player_pos[0] += delta_x
    player_pos[1] += delta_y
    player = set_position_image(player, player_pos)

    screen_surface.fill(background_color) #!!!!!!!!!
    print_image(player)

    pygame.display.update()
    clock.tick(60)
    pass
pygame.quit()
quit()
