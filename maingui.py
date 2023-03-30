import pygame
import os, sys, time


# Set up Pygame display
pygame.init()
display_width = 495
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Digital Signage")

# Set up font
font = pygame.font.SysFont(None, 48)

# Set up images
img_dir = os.path.join(os.path.dirname(__file__), 'Assets')
background_img = pygame.image.load(os.path.join(img_dir, 'background.jpg'))
# logo_img = pygame.image.load(os.path.join(img_dir, 'logo.png'))

# Set up text
# # text = "Welcome to our store!"
# text_surf = font.render(text, True, (255, 255, 255))
# text_rect = text_surf.get_rect()
# text_rect.center = (display_width // 2, display_height // 2)

# Set up clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Draw background
    display.blit(background_img, (0, 0))

    # Draw logo
    # display.blit(logo_img, (20, 20))

    # Draw text
    # display.blit(text_surf, text_rect)

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(30)
