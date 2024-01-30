import pygame
import sys

# запустим pygame (инициализируем)
pygame.init()

FPS = 60
SCREEN_SIZE = (600, 400)

# создать окно
screen = pygame.display.set_mode(SCREEN_SIZE)
# для отслеживания времени
clock = pygame.time.Clock()
surface_font_1 = pygame.font.Font("font/NewTimeNerd.ttf", 50)

surface_sky = pygame.image.load("grapics/sky.png").convert()
surface_ground = pygame.image.load("grapics/ground.png").convert()
surface_text_hp = surface_font_1.render("HP ", False, "White")


while True:
    # цикл событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # деинициализация Pygame
            pygame.quit()
            # завершение работы программы
            sys.exit()
    screen.blit(surface_sky, (0, 0))
    screen.blit(surface_ground, (0, 280))
    screen.blit(surface_text_hp, (150, 50))

    # обновлять кадры
    pygame.display.update()
    # верхняя граница FPS
    clock.tick(FPS)
