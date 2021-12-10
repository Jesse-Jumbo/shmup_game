# 設螢幕寬480，高600適合射擊遊戲，並且將幀數設成60，讓動作順暢快速
from os import path

import pygame

pygame.mixer.init()

WIDTH = 480
HEIGHT = 600
FPS = 60

img_dir = path.join(path.dirname(__file__), '../img')
snd_dir = path.join(path.dirname(__file__), '../../snd')

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup!")
clock = pygame.time.Clock()

# Load BG
background = pygame.image.load(path.join(img_dir, "Space Shooter Background - Imgur.png")).convert()
background_rect = background.get_rect()

'''font'''
font_name = pygame.font.match_font('arial')

# Load other image
player_img = pygame.image.load(path.join(img_dir, "playerShip3_red.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png',
               'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png', 'meteorBrown_tiny2.png', 'meteorGrey_big1.png', 'meteorGrey_big2.png',
               'meteorGrey_big3.png', 'meteorGrey_big4.png', 'meteorGrey_med1.png', 'meteorGrey_med2.png',
               'meteorGrey_small1.png', 'meteorGrey_small2.png', 'meteorGrey_tiny1.png', 'meteorGrey_tiny2.png']
meteor_images = []
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

# Load all game sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)
