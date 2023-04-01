import pygame

# инициализация Pygame
pygame.init()

# установка размера окна
size = (800, 600)
screen = pygame.display.set_mode(size)

# установка заголовка окна
pygame.display.set_caption("My House")

# определение цветов RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# создание поверхности для рисования
house_surface = pygame.Surface((400, 400))

# настройка параметров крыши
roof_points = [(0, 0), (200, -100), (400, 0)]
roof_color = RED

# настройка параметров второго ската крыши
roof_points2 = [(0, 0), (200, -2000), (400, 0)]

# настройка параметров дома
house_rect = pygame.Rect((50, 200, 300, 200))
house_color = BLUE

# настройка параметров окна
window_rect = pygame.Rect((100, 250, 50, 50))
window_color = WHITE

# настройка параметров двери
door_rect = pygame.Rect((225, 300, 50, 100))
door_color = GRAY

# настройка параметров бассейна
pool_rect = pygame.Rect((75, 350, 150, 50))
pool_color = BLUE

# рисование первого ската крыши на поверхности
pygame.draw.polygon(house_surface, roof_color, roof_points)

# рисование второго ската крыши на поверхности
pygame.draw.polygon(house_surface, roof_color, roof_points2)

# рисование дома на поверхности
pygame.draw.rect(house_surface, house_color, house_rect)

# рисование окна на поверхности
pygame.draw.rect(house_surface, window_color, window_rect)

# рисование двери на поверхности
pygame.draw.rect(house_surface, door_color, door_rect)

# рисование бассейна на поверхности
pygame.draw.rect(house_surface, pool_color, pool_rect)

# основной цикл программы
done = False
while not done:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # заливка экрана черным цветом
    screen.fill(BLACK)

    # отображение поверхности с домом на экран
    screen.blit(house_surface, (200, 100))

    # обновление экрана
    pygame.display.flip()

# завершение Pygame
pygame.quit()
