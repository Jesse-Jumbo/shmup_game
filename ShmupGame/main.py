import random

import pygame

from ShmupGame.ShmupModule.Die_anima import Die_anima
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

stop = False

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
    if keystate[pygame.K_SPACE] and not player.die_time:
        now = pygame.time.get_ticks()
        if now - player.last_shot > player.shoot_delay:
            player.last_shot = now
            if player.power == 1:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if player.power >= 2:
                bullet1 = Bullet(player.rect.left, player.rect.centery)
                bullet2 = Bullet(player.rect.right, player.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    if keystate[pygame.K_p]:
        stop = not stop

    # Update
    if not stop:
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
            # shield_sound.player()
            if player.shield >= 100:
                player.shield = 100

        if hit.type == 'gun':
            player.powerup()
            # power_sound.player()
    # check to see if a mob hit the player
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        newmob()
        if not player.die_time:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)

            if 100 >= player.shield > 90:
                player.image = player_images["100-91"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 90 >= player.shield > 80:
                player.image = player_images["90-81"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 80 >= player.shield > 70:
                player.image = player_images["80-71"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 70 >= player.shield > 60:
                player.image = player_images["70-61"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 60 >= player.shield > 50:
                player.image = player_images["60-51"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 50 >= player.shield > 40:
                player.image = player_images["50-41"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 40 >= player.shield > 30:
                player.image = player_images["40-31"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 30 >= player.shield > 20:
                player.image = player_images["30-21"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 20 >= player.shield > 10:
                player.image = player_images["20-11"][1]
                player.hit_changes = pygame.time.get_ticks()
            elif 10 >= player.shield > 1:
                player.image = player_images["10-1"][1]
                player.hit_changes = pygame.time.get_ticks()

    if player.lives == 0 and player.frame == 0:
        pass
        # running = False
    # Draw / render
    # screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 5, 5, player.shield)
    draw_lives(screen, WIDTH - 100, 5, player.lives, lives_img)
    # check hit rect
    # pygame.draw.circle(screen, BLACK, player.rect.center, player.radius, 1)
    # for mob in mobs:
    #     pygame.draw.circle(screen, RED, mob.rect.center, mob.radius, 1)
    # *after* drawing everything, flip the display

    pygame.display.flip()

pygame.quit()
