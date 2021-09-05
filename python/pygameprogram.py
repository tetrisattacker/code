import pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])
def check_if_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

running = True
while running:
    running = check_if_quit()
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()
pygame.quit()