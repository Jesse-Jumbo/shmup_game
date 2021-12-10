import random

import pygame
from ShmupModule.mob import Mob
from ShmupModule.player import Player
from ShmupModule.bullet import Bullet
from ShmupModule.draw_text import draw_text
from ShmupModule.setting import *
from ShmupModule.newmob import newmob
from ShmupModule.draw_shield_bar import draw_shield_bar

# initialize
pygame.init()
pygame.mixer.init()



score = 0


# Let all sprites can be added and added to all_sprites
player = Player()
all_sprites.add(player)
for i in range(8):
    newmob()

bullets = pygame.sprite.Group()
chances = 0

pygame.mixer.music.play(loops=-1)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(b)
                bullets.add(b)
                shoot_sound.play()

    # Update
    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        newmob()
    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 2
        newmob()
        if player.shield <= 0:
            running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
