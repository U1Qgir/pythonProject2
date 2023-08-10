import pygame
import  random
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.centerx=WIDTH//2
        self.rect.centery=HEIGHT//2
        self.speed=[0,0]
    def update(self):
        self.rect.centerx+=self.speed[0]
        self.rect.centery+=self.speed[1]
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed[0]=-10

class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
pygame.init()

SIZE = WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode(SIZE)
game = True
player = Player()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((0,0,0))
    screen.blit(player.image, player.rect)
    pygame.display.update()


