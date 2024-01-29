import pygame

SCREEN_SIZE = (400, 300)
FPS = 60

# инициализация Pygame / как завести ключ зажигания
pygame.init()

# отобразить экран
screen = pygame.display.set_mode(SCREEN_SIZE)

# объект поможет отслеживать время
clock = pygame.time.Clock()

surface_sky = pygame.image.load("graphics/sky.png").convert()
surface_ground = pygame.image.load("graphics/ground.png").convert()

while True:
    # эвэнт цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(surface_sky, (0, 0))
    screen.blit(surface_ground, (0, 220))

    pygame.display.update()

    clock.tick(FPS)
