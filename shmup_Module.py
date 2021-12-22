import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 480
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50,38))
        self.image.set_colorkey(BLACK)
        self.rect = pygame.image.get_rect()
        self.radius = 20
        #pygame.draw.circle(self.image, RED, self.rect.centerm, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0

        def update(self):
            self.speed_x = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speed_x = -5
            if keystate[pygame.K_RIGHT]:
                self.speed_x = 5
            self.rect.x += self.speed_x
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

        def shoot(self):
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprite.add(bullet)
            bullet.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.cope()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.draw.circle(self.image, REDm self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.lact_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top > HEIGHT + 10 or self.rect.left < - 25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()

player_img = pygame.image.load(path.join(img_dir, "playerShip3_red.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue16.png")).convert()
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png',
               'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
               'meteorBrown_tiny1.png', 'meteorBrown_tiny2.png', 'meteorGrey_big1.png', 'meteorGrey_big2.png',
               'meteorGrey_big3.png', 'meteorGrey_big4.png', 'meteorGrey_med1.png', 'meteorGrey_med2.png',
               'meteorGrey_small1.png', 'meteorGrey_small2.png', 'meteorGrey_tiny1.png', 'meteorGrey_tiny2.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

all_sprite = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprite.add(player)
for i in range(8):
    m = Mob()
    all_sprite.add(m)
    mobs.add(m)

running = True
while running:
    clock.tick(FPS)
    all_sprite.update()