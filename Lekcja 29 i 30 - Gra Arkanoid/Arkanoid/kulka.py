import pygame
import random

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

# Czym jest wektor?
# - ma kierunek (w którą stonę sie coś porusza)
# - ma długość (czyli jak szybko się coś porusza)
# - zwrot

# "Idź w stornę xx z taką prędkością zz"

vec = pygame.math.Vector2
predkosc = 15

class Kulka(pygame.sprite.Sprite):
    def __init__(self):
        super(Kulka, self).__init__()
        # image, surface, rect
        self.obraz = pygame.image.load("images/ball.png")

        self.zresetuj_pozycje() 

        self.r = 16
        self.przegrana = False
    

    def zresetuj_pozycje(self):
        # startowa pozycja kulki
        self.wspolrzedne = vec(SZEROKOSC_EKRANU/2, WYSOKOSC_EKRANU-140)
        self.rect = self.obraz.get_rect(center=self.wspolrzedne)
        
        self.wektor = vec(0, -predkosc)
        self.kat_nachylenia = random.randrange(-30, 30)

        self.wektor.rotate_ip(self.kat_nachylenia)
        self.przegrana = False


    def aktualizuj(self, platforma):
        self.wspolrzedne += self.wektor
        self.rect.center = self.wspolrzedne

        self.sprawdz_kolizje(platforma) #!!!
    

    def sprawdz_kolizje(self, platforma):
        # krawędzie ekranu
        if self.rect.left <= 0:
            self.wektor.x *= -1
        if self.rect.right >= SZEROKOSC_EKRANU:
            self.wektor.x *= -1
        
        if self.rect.top <= 0:
            self.wektor.y *= -1
        
        if self.rect.bottom >= WYSOKOSC_EKRANU:
            self.przegrana = True
        
        if self.rect.colliderect(platforma.rect):
            self.wektor.y *= -1
            self.wektor.x += platforma.porusza_sie*5
        
            if self.wektor.x < -predkosc:
                self.wektor.x = -predkosc
            if self.wektor.x > predkosc:
                self.wektor.x = predkosc

