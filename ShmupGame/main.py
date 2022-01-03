import random

import pygame

from ShmupGame.ShmupModule.Pow import Pow
from ShmupModule.mob import Mob
from ShmupModule.player import Player
from ShmupModule.bullet import Bullet
from ShmupModule.draw_text import draw_text
from ShmupModule.setting import *
from ShmupModule.newmob import newmob
from ShmupModule.draw_shield_bar import draw_shield_bar
from ShmupModule.explosion import Explosion
from ShmupModule.draw_lives import draw_lives

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
powerups = pygame.sprite.Group()

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
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        now = pygame.time.get_ticks()
        if now - player.last_shot > player.shoot_delay:
            player.last_shot = now
            bullet = Bullet(player.rect.centerx, player.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

    # Update
    all_sprites.update()

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    # check to see if player hit a powerup
    hits = pygame.sprite.spritecollide(player, powerups, True)
    for hit in hits:
        if hit.type == 'shield':
            player.shield += random.randrange(10, 30)
            if player.shield >= 100:
                player.shield = 100

        if hit.type == 'gun':
            pass
    # check to see if a mob hit the player
    # hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    # for hit in hits:
    #     player.shield -= hit.radius * 2
    #     expl = Explosion(hit.rect.center, 'sm')
    #     all_sprites.add(expl)
    #     newmob()
    #     if player.shield <= 0:
    #         death_explosion = Explosion(player.rect.center, 'player')
    #         all_sprites.add(death_explosion)
    #         player.hide()
    #         player.lives -= 1
    #         player.shield = 100
    #
    # if player.lives == 0 and not death_explosion.alive():
    #     running = False

    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
