import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player
from shot import Shot


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

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #
    # Groups
    #
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = updatable
    AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        # Closes the GUI window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()

        screen.fill("black")

        updatable.update(dt)

        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()  # refreshes the screen

        dt = clock.tick(60) / 1000  # updates delta time


if __name__ == "__main__":
    main()
