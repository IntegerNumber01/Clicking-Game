import pygame
import random

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 800))
font = pygame.font.SysFont('freesansbold.ttf', 50)
clock = pygame.time.Clock()


def render_board(squares, size):
    storage = []
    x = int((800 - (size[0] * squares[0])) / 2)
    y = int((800 - (size[1] * squares[1])) / 2)

    for a in range(squares[0]):
        for b in range(squares[1]):
            pygame.draw.rect(screen, (0, 0, 0), (x + (a * size[0]), y + (b * size[1]), size[0], size[1]), 1)
            storage.append((x + (a * size[0]), y + (b * size[1]), size[0], size[1]))

    return storage


def pre_time(counter):
    if counter > 9:
        return '0:'
    else:
        return '0:0'


squares = (5, 5)
size = (50, 50)
score = 0
counter = 30  # seconds
storage = render_board(squares, size)
reset = True
running = True

timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)
score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
timer_text = font.render(pre_time(counter) + str(counter), True, (0, 0, 0))

while running:
    clock.tick()
    mouse = pygame.mouse.get_pos()

    if reset is True:
        number = random.randint(0, (squares[0] * squares[1]) - 1)
        target = (storage[number][0], storage[number][1])
        if random.randint(1, 2) == 1:
            color = (20, 100, 0)
            click = 'left'
        else:
            color = (252, 151, 20)
            click = 'right'
        reset = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT or counter == 1:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] > target[0] and mouse[0] < target[0] + size[0] and mouse[1] > target[1] and mouse[1] < target[1] + size[1]:
                if (event.button == 1 and click == 'left') or (event.button == 3 and click == 'right'):
                    score = score + 1
                    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
                reset = True
        if event.type == timer_event:
            counter = counter - 1
            timer_text = font.render(pre_time(counter) + str(counter), True, (0, 0, 0))

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, color, (target[0], target[1], size[0], size[1]))
    storage = render_board(squares, size)

    screen.blit(score_text, (10, 10))
    screen.blit(timer_text, (650, 10))

    pygame.display.flip()

pygame.quit()

print('Your score was: ' + str(score))
