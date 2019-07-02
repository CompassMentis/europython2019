# Import and initialise pygame
import pygame

pygame.init()

# Create a 320 x 240 window
pygame.display.set_mode((320, 240))

# Game loop - wait until the close button (x) is pressed
# Many examples use an infinite loop (while True:), and sys.exit() when done
done = False
while not done:
    for event in pygame.event.get():
        # Was the close button clicked?
        if event.type == pygame.QUIT:
            done = True
