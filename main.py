import pygame
import random
SCREEN_SIZE=SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen=pygame.display.set_mode(SCREEN_SIZE)
clock=pygame.time.Clock()
rect_x=200
rect_y=200
speed=5
all_sprite = pygame.sprite.Group() 
player = pygame.sprite.Sprite(all_sprite) 
player.image = pygame.image.load('alien.png') 
player.rect = player.image.get_rect() 
player.rect.x = 50
player.rect.y = 50
coin = pygame.sprite.Sprite(all_sprite) 
coin.image = pygame.image.load('coin.png') 
coin.rect = player.image.get_rect() 
coin.rect.x = random.randint(0,400)
coin.rect.y = random.randint(0,400)
run=True
while run:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect_y-=50
    if keys[pygame.K_d]:
        rect_x+=50
    if keys[pygame.K_a]:
        rect_x-=50
    if keys[pygame.K_s]:
        rect_y+=50

    player.rect.x = rect_x
    player.rect.y = rect_y


    if pygame.sprite.collide_rect(player, coin):
        coin.rect.x = random.randint(0,400)
        coin.rect.y = random.randint(0,400)
        
    all_sprite.draw(screen)
    pygame.display.update()
    clock.tick(100000000)

pygame.quit()