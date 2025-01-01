from constants import ASTEROID_MIN_RADIUS
from shapes import CircleShape
import pygame, random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def split(
        self,
    ):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        spawn_direction1 = self.velocity.rotate(-random_angle)
        spawn_direction2 = self.velocity.rotate(random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        chunk1 = Asteroid(self.position.x, self.position.y, new_radius)
        chunk1.velocity = spawn_direction1 * 1.2

        chunk2 = Asteroid(self.position.x, self.position.y, new_radius)
        chunk2.velocity = spawn_direction2 * 1.2

    def update(self, dt):
        self.position += self.velocity * dt
