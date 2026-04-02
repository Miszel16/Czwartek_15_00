# - szkielet aplikacji
# - plik Jablko.py

import pygame
import random
import time
#     plik         klasa
from jablko import Jablko # !!!
pygame.init()

SZEROKOSC_EKRANU = 800 # 25 
WYSOKOSC_EKRANU = 608 # 19

# (32 x 32)
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

for i in range(25): # 0,1,2,3,4,5,6,7,8 .... 24  -> 0,32,64,96 ...
    for j in range(19): # 0,1,2,3,4,5,6,7 ... 18 -> 0,32,64,96 ...
        obraz = pygame.image.load("images/background.png")
        # R(0,255)  G(0,255)  B(0,255)  (r,g,b)
        #       (           R                      G                       B           )
        maska = (random.randrange(0,20), random.randrange(0,20), random.randrange(0,20))

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        tlo.blit(obraz, (i*32, j*32))

ekran = pygame.display.set_mode((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
zegar = pygame.time.Clock()
# -----------------------------------------------------------------------------------------------

jablko = Jablko()

jablka_lista = pygame.sprite.Group()
jablka_lista.add(jablko)

# -----------------------------------------------------------------------------------------------
status_gry = True
while status_gry:
    zdarzenia = pygame.event.get() # WSZYTSKIE / lista
    for z in zdarzenia: # z - pojedyncze zdarzenie
        if z.type == pygame.QUIT:
            status_gry = False
        pass

    ekran.blit(tlo, (0,0)) #!!!

    for jablko in jablka_lista:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()
    zegar.tick(30)
    pass

time.sleep(1)
pygame.quit()
quit()