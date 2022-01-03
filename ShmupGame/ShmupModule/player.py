import pygame

from .setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player00_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.hit_changes = pygame.time.get_ticks()
#
    def update(self):
        now = pygame.time.get_ticks()                               # Declare the now equals game time ticks
        if now - self.hit_changes > 1000:                             # if the now
            self.hit_changes
            if 100 >= self.shield > 90:
                self.image = player00_img
            elif 90 >= self.shield > 80:
                self.image = player01_img
            elif 80 >= self.shield > 70:
                self.image = player02_img
            elif 70 >= self.shield > 60:
                self.image = player03_img
            elif 60 >= self.shield > 50:
                self.image = player04_img
            elif 50 >= self.shield > 40:
                self.image = player05_img
            elif 40 >= self.shield > 30:
                self.image = player06_img
            elif 30 >= self.shield > 20:
                self.image = player07_img
            elif 20 >= self.shield > 10:
                self.image = player08_img
            elif 10 >= self.shield > 1:
                self.image = player09_img
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        # unhide.if hidden
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed_x = -5
        if key_state[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if key_state[pygame.K_UP]:
            self.speed_y = -5
        if key_state[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.y += self.speed_y
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)
