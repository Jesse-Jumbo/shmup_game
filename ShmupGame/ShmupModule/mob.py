import pygame
import random
from .setting import *

class Mob(pygame.sprite.Sprite):
    def __init__(self, img_list):                                   # define our initialize function of all we need to initialize object in Mob
        pygame.sprite.Sprite.__init__(self)                         # initialize the self function in pygame.sprite.Sprite
        self.image_orig = random.choice(img_list)                   # randomly choose one in the image list to initialize our original image
        self.image_orig.set_colorkey(BLACK)                         # ignore the black on the Mob image
        self.image = self.image_orig.copy()                         # initialize our image is copied from the original
        self.rect = self.image.get_rect()                           # initialize our rect is to get the image rectangle
        self.radius = int(self.rect.width * .85 / 2)                # initialize the radius of our circle rect
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)  # The initial position of rect.x will be randomly within the range of 0 to WIDTH(minus the width of rect)\
        self.rect.y = random.randrange(-150, -100)                  # the initial posution of rect.y will be randomly within the range of-150 to -100 position
        self.speed_y = random.randrange(1, 8)                       # initialize the y of speed will random at randrange 1~8
        self.speed_x = random.randrange(-3, 3)                      # initialize the x of speed will random at randrange -3~3
        self.rot = 0                                                # initialize our rot is 0 on the rect
        self.rot_speed = random.randrange(-8, 8)                    # initialize the speed of rot will random at randrange -8~8
        self.last_update = pygame.time.get_ticks()                  # set the last update will follow our game time ticks

    def rotate(self):                                               # define rotate to rotate the mob
        now = pygame.time.get_ticks()                               # Declare the now equals game time ticks
        if now - self.last_update > 50:                             # if the now
            self.last_update = now
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
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)


