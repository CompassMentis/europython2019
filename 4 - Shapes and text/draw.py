import pygame


def draw_shapes(canvas):
    # For a list of colour names see
    # https://mike632t.wordpress.com/2018/02/10/displaying-a-list-of-the-named-colours-available-in-pygame/

    # rect(Surface, color, Rect, width=0) -> Rect
    pygame.draw.rect(canvas, pygame.Color('red'), (10, 10, 50, 50), 5)
    pygame.draw.rect(canvas, pygame.Color('green'), (10, 70, 50, 50))

    # polygon(Surface, color, pointlist, width=0) -> Rect
    pygame.draw.polygon(canvas, pygame.Color('blue'),
                        ((10, 200), (50, 200), (40, 230), (50, 260), (10, 260), (20, 230)), 5)
    pygame.draw.polygon(canvas, pygame.Color('lightcoral'),
                        ((10, 300), (50, 300), (40, 330), (50, 360), (10, 360), (20, 330)))

    # circle(Surface, color, pos, radius, width=0) -> Rect
    pygame.draw.circle(canvas, pygame.Color('lightgoldenrod'), (50, 420), 25, 5)
    pygame.draw.circle(canvas, pygame.Color('lightskyblue'), (50, 500), 25)

    # ellipse(Surface, color, Rect, width=0) -> Rect
    pygame.draw.ellipse(canvas, pygame.Color('lightsteelblue'), (200, 10, 100, 50), 5)
    pygame.draw.ellipse(canvas, pygame.Color('magenta'), (200, 100, 100, 50))

    # arc(Surface, color, Rect, start_angle, stop_angle, width=1) -> Rect
    pygame.draw.arc(canvas, pygame.Color('mediumaquamarine'), (200, 200, 50, 50), 0, 2, 5)
    pygame.draw.arc(canvas, pygame.Color('mediumorchid'), (200, 250, 50, 50), 0, 2)

    # line(Surface, color, start_pos, end_pos, width=1) -> Rect
    # aaline(Surface, color, startpos, endpos, blend=1) -> Rect    (thin line, anti-aliased)
    # Note the final arguments for these: width vs blend
    pygame.draw.rect(canvas, pygame.Color('red'), (200, 300, 100, 80))
    pygame.draw.line(canvas, pygame.Color('white'), (200, 300), (300, 320), 5)
    pygame.draw.line(canvas, pygame.Color('white'), (200, 320), (300, 340), 1)
    pygame.draw.aaline(canvas, pygame.Color('white'), (200, 340), (300, 360), True)
    pygame.draw.aaline(canvas, pygame.Color('white'), (200, 360), (300, 380), False)

    # lines(Surface, color, closed, pointlist, width=1) -> Rect
    # aalines(Surface, color, closed, pointlist, blend=1) -> Rect
    # Like above, note the final arguments
    pygame.draw.lines(canvas, pygame.Color('blue'), False, ((200, 400), (250, 400), (200, 420), (250, 420)), 5)
    pygame.draw.lines(canvas, pygame.Color('yellow'), True, ((200, 450), (250, 455), (200, 470), (250, 475)), 1)
    pygame.draw.aalines(canvas, pygame.Color('white'), False, ((200, 500), (250, 505), (200, 520), (250, 525)))


def write_font(font_type, font_size, canvas, location, bold=False, italic=False):
    font_description = f'{font_type}, size {font_size}'
    if bold:
        font_description += ', bold'
    if italic:
        font_description += ', italic'

    # SysFont(name, size, bold=False, italic=False) -> Font
    font = pygame.font.SysFont(font_type, font_size, bold, italic)

    # render(text, antialias, color, background=None) -> Surface
    text_surface = font.render(font_description, True, pygame.Color('white'))

    canvas.blit(text_surface, location)


def draw_text(canvas):
    write_font('Arial', 18, canvas, (400, 10))
    write_font('Arial', 24, canvas, (400, 40))
    write_font('Arial', 48, canvas, (400, 90))
    write_font('Courier New', 24, canvas, (400, 170))
    write_font('Courier New', 24, canvas, (400, 230), bold=True)
    write_font('Courier New', 24, canvas, (400, 270), italic=True)


pygame.init()

canvas = pygame.display.set_mode((800, 600))

draw_shapes(canvas)
draw_text(canvas)
pygame.display.flip()

# Wait until the close button (x) is pressed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
