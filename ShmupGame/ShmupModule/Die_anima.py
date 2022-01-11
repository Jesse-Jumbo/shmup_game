from .setting import *


class Die_anima(pygame.sprite.Sprite):
    def __init__(self, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_die_list[0]
        self.rect = self.image.get_rect()
        self.rect.midbottom = bottom
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(player_die_list):
                self.kill()
            else:
                bottom = self.rect.midbottom
                self.image = player_die_list[self.frame]
                self.rect = self.image.get_rect()
                self.rect.midbottom = bottom
