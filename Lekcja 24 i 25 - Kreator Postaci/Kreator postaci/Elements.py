import pygame

class Picture():
    def __init__(self, path):
        self.image = pygame.image.load(path).convert_alpha()


class Element():
    def __init__(self, typ):
        # [body1, body2, body3] len() = 3
        #    0      1      2
        self.chosen = 0 
        self.list_img = []

        # start, stop, step
        for i in range(1,4): # 1, 2, 3
            path = f"images/{typ}{i}.png"
            img = Picture(path)
            self.list_img.append(img)
    
    def chooseNext(self):
        self.chosen += 1
        if self.chosen >= len(self.list_img):
            self.chosen = 0
    
    def chosenImage(self):
        return self.list_img[self.chosen].image


class Head(Element):
    def __init__(self):
        super().__init__("head")

# Body
# Eyes
# Weapon
