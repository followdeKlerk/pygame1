import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    color = "black"

    shots_group = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid_group, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = shots_group

    asteroidsfield = AsteroidField()
    player = Player(x, y, shots_group)

    tc = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # New GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        dt = tc.tick(60) / 1000
        updatable.update(dt)

        screen.fill(color, rect=None, special_flags=0)

        for unit in drawable:
            unit.draw(screen)

        for shots in shots_group:
            shots.draw(screen)
            updatable.add(shots)

        for asteroid in asteroid_group:
            if asteroid.collision_detection(player):
                sys.exit("Game over!")

        for asteroid in asteroid_group:
            for shot in shots_group:
                if shot.collision_detection(asteroid):
                    shot.kill()
                    asteroid.split()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()


if __name__ == "__main__":
    main()
