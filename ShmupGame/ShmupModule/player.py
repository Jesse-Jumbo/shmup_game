import pygame

from .setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_images["100-91"][0]
        self.rect = self.image.get_rect()
        self.radius = PLAYER_RADIUS
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
        self.frame = 0
        self.die_time = False
#
    def update(self):
        if not self.die_time:
            self.get_key()
        now = pygame.time.get_ticks()                               # Declare the now equals game time ticks
        if now - self.hit_changes > 1000:                             # if the now
            self.hit_changes = now
            if 100 >= self.shield > 90:
                self.image = player_images["100-91"][0]
            elif 90 >= self.shield > 80:
                self.image = player_images["90-81"][0]
            elif 80 >= self.shield > 70:
                self.image = player_images["80-71"][0]
            elif 70 >= self.shield > 60:
                self.image = player_images["70-61"][0]
            elif 60 >= self.shield > 50:
                self.image = player_images["60-51"][0]
            elif 50 >= self.shield > 40:
                self.image = player_images["50-41"][0]
            elif 40 >= self.shield > 30:
                self.image = player_images["40-31"][0]
            elif 30 >= self.shield > 20:
                self.image = player_images["30-21"][0]
            elif 20 >= self.shield > 10:
                self.image = player_images["20-11"][0]
            elif 10 >= self.shield >= 1:
                self.image = player_images["10-1"][0]
        if self.shield <= 0:
            self.die_time = True
            self.img_anima(player_images["0"], self.rect.midbottom)
            if self.frame == 0:
                self.hide()
                self.lives -= 1
                self.die_time = False
                self.shield = 100
        # timeout for powerups
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()
        # unhide.if hidden
        if self.hidden and self.frame == 0:
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.power = 1
            self.hidden = False

    def get_key(self):
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
        self.image = player_images["100-91"][0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def img_anima(self, img_list, midbottom):

        if int(self.frame) == len(img_list):
            self.frame = 0
        else:
            change_image = img_list[int(self.frame)]
            self.image = change_image
            self.rect = self.image.get_rect()
            self.rect.midbottom = midbottom
            self.frame += 0.4
