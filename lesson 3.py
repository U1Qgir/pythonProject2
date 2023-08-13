import pygame
from random import *
pygame.init()
yellow=(0,100,2)
black=(255,255,255)
blue=(255,0,0)
W=600
H=400
W1=randint(10,600)
H2=randint(10,400)
game = True
score=0
position=W1,H2
screen=pygame.display.set_mode((W,H))

while game:
    score_font = pygame.font.Font(None, 35)

    text_score=score_font.render(str(score),1,(255,255,245))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] <= W1+15 and event.pos[1]<=H2+15 and event.pos[0] >= W1 and event.pos[1]>=H2:
                W1 = randint(10, 600)
                H2 = randint(10, 400)
                score += 1
    screen.fill((0,0,0))
    screen.blit(text_score,(20,30))
    pygame.draw.rect(screen,black,(W1,H2,15,15))
    pygame.display.update()