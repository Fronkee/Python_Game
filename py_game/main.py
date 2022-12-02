import pygame

pygame.init()

"""  y
     | 
     |
     | ___ ___ ___ x


"""
# player
playerImg  = pygame.image.load('space.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x,y))


# create screen
screen = pygame.display.set_mode((800,600))

# title and icon
pygame.display.set_caption("Space Fix")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


# game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            print("event type", event.type)
            running = False
    
    # keystroke is pressed left to right
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("key left")
            playerX_change = -0.1
        if event.key == pygame.K_RIGHT:
            print("key right")
            playerX_change = 0.1

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
            print("key stroke")

    # key up and down
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            playerY_change = -0.1
            print("Key up")
        if event.key == pygame.K_DOWN:
            playerY_change = 0.1
            print("key down")    

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerY_change = 0
            print("key stroke")

    playerY += playerY_change
    playerX += playerX_change
    # RBG red, green ,blue
    screen.fill((140,100,20))     
    player(playerX,playerY)   
    pygame.display.update()