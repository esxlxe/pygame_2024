import pygame
import sys

SCREEN_SIZE = (700, 500)
FPS = 60
moving_right = False
moving_left = False

# инициация Pygame
pygame.init()
# отображать окно
screen = pygame.display.set_mode(SCREEN_SIZE)
# отслеживать время
clock = pygame.time.Clock()

surface_sky = pygame.image.load("graphics/sky.png")
surface_ground = pygame.image.load("graphics/ground.png")
surface_enemy_fox = pygame.image.load("graphics/enemy_fox.png").convert_alpha()
rect_enemy_fox = surface_enemy_fox.get_rect(midbottom=(420, 420))
surface_player = pygame.image.load("graphics/player.png").convert_alpha()
rect_player = surface_player.get_rect(midbottom=(50, 420))

surface_font = pygame.font.Font("fonts/PressStart.ttf", 20)
surface_text = surface_font.render("HP: __", False, "White")

while True:
    # цикл событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # деинициализация pygame
            pygame.quit()
            # выход из программы
            sys.exit()
        # Проверяем нажата ли клавиша
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                moving_right = True
        if event.type == pygame.KEYUP:
            # TODO: добавьте код по аналогии с KEYDOWN
            ...

    screen.blit(surface_sky, (0, 0))
    screen.blit(surface_ground, (0, 420))
    screen.blit(surface_text, (500, 40))
    screen.blit(surface_enemy_fox, rect_enemy_fox)

    if moving_right == True:
        rect_player.x += 1


    screen.blit(surface_player, rect_player)
    rect_enemy_fox.x -= 3
    if rect_enemy_fox.x < 0:
        rect_enemy_fox.x = 800


    # обновление кадров
    pygame.display.update()

    # Устанавливаем FPS
    clock.tick(FPS)
