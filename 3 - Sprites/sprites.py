from random import randint
import pygame

NEW_BLOCK_EVENT = pygame.USEREVENT + 1
BLOCK_SIZE = 50
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CANVAS_EDGE_X = CANVAS_WIDTH - BLOCK_SIZE - 1
CANVAS_EDGE_Y = CANVAS_HEIGHT - BLOCK_SIZE - 1
BLACK = (0, 0, 0)


def random_colour():
    return randint(0, 255), randint(0, 255), randint(0, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.image.fill(random_colour())
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, CANVAS_EDGE_X)
        self.rect.y = -BLOCK_SIZE

    def move(self):
        self.rect.y += 1


def create_new_block():
    new_block = Block()
    while pygame.sprite.spritecollide(new_block, all_blocks, False):
        new_block = Block()
    all_blocks.add(new_block)
    falling_blocks.add(new_block)


def update():
    stopped_blocks = []
    for block in falling_blocks:
        block.move()
        if block.rect.y > CANVAS_EDGE_Y or \
                pygame.sprite.spritecollide(block, stable_blocks, False):
            stopped_blocks.append(block)

    for block in stopped_blocks:
        falling_blocks.remove(block)
        stable_blocks.add(block)


pygame.init()
canvas = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

all_blocks = pygame.sprite.Group()
falling_blocks = pygame.sprite.Group()
stable_blocks = pygame.sprite.Group()

pygame.time.set_timer(NEW_BLOCK_EVENT, 500)
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == NEW_BLOCK_EVENT:
            create_new_block()

    canvas.fill(BLACK)
    all_blocks.draw(canvas)
    pygame.display.flip()

    update()
    clock.tick(60)
