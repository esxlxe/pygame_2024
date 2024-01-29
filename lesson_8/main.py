import pygame

# инициализация Pygame / как завести ключ зажигания
pygame.init()

SCREEN_SIZE = (400, 300)
FPS = 60

# отобразить экран
screen = pygame.display.set_mode(SCREEN_SIZE)

# объект поможет отслеживать время
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill((255,0,255)) # RGB

while True:
    # эвэнт цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(test_surface, (0,0))

    pygame.display.update()

    clock.tick(FPS)
