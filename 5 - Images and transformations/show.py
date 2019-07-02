import pygame

pygame.init()

canvas = pygame.display.set_mode((830, 600))
canvas.fill((255, 192, 192))

# 400 x 270 image
bear = pygame.image.load('bear.png')

# Show full size image at 10, 10
canvas.blit(bear, (10, 10))

# Scale to a just under half size, 195 x 130
small_bear = pygame.transform.scale(bear, (195, 130))

# Show small image at 10, 290
canvas.blit(small_bear, (10, 290))

# Flip small image - horizontal and show next to small image
h_flipped_bear = pygame.transform.flip(small_bear, True, False)
canvas.blit(h_flipped_bear, (215, 290))

# Ditto, vertical flip
v_flipped_bear = pygame.transform.flip(small_bear, False, True)
canvas.blit(v_flipped_bear, (10, 430))

# Ditto, both flip
b_flipped_bear = pygame.transform.flip(small_bear, True, True)
canvas.blit(b_flipped_bear, (215, 430))

# Flatten and show original image
squashed_bear = pygame.transform.scale(bear, (400, 80))
canvas.blit(squashed_bear, (420, 10))

# Rotate 15 degrees counterclockwise
rotated_bear = pygame.transform.rotate(small_bear, 15)
canvas.blit(rotated_bear, (420, 170))

# Ditto - 15 degrees clockwise, rotate and show directly
canvas.blit(
    pygame.transform.rotate(small_bear, -15),
    (570, 380)
)

# Show the result
pygame.display.flip()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
