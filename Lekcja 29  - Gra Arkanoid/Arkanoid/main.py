import pygame
#      plik             klasa
from platforma import Platforma #!!!!!!!!!!
pygame.init()

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

ekran = pygame.display.set_mode((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('images/background.png')


platforma = Platforma() #!!!!!!

status_gry = True
while status_gry:
    zdarzenia = pygame.event.get()
    for z in zdarzenia:
        if z.type == pygame.QUIT:
            status_gry = False
        # wykrywamy tylko moment wciśnięcia
        elif z.type == pygame.KEYDOWN:
            if z.key == pygame.K_ESCAPE:
                status_gry = False

    klawisze = pygame.key.get_pressed()
    if klawisze[pygame.K_a]:# w lewo (x maleje)
        platforma.ruszaj_platforma(-1)
    if klawisze[pygame.K_d]:# w prawo (x rośnie)
        platforma.ruszaj_platforma(+1)

    ekran.blit(obraz_tla, (0,0))
    ekran.blit(platforma.obraz, platforma.rect)

    pygame.display.flip()
    zegar.tick(30)
pygame.quit()
quit()
