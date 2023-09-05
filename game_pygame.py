import pygame

#init -> initialisation
pygame.init()
jalan = True
#membuat display surface object
win_lebar = 500
win_panjang = 500
window = pygame.display.set_mode((win_lebar,win_panjang))

#object game
#coordinate_position
x = 250
y = 250

#ukuran
panjang = 20
lebar = 20

#kecepatan
speed = 10

while jalan:
    pygame.time.delay(10)
    #user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jalan = False
    
    keyboard = pygame.key.get_pressed()
    if keyboard[pygame.K_LEFT] and x > 0:
        x -= speed
    
    if keyboard[pygame.K_RIGHT] and x < win_lebar-lebar:
        x +=speed

    if keyboard[pygame.K_DOWN] and y < win_panjang-panjang:
        y += speed

    if keyboard[pygame.K_UP] and y > 0:
        y -= speed
    #update asset
    window.fill((255,255,255))
    #render ke display
    pygame.draw.rect(window,(255,120,0),(x,y,lebar,panjang))
    pygame.display.update()

pygame.quit()