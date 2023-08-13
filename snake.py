import pygame
from random import *

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])

pygame.init()

SIZE = WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

blue=(0,0,255)
green=(0,255,0)
white=(255,255,255)

score = 1

position=[300,200]
moove=[0,0]
foodpos = [200,100]
block_size=10

snake_list = []

game = True

while game:
    clock.tick(15)
    score_font = pygame.font.Font(None, 35)

    text_score=score_font.render(str(score-1),1,(255,255,245))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
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

    screen.fill((0, 10, 230))
    pygame.draw.rect(screen,white,(position[0],position[1],10,10))
    pygame.draw.rect(screen,green,(foodpos[0],foodpos[1],10,10))
    screen.blit(text_score, (20, 30))
    snake_head = []
    snake_head.append(position[0])
    snake_head.append(position[1])
    snake_list.append(snake_head)
    if(len(snake_list) > score):
        del snake_list[0]
    our_snake(block_size,snake_list)
    pygame.display.update()

    position[0]+=moove[0]
    position[1]+=moove[1]
    if(position[0] == foodpos[0] and position[1] == foodpos[1]):
        foodpos[0] = (randint(0,WIDTH)//10)*10
        foodpos[1] = (randint(0,HEIGHT)//10)*10
        score+=1
    if position[0]>SIZE[0]:
        position[0]-=SIZE[0]
    if position[0]<0:
        position[0]+=SIZE[0]
    if position[1]>SIZE[1]:
        position[1]-=SIZE[1]
    if position[1]<0:
        position[1]+=SIZE[1]