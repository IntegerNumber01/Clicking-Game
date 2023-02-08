import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('left')
            if event.button == 3:
                print('right')

pygame.quit()
