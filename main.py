## 1
# 9/10/2021 - 13/10/2021
# SPACE INVADER.SV
import pygame
from pygame import mixer
import math
import random

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((600, 700))

# Background
moonImage = pygame.image.load("game_assets/game_images/moon.png")
moonX = 450
moonY = 0
moonY_change = 0.1


def moon(x, y):
    screen.blit(moonImage, (x, y))


meo2 = pygame.image.load('game_assets/game_images/white dot 2.jpg')
meo1 = pygame.image.load('game_assets/game_images/white dot.jpg')
meoType = [meo1, meo2]
meoImage = random.choice(meoType)
meoX = 0
meoY = 0
meoY_change = 2

def fall_meos(x, y):
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 190, y + 29))
    screen.blit(meoImage, (x + 553, y - 498))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 220, y - 633))
    screen.blit(meoImage, (x + 497, y - 43))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 178, y + 275))
    screen.blit(meoImage, (x + 544, y - 799))
    screen.blit(meoImage, (x + 219, y + 327))
    screen.blit(meoImage, (x + 358, y + 744))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 435, y + 45))
    screen.blit(meoImage, (x + 580, y - 260))
    screen.blit(meoImage, (x + 90, y + 529))
    screen.blit(meoImage, (x + 53, y - 398))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 20, y - 133))
    screen.blit(meoImage, (x + 497, y - 43))
    screen.blit(meoImage, (x + 78, y + 475))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 544, y - 99))
    screen.blit(meoImage, (x + 219, y + 227))
    screen.blit(meoImage, (x + 358, y + 744))
    screen.blit(meoImage, (x + 35, y + 5))
    screen.blit(meoImage, (x + 580, y - 260))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 190, y + 29))
    screen.blit(meoImage, (x + 53, y - 598))
    screen.blit(meoImage, (x + 220, y - 333))
    screen.blit(meoImage, (x + 97, y - 243))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 178, y + 575))
    screen.blit(meoImage, (x + 544, y - 399))
    screen.blit(meoImage, (x + 19, y + 727))
    meoImage = random.choice(meoType)
    screen.blit(meoImage, (x + 358, y + 44))
    screen.blit(meoImage, (x + 35, y + 25))
    screen.blit(meoImage, (x + 580, y - 60))


# Sound
mixer.music.load("game_assets/game_sounds/deadite-ash-vs-evil-dead-song--8688.mp3")
# mixer.music.load("demon-slayer-8687.mp3")
mixer.music.play(-1)

pygame.display.set_caption("SPACE INVADERS.SV")
icon = pygame.image.load('game_assets/game_images/spaceship (1).png')
pygame.display.set_icon(icon)

# shipImage = pygame.image.load('game_assets/game_images/spaceship (1).png')
# shipImage = pygame.image.load('game_assets/game_images/spaceship (3).png')
shipImage = pygame.image.load('game_assets/game_images/spaceship (4).png')
shipX = 262
shipY = 635
shipX_change = 0

# Enemy
ufoType = []
ufoX = []
ufoY = []
ufoX_change = []
ufoY_change = []
num_of_ufos = 5

for i in range(num_of_ufos):
    # ufoImage = pygame.image.load('ufo.png')
    # ufo2Image = pygame.image.load('ufo 2.png')
    # ufosImage = [ufoImage, ufo2Image]
    ufoType.append(pygame.image.load('game_assets/game_images/ufo.png'))
    # ufoType.append('ufoType')
    ufoX.append(random.randint(0, 535))
    ufoY.append(random.randint(0, 10))
    ufoX_change.append(0.3)
    ufoY_change.append(0.3)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

'''bulletImg = pygame.image.load('game_assets/game_images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"'''
bulletImage2 = pygame.image.load('game_assets/game_images/laser1.png')
bulletImage1 = pygame.image.load('game_assets/game_images/laser.png')
bulletType = [bulletImage1, bulletImage2]
bulletImage = random.choice(bulletType)
bulletX = 0
bulletY = 635
bulletY_change = 2
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 30)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def ship(x, y):
    screen.blit(shipImage, (x, y))


def ufo(x, y, i):
    screen.blit(ufoType[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    bulletImage = random.choice(bulletType)
    screen.blit(bulletImage, (x - 2, y))
    screen.blit(bulletImage, (x + 34, y))

def isCollision(ufoX, ufoY, bulletX, bulletY):
    distance = math.sqrt(math.pow(ufoX - bulletX, 2) + (math.pow(ufoY - bulletY, 2)))
    if distance < 50:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    moon(moonX, moonY)
    moonY += moonY_change
    if moonY > 900:
        moonY = -100

    fall_meos(meoX, meoY)
    meoY += meoY_change
    if meoY > 800:
        meoY = 0
        meoImage = random.choice(meoType)
    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipX_change = -0.7
            if event.key == pygame.K_RIGHT:
                shipX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("game_assets/game_sounds/3_12.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = shipX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shipX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    shipX += shipX_change
    if shipX <= 0:
        shipX = 0
    elif shipX >= 536:
        shipX = 536

    # Enemy Movement
    for i in range(num_of_ufos):

        # Game Over
        if ufoY[i] > 600:
            for j in range(num_of_ufos):
                ufoY[j] = 610
            game_over_text()

            break

        ufoX[i] += ufoX_change[i]
        ufoY[i] += ufoY_change[i]

        if ufoX[i] <= 0:
            ufoX_change[i] = 0.15
        elif ufoX[i] >= 536:
            ufoX_change[i] = -0.15
        
        # Collision
        collision = isCollision(ufoX[i], ufoY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("game_assets/game_sounds/QuantumTorp.mp3")
            explosionSound.play()
            bulletY = 635
            bullet_state = "ready"
            score_value += 1
            ufoX[i] = random.randint(0, 535)
            ufoY[i] = random.randint(-20, 10)

        ufo(ufoX[i], ufoY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 635
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    ship(shipX, shipY)
    show_score(textX, testY)
    pygame.display.update()
    
