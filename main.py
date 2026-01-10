import pygame
from logger import log_state

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize the game
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    # New instance of the GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Closes the GUI window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()
        screen.fill("black")
        pygame.display.flip()  # refreshes the screen

        dt = clock.tick(60) / 1000  # updates delta time


if __name__ == "__main__":
    main()
