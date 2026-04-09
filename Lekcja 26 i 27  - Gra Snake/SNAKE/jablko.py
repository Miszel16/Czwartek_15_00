import pygame
import random

class Jablko(pygame.sprite.Sprite):
    def __init__(self):
        super(Jablko, self).__init__()
        self.obraz = pygame.image.load("images/apple.png")
        # image - oryginalny obraz,
        # surface - powierzchnia do wyświetlenia,
        # rect - współrzędne, wysokosć i szerokość
        #                               X                      Y                  w   h
        self.rect = pygame.Rect(random.randint(0,24)*32, random.randint(0,18)*32, 32, 32)

