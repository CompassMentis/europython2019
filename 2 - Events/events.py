import pygame


MY_EVENT = pygame.USEREVENT + 1


class GameCounter:
    # Keep track of the number of seconds since the start of the game
    # For demonstration purposes we'll do this using a regular event

    def __init__(self, canvas):
        # Start with 0 seconds
        self.value = 0
        self.canvas = canvas

        # Create a PyGame 'font', to draw the text
        self.font = pygame.font.SysFont('Arial', 32)

    def draw(self):
        text_surface = self.font.render(f'{self.value} second(s)', True, pygame.Color('white'))
        self.canvas.blit(text_surface, (500, 10))

    def increase(self):
        self.value += 1


class EventLog:
    # A running list of log entries
    def __init__(self, canvas):
        self.canvas = canvas
        self.entries = []
        self.font = pygame.font.SysFont('Arial', 18)

    def draw(self):
        for i, line in enumerate(self.entries[-28:]):
            text_surface = self.font.render(line, True, pygame.Color('white'))
            self.canvas.blit(text_surface, (20, 10 + 20 * i))

    def add(self, entry):
        self.entries.append(entry)


def write_line(canvas, line_number, text):
    font = pygame.font.SysFont('Arial', 18)
    text_surface = font.render(text, True, pygame.Color('white'))
    canvas.blit(text_surface, (500, 150 + 25 * line_number))


def show_status(canvas):
    write_line(canvas, 0, f'Mouse at: {pygame.mouse.get_pos()}')
    write_line(canvas, 1, f'Mouse state: {pygame.mouse.get_pressed()}')
    write_line(canvas, 2, f'Keyboard: {pygame.key.get_mods()}')
    pressed = pygame.key.get_pressed()
    keys_pressed = [i for i, state in enumerate(pressed) if state]
    write_line(canvas, 3, f'Pressed: {keys_pressed}')


pygame.init()

canvas = pygame.display.set_mode((800, 600))

game_counter = GameCounter(canvas)
event_log = EventLog(canvas)

# Generate an event of type MY_EVENT every 1000 miliseconds
pygame.time.set_timer(MY_EVENT, 1000)

# Wait until the close button (x) is pressed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == MY_EVENT:
            game_counter.increase()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            event_log.add(f'Mouse button down')

        elif event.type == pygame.MOUSEBUTTONUP:
            event_log.add('Mouse button up')

        elif event.type == pygame.KEYDOWN:
            event_log.add('Key down')

        elif event.type == pygame.KEYUP:
            event_log.add('Key up')

            if event.key == pygame.K_LEFT:
                event_log.add('   Left arrow')
            elif event.key == pygame.K_RIGHT:
                event_log.add('   Right arrow')
            else:
                event_log.add(f'    {event.key}')
    canvas.fill((0, 0, 0))
    game_counter.draw()
    show_status(canvas)
    event_log.draw()
    pygame.display.flip()
