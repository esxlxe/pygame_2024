import pygame
import sys
import random

SCREEN_SIZE = (700, 500)
FPS = 60
moving_right = False
moving_left = False
player_gravity = 0
hp = 100
player_score = 0
collision_dectected = False
collision_cooldown = 0
cooldown_duration = 30
is_paused = False
is_damaged = False

# инициируем Pygame модуль
pygame.init()
pygame.mixer.init()

# отображение (окно)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("My first game")

# создать объект для отслеживания времени
clock = pygame.time.Clock()
# create font
# my_font = pygame.font.Font(None, 50)
my_font = pygame.font.Font("font/Pixeltype.ttf", 60)

# создание surface
surface_ground = pygame.image.load("graphics/ground.png").convert() # Pygame will run faster
surface_bg = pygame.image.load("graphics/bg_rock.png").convert()
enemy_wolf = pygame.image.load("graphics/enemy_wolf.png").convert_alpha()
enemy_rect = enemy_wolf.get_rect(midbottom=(380, 424))

player_surface = pygame.image.load("graphics/player/player_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 424))

# collision_sound = pygame.mixer.Sound("sounds/damage.wav")

while True:
    # event loop - проверять все эвэнты
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # деинициализация Pygame
            pygame.quit()
            # завершение работы программы
            sys.exit()

        # Пользователь нажал клавишу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE and player_rect.bottom == 424:
                player_gravity = -20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    if not is_paused: # NEW
        if moving_left:
            player_rect.x -= 1
        if moving_right:
            player_rect.x += 1

        collision_dectected = player_rect.colliderect(enemy_rect)

        if collision_dectected and collision_cooldown == 0:
            random_damage = random.randint(8, 12)
            hp -= random_damage
            if enemy_rect.x != 0:
                is_damaged = True
            # collision_sound.play()
            collision_cooldown = cooldown_duration
        if collision_cooldown > 0:
            collision_cooldown -= 1

        text_surface_hp = my_font.render(f"HP: {hp}", False, "Red")
        # TODO 1 - добавить score
        text_surface_score = my_font.render(f"score: {player_score}", False, "Red")
        screen.blit(surface_bg, (0, 0))
        # screen.blit(surface_sky, (0, 0))
        screen.blit(surface_ground, (0, 424))
        screen.blit(text_surface_hp, (500, 40))
        screen.blit(text_surface_score, (500, 80))

        screen.blit(enemy_wolf, enemy_rect)
        screen.blit(player_surface, player_rect)

        player_rect.y += player_gravity
        player_gravity += 1 # 0 1 3 5 8 13

        if player_rect.bottom >= 424:
            player_rect.bottom = 424

        enemy_rect.x -= 4
        if enemy_rect.x < -50:
            enemy_rect.x = 800
            is_damaged = False
        if enemy_rect.x == 0 and is_damaged == False:
            player_score += 1

        if player_rect.bottom < 0:
            player_rect.bottom = 500

        if hp <= 0:
            is_paused = True

        # обновлять фрэймы
        pygame.display.update()
        # framerate (частота кадров) -
        # верхняя граница, чтобы не обновлялось слишком быстро
        clock.tick(FPS)
