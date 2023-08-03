import pygame
from random import *
pygame.init()

SIZE = WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

blue=(0,0,255)
white=(255,255,255)
game = True
score = 0
position=[300,200]
moove=[0,0]
W1=randint(10,580)
H2=randint(10,380)
block_size=10
while game:
    score_font = pygame.font.Font(None, 35)

    text_score=score_font.render(str(score),1,(255,255,245))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if position[0]==W1 and position[1]==H2:
            if event.pos[0] <= W1+20 and event.pos[1]<=H2+20 and event.pos[0] >= W1 and event.pos[1]>=H2:
                W1 = randint(10, 600)
                H2 = randint(10, 400)
                score += 1
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                moove[0]= -block_size
                moove[1]=0
            if event.key==pygame.K_RIGHT:
                moove[0]= block_size
                moove[1] = 0
            if event.key==pygame.K_UP:
                moove[1]= -block_size
                moove[0] = 0
            if event.key==pygame.K_DOWN:
                moove[1]= block_size
                moove[0] = 0

    screen.fill((0, 0, 0))
    if W1 % 10 ==0 and H2 % 10==0:
        pygame.draw.rect(screen,white,(W1,H2,10,10))
    pygame.draw.rect(screen,blue,(position[0],position[1],10,10))
    screen.blit(text_score, (20, 30))

    clock.tick(15)

    pygame.display.update()

    position[0]+=moove[0]
    position[1]+=moove[1]