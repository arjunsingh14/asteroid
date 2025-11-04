import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        dt = clock.tick(60) / 1000
        for object in drawable:
            object.draw(screen)
        for asteroid in asteroids:
            for s in shots:
                if asteroid.check_collision(s):
                    asteroid.split()
                    s.kill()
            if asteroid.check_collision(player):
                print("Game Over!")
                sys.exit()
        updateable.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
