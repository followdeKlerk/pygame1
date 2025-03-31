import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    player = Player(x, y)
    color = "black"

    tc = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # New GUI Window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    #
    while True:
        tc.tick(60)
        player.update(dt)
        dt = tc.tick(60) / 1000  # noqa: F841
        screen.fill(color, rect=None, special_flags=0)
        player.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            pygame.display.flip()


if __name__ == "__main__":
    main()
