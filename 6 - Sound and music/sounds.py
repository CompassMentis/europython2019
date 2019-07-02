# Sound from https://opengameart.org/content/atmospheric-interaction-sound-pack - Public domain
import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('anchor_action.wav')
sound.play(7, fade_ms=10000)

# Put your own music file here - the one I used is under copyright
pygame.mixer.music.load('damn_it_janet.ogg')
pygame.mixer.music.play()

# Wait until the close button (x) is pressed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
