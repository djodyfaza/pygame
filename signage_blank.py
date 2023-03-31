import pygame
import subprocess

pygame.init()

screen_width = 485
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((128, 128, 128))
pygame.display.set_caption('Digital Signage')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            subprocess.Popen(['python', 'signage.py'])
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False  # Close the current window when mouse is clicked
            subprocess.Popen(['python', 'signage.py'])
    pygame.display.update()

pygame.quit()
