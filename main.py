import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    # INIT
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()
    dt = 0  # delta time, time passed since last frame
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)
        player.draw(screen)
        pygame.display.flip()

        # used to limit to 60 fps
        # we update our dt, since tick returns ms we divide by 1000 to get secs
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
