# Import
import pygame
from pygame.locals import *
import random
pygame.init()

# Display
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hunt the mole')

# Entities
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('circle.gif')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        self.sound = pygame.mixer.Sound('son01.wav')
        # limit Screen
        self.rect.left = random.randint(0,620)
        self.rect.top = random.randint(0, 460)

    def flee(self):
        self.rect.left = random.randint(0, 620)
        self.rect.top = random.randint(0, 460)

    def cry(self):
        self.sound.play()

    def hit(self, pos):
        return self.rect.collidepoint(pos)

class Shovel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('mt2.gif')
        self.image = pygame.transform.scale(self.image, (120,80))
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


mole = Mole()
shovel = Shovel()

sprite_group = pygame.sprite.Group()
sprite_group.add(mole)
sprite_group.add(shovel)

bg = pygame.image.load('img1.png')
bg = pygame.transform.scale(bg, (size))

bg_red = pygame.Surface(size)
bg_red = bg_red.convert()
bg_red.fill((25,0,0))

font = pygame.font.Font(None, 25)

# Actions ---> Alter

# Assign Variables
keepGoing = True
zahler = 0
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT, 200)

# Loop
while keepGoing:
    # Timer
    clock.tick(30)

    # Event Handling
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif event.type == MOUSEBUTTONDOWN:
            if mole.hit(pygame.mouse.get_pos()):
                mole.cry()
                zahler += 1
                screen.blit(bg_red, (0,0))
                break
        elif event.type == USEREVENT:
            mole.flee()
            pygame.time.set_timer(USEREVENT, 1000)
            screen.blit(bg, (0,0))
            sprite_group.update()
            sprite_group.draw(screen)
            text = font.render(' Score: ' + str(zahler), True, Color('White'))
            screen.blit(text, (10,10))

    # Redisplay
    pygame.display.flip()
