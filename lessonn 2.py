import math

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
        self.snakebones = []
        self.Lengthsnake = 1
    def update(self):
        previousposition = self.rect

        for item in self.snakebones:
            #if(Distance(item.rect,self.rect)>200):
            #    currentboneposition = item.rect
            #    item.rect = previousposition
            #    previousposition = currentboneposition
            print(item)
            screen.blit(item.image,item.rect)
        self.rect.centerx+=self.speed[0]
        self.rect.centery+=self.speed[1]

        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed[0]=-10
            self.speed[1]=0
        if keys[pygame.K_RIGHT]:
            self.speed[0]=+10
            self.speed[1] = 0
        if keys[pygame.K_UP]:
            self.speed[1]=-10
            self.speed[0] = 0
        if keys[pygame.K_DOWN]:
            self.speed[1]=10
            self.speed[0] = 0
class Bones(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
class Food(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50,SIZE[0])
        self.rect.centery = random.randint(50,SIZE[1])
    def Contact(self):
        self.rect.centerx = random.randint(50, SIZE[0])
        self.rect.centery = random.randint(50, SIZE[1])

def Distance(item1, item2):
    dist = math.sqrt((abs(item1.x-item2.x)**2)+(abs(item1.y-item2.y)**2))
    print(dist)
    return dist
pygame.init()

SIZE = WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
game = True
player = Player()
food = Food()
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    player.update()
    screen.fill((0,0,0))
    screen.blit(player.image, player.rect)
    screen.blit(food.image, food.rect)
    pygame.display.update()
    clock.tick(30)
    if(pygame.sprite.collide_mask(player,food)):
         food.Contact()
         bones = Bones(player.rect.x,player.rect.y)
         player.snakebones.append(bones)


