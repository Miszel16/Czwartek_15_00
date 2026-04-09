# CZĘŚĆ I
# - szkielet aplikacji
# - plik Jablko.py
# ------------------------------------
# CZĘŚĆ II
# - głowa węża
# - sterowanie


import pygame
import random
import time
#     plik         klasa
from jablko import Jablko 
from kierunek import Kierunek # !!!
from waz import Waz # !!!
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
# Tworzymy węża
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
# wywołaj co 200 ms
pygame.time.set_timer(PORUSZ_WEZEM, 200)

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
        
        if z.type == pygame.KEYDOWN:
            if z.key == pygame.K_w:
                waz.zmien_kierunek(Kierunek.GORA)
            if z.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
            if z.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if z.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)

        elif z.type == PORUSZ_WEZEM:
            waz.aktualizuj()

        pass

    ekran.blit(tlo, (0,0))
    
    ekran.blit(waz.obraz, waz.rect) #!!!

    for jablko in jablka_lista:
        ekran.blit(jablko.obraz, jablko.rect)

    pygame.display.flip()
    zegar.tick(30)
    pass

time.sleep(1)
pygame.quit()
quit()