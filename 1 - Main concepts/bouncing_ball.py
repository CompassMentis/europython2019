# Background image from https://www.pexels.com/photo/brown-brick-wall-207142/
# Ball image from https://www.maxpixel.net/Sports-Ball-Round-Basketball-Orange-157925

import pygame


class Ball:
    def __init__(self, canvas):
        # Store the drawing canvas (screen)
        self.canvas = canvas

        # Starting location: 20, 20
        self.location_x = 20
        self.location_y = 20

        # Starting speed: 5 right, 5 up
        self.speed_x = 5
        self.speed_y = 5

        # Load the ball image
        self.image = pygame.image.load('ball.png')

    def move(self):
        # Move to the new location
        self.location_x += self.speed_x
        self.location_y += self.speed_y

        # If we're (just) outside the edge, change direction
        if self.location_x < 20:
            self.speed_x = 5
        if self.location_x > 730:
            self.speed_x = -5
        if self.location_y < 20:
            self.speed_y = 5
        if self.location_y > 530:
            self.speed_y = -5

    def draw(self):
        # Draw the ball at its location
        self.canvas.blit(self.image, (self.location_x, self.location_y))

    def reverse(self):
        # When the space bar gets hit, reverse the ball's direction
        self.speed_x *= -1
        self.speed_y *= -1


pygame.init()

# Create a 600 x 600 window
canvas = pygame.display.set_mode((800, 600))

# Load background image
background = pygame.image.load('wall.png')

ball = Ball(canvas)

done = False
while not done:
    for event in pygame.event.get():
        # If close button clicked, finish
        if event.type == pygame.QUIT:
            done = True

        # If the spacebar is pressed, reverse the ball's direction
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ball.reverse()

    # Draw the background and the ball
    canvas.blit(background, (0, 0))
    ball.draw()

    # Show the new canvas
    pygame.display.flip()

    ball.move()
