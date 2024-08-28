import pygame
from constants import *


def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0  # delta time, time passed since last frame
    while running:
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # we update our dt, since tick returns ms we divide by 1000 to get secs
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
