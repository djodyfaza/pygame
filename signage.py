import pygame
import os, sys, time, subprocess


# Set up display
dis_hei, dis_wid = 700, 485
display = pygame.display.set_mode((dis_wid, dis_hei))
pygame.display.set_caption("Digital Signage")

# Set up images
img_dir = os.path.join(os.path.dirname(__file__), 'Assets')
images = os.listdir(img_dir)
current_index = 0
current_image = pygame.image.load(os.path.join(img_dir, images[current_index]))
next_index = (current_index + 1) % len(images)
next_image = pygame.image.load(os.path.join(img_dir, images[next_index]))
offset = dis_wid // 10

# Set up clock
clock = pygame.time.Clock()

# Set up delay
delay = 4
last_transition_time = time.time()

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # Quit window when random clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            subprocess.Popen(['python', 'signage_blank.py'])
            pygame.quit()
            quit()

    # Create two surfaces for transition effect
    previous_surface = pygame.Surface((dis_wid, dis_hei))
    previous_surface.blit(current_image, (0, 0))
    next_surface = pygame.Surface((dis_wid, dis_hei))
    next_surface.blit(next_image, (0, 0))

    # Scale images to fit screen
    current_image = pygame.transform.scale(current_image, (dis_wid, dis_hei))
    next_image = pygame.transform.scale(next_image, (dis_wid, dis_hei))

    # Draw current image
    display.blit(current_image, (0, 0))

    # Calculate offset for transition effect
    if offset > 0:
        previous_surface.set_alpha(int(offset / (dis_wid / 255)))
        next_surface.set_alpha(255 - int(offset / (dis_wid / 255)))
        display.blit(previous_surface, (-offset, 0))
        display.blit(next_surface, (dis_wid - offset, 0))
        offset -= 5  # Decrease offset for 5 iteration


    # Transition to next image when delay is over
    elif time.time() - last_transition_time >= delay:
        current_index = next_index
        current_image = next_image
        next_index = (current_index + 1) % len(images)
        next_image = pygame.image.load(os.path.join(img_dir, images[next_index]))
        offset = dis_wid // 10
        last_transition_time = time.time()

    # Update display
    pygame.display.update()

    # Set frame rate
    clock.tick(25)

if __name__=='__main__':
	obj=change_image()
	obj.main()