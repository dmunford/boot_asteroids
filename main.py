import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Init game, clock, screen
    pygame.init()
    dt = 0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set up player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Set up asteroids
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    af = AsteroidField()

    # Set up shots
    Shot.containers = (updatable, drawable, shots)
    # shots = Shot()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                exit()
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__=="__main__":
    main()