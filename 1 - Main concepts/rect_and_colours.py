import pygame

BLUE = (0, 0, 255)

pygame.init()

canvas = pygame.display.set_mode((800, 600))

# White block at 0, 0, size 50wx50h
white_block = pygame.Surface((50, 50))
white_block.fill((255, 255, 255))
canvas.blit(white_block, (0, 0))

# Green block at 100, 0, size 50wx50h
green_block = pygame.Surface((50, 50))
green_block.fill(pygame.Color('green'))
green_rect = green_block.get_rect()
green_rect.x = 100
green_rect.y = 20
canvas.blit(green_block, green_rect)

# Blue block at 200, 50, size 100wx10h
blue_rect = pygame.Rect(200, 50, 100, 10)
blue_block = pygame.Surface(blue_rect.size)
blue_block.fill(BLUE)
canvas.blit(blue_block, blue_rect)

pygame.display.flip()

# Wait until the close button (x) is pressed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
