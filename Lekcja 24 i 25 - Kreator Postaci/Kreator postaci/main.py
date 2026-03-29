import os
os.chdir(os.path.dirname(__file__))
import pygame
#      nazwa pliku
import Elements #!!!!!!!!!!!
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
background_img = pygame.image.load("images/background.png")
base_img = pygame.image.load("images/base.png")
clock = pygame.time.Clock()

# ---------------- Renderowanie napisu ------------------------
font = pygame.font.SysFont('Comic Sans MS', 30)
def print_text(screen, text, position):
    label = font.render(text, False, (255,255,255)) # Red Green Blue (0-255)
    screen.blit(label, position)
# ---------------------------------------------------------------

# -------- Tworzymy obiekty -------------------------
head = Elements.Head() # [head1.png, head2.png, head3.png], chosen = 0
body = Elements.Body()
eye = Elements.Eye()
weapon = Elements.Weapon()
# ---------------------------------------------------

# -------ZAPISYWANIE---------
save = False
save_text = ""
save_time = 0
# ---------------------------

game_status = True
while game_status:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            game_status = False

        # Q - nakrycie głowy (head)
        # W - oczy (eye)
        # E - ubrania (body)
        # R - bron (weapon)
        # S - save
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                head.chooseNext()
            if event.key == pygame.K_w:
                eye.chooseNext()
            if event.key == pygame.K_e:
                body.chooseNext()
            if event.key == pygame.K_r:
                weapon.chooseNext()

            if event.key == pygame.K_s: # !!!!!!!
                save = True # !!!!!!!!!
        

    screen.blit(background_img, (0,0))
    screen.blit(base_img, (270, 130))

    screen.blit(head.chosenImage(), (270, 130))
    screen.blit(body.chosenImage(), (270, 130))
    screen.blit(eye.chosenImage(), (270, 130))
    screen.blit(weapon.chosenImage(), (270, 130))

                                                    #  x  , y
    print_text(screen, f"[Q] Head: {head.chosen+1}", (100, 100))
    print_text(screen, f"[W] Eyes: {eye.chosen+1}", (100, 140))
    print_text(screen, f"[E] Body: {body.chosen+1}", (100, 180))
    print_text(screen, f"[R] Weapon: {weapon.chosen+1}", (100, 220))
    # .....

    if save:
        pass
    pygame.display.flip() # .update()

    clock.tick(60)
    pass
pygame.quit()
quit()
