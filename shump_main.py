import pygame
from os import path
import shmup_Module

img_dir = path.join(path.dirname(__file__), 'img')

screen = pygame.display.set_mode((shmup_Module.TWIDH, shmup_Module.HEIGHT))
pygame.display.set_caption("Shmup!")

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, shmup_Module.WIDTH)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

background = pygame.image.load(path.join(img_dir, "Space Shooter Background - Imgur.png")).convert()
background_rect = background.get_rect()

score = 0

running = True
while running:
    shmup_Module.clock.tick(shmup_Module.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shmup_Module.player.shoot()

    shmup_Module.all_sprite.update()

    hits = pygame.sprite.groupcollide(shmup_Module.mobs, shmup_Module.bullets, True, True)
    for hit in hits:
        score += 50 - hit.shmup_Module.mobs.radius
        shmup_Module.m = shmup_Module.Mob()
        shmup_Module.all_sprite.add(shmup_Module.m)
        shmup_Module.mobs.add(shmup_Module.m)

    hits = pygame.sprite.spritecollide(shmup_Module.player, shmup_Module.mobs, True, pygame.sprite.collide_circle)
    if hits:
        running = False

    screen.fill(shmup_Module.BLACK)
    screen.blit(background, background_rect)
    shmup_Module.all_sprite.draw(screen)
    draw_text(screen, str(score), 18, shmup_Module.WIDTH / 2, 10)
    pygame.display.flip()

pygame.quit()