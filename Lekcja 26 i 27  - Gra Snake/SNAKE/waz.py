import pygame
#      plik            klasa
from kierunek import Kierunek

class Waz(pygame.sprite.Sprite):
    def __init__(self):
        self.oryginalny_obraz = pygame.image.load("images/head.png")

        # pomocnicza do zmiany kierunku
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)

        # współrzędne i wielkość
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))

        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA # możemy sie obracać tylko o 90stopni

    

    def zmien_kierunek(self, kierunek):
        zmiana_mozliwa = True #bool

        if self.kierunek == Kierunek.GORA and kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if self.kierunek == Kierunek.PRAWO and kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False
        if self.kierunek == Kierunek.DOL and kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if self.kierunek == Kierunek.LEWO and kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        
        if zmiana_mozliwa:
            self.nowy_kierunek = kierunek

    # - przesuwanie 
    # - obrót obrazka
    #-------------------
    # - segmenty węża
    # - kolizje
    def aktualizuj(self):
        self.kierunek = self.nowy_kierunek
        #                                                              0,1,2,3          * -90
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value* -90))

        # przesuwamy węża     x,  y
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, +32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(+32, 0)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)