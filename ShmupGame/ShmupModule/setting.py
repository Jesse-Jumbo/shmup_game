# 設螢幕寬480，高600適合射擊遊戲，並且將幀數設成60，讓動作順暢快速
from os import path

import pygame

pygame.mixer.init()

WIDTH = 480
HEIGHT = 600
FPS = 60
POWERUP_TIME = 5000

img_dir = path.join(path.dirname(__file__), '../../img')
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
background = pygame.image.load(path.join(img_dir, "background.png")).convert()
background_rect = background.get_rect()

'''font'''
font_name = pygame.font.match_font('arial')

# Load other image
'''player'''
player00_img = pygame.image.load(path.join(img_dir, "player00.png")).convert_alpha()
player01_img = pygame.image.load(path.join(img_dir, "player01.png")).convert_alpha()
player02_img = pygame.image.load(path.join(img_dir, "player02.png")).convert_alpha()
player03_img = pygame.image.load(path.join(img_dir, "player03.png")).convert_alpha()
player04_img = pygame.image.load(path.join(img_dir, "player04.png")).convert_alpha()
player05_img = pygame.image.load(path.join(img_dir, "player05.png")).convert_alpha()
player06_img = pygame.image.load(path.join(img_dir, "player06.png")).convert_alpha()
player07_img = pygame.image.load(path.join(img_dir, "player07.png")).convert_alpha()
player08_img = pygame.image.load(path.join(img_dir, "player08.png")).convert_alpha()
player09_img = pygame.image.load(path.join(img_dir, "player09.png")).convert_alpha()
player0_5_img = pygame.image.load(path.join(img_dir, "player0.5.png")).convert_alpha()
player1_5_img = pygame.image.load(path.join(img_dir, "player1.5.png")).convert_alpha()
player2_5_img = pygame.image.load(path.join(img_dir, "player2.5.png")).convert_alpha()
player3_5_img = pygame.image.load(path.join(img_dir, "player3.5.png")).convert_alpha()
player4_5_img = pygame.image.load(path.join(img_dir, "player4.5.png")).convert_alpha()
player5_5_img = pygame.image.load(path.join(img_dir, "player5.5.png")).convert_alpha()
player6_5_img = pygame.image.load(path.join(img_dir, "player6.5.png")).convert_alpha()
player7_5_img = pygame.image.load(path.join(img_dir, "player7.5.png")).convert_alpha()
player8_5_img = pygame.image.load(path.join(img_dir, "player8.5.png")).convert_alpha()
player9_5_img = pygame.image.load(path.join(img_dir, "player9.5.png")).convert_alpha()
# player_img = pygame.transform.scale(player_img, (55, 80))
lives_img = pygame.image.load(path.join(img_dir, "lives.png")).convert_alpha()
# player_mini_img = pygame.transform.scale(player_img, (25, 19))
lives_img.set_colorkey(BLACK)
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png',
               'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png', 'meteorBrown_tiny2.png', 'meteorGrey_big1.png', 'meteorGrey_big2.png',
               'meteorGrey_big3.png', 'meteorGrey_big4.png', 'meteorGrey_med1.png', 'meteorGrey_med2.png',
               'meteorGrey_small1.png', 'meteorGrey_small2.png', 'meteorGrey_tiny1.png', 'meteorGrey_tiny2.png']
meteor_images = []
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = f'regularExplosion0{i}.png'
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = f'sonicExplosion0{i}.png'
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()

# Load all game sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
# TODO add sound for powerups
# shield_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew4.wav'))
# power_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew5.wav'))

expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)

all_sprites = pygame.sprite.Group()             # for we can more convenient to update all sprite

mobs = pygame.sprite.Group()
