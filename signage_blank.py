import pygame

pygame.init()

screen_width = 485
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((128, 128, 128))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            quit()
    pygame.display.update()

# Exit when clicked
