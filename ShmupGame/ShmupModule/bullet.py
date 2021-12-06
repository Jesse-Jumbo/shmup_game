from .setting import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):               # define initialize function to initialize all object in Bullet
        pygame.sprite.Sprite.__init__(self) # initialize the self function of pygame.sprite.Sprite
        self.image = bullet_img             # load bullet image
        self.image.set_colorkey(BLACK)      # ignore the black on the bullet image
        self.rect = self.image.get_rect()   # get the rectangle of the bullet image
        self.rect.bottom = y                # initialize our rect.bottom at the y position
        self.rect.centerx = x               # initialize our rect.centerx at the x position
        self.speed_y = -10                  # initialize our speed is -10, which means our bullet will move up

    def update(self):                       # define the update in the Bullet class
        self.rect.y += self.speed_y         # every time we update, the rect will follow our movement
        # kill if it moves off the tpo of the screen
        if self.rect.bottom < 0:
            self.kill()
