import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 460
playerX_change = 40

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop


running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # Checking for boundaries of spaceship, so it doesn't go outside of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

        # Enemy Movement
        enemyX += enemyX_change

        if enemyX <= 0:
            enemyX_change = 0.3
        elif enemyX >= 736:
            enemyX_change = -0.3

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
