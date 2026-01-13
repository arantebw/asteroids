import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Invoke CircleShape's constructor
        self.rotation = 0

    def triangle(self):
        """Draw the player's ship."""

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Override the CircleShape's implementation of the draw method."""

        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
