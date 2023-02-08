import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((500, 500))
font = pygame.font.SysFont('freesansbold.ttf', 50)

text = font.render('IntegerNumber', True, (255, 255, 255))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(text, (125, 200))
    pygame.display.flip()

pygame.quit()
