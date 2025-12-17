import pygame
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


player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
player = load_image(player_path, player_pos)

clock = pygame.time.Clock()
game_status = True

while game_status:
    events = pygame.event.get()

    for event in events:
        #print(event)
        if event.type == pygame.QUIT:
            game_status = False
        pass
    

    pygame.display.update()
    clock.tick(60)
    pass

pygame.quit()
quit()
