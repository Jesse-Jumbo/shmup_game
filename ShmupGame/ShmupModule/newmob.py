from .setting import *
from .mob import *


def newmob():
    m = Mob(meteor_images)
    all_sprites.add(m)
    mobs.add(m)