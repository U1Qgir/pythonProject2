
import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

player=Car(400, 300, 'enemy.png')
player.rect.y=300
player.rect.x=400
enemy=Car(100,300, 'enemy_car.jpg')
enemy.rect.y=100
enemy.rect.x=300
game = True

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    screen.fill((0, 0, 0))
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image,enemy.rect )
    pygame.display.update()
    clock.tick(15)

    if pygame.sprite.collide_mask(player,enemy):
        game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 50
    if keys[pygame.K_RIGHT]:
        player.rect.x += 50
    if keys[pygame.K_DOWN]:
        player.rect.y += 50
    if keys[pygame.K_UP]:
        player.rect.y -= 50

    if keys[pygame.K_a]:
        enemy.rect.x -= 50
    if keys[pygame.K_d]:
        enemy.rect.x += 50
    if keys[pygame.K_s]:
        enemy.rect.y += 50
    if keys[pygame.K_w]:
        enemy.rect.y -= 50


    if player.rect.y == 550:
        player.rect.y -=50
    if player.rect.y == 0:
        player.rect.y +=50
    if player.rect.x == 750:
        player.rect.x -=50
    if player.rect.x == 0:
        player.rect.x +=50


    if enemy.rect.y == 550:
        enemy.rect.y -=50
    if enemy.rect.y == 0:
        enemy.rect.y +=50
    if enemy.rect.x == 750:
        enemy.rect.x -=50
    if enemy.rect.x == 0:
        enemy.rect.x +=50
