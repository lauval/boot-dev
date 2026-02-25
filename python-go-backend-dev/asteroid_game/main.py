import pygame  # game engine
import sys
from logger import log_state, log_event  # for automated boot dev testing
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

VERSION = pygame.ver


def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()

    # containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    # initialise the pygame instance
    pygame.init()

    clock = pygame.time.Clock()  # to set a refresh rate (see end of game loop below)

    dt = 0  # time between each screen refresh

    # define screen params
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set condition for game loop
    run_game = True

    # initialise player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # initialise asteroid field
    AsteroidField()

    # run the game loop
    while run_game:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # make the `close window` button work
                return

        screen.fill("black")

        # bulk update for all "updatable" objects
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # check for collisions between shots and 
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # drawing objects to the screen requires a specific type of sprite (sprite.image)
        # our sprites need to be drawn procedurally, therefore we need an additional `for` loop to handle rendering
        for drawable_object in drawable:
            # render drawable objects
            drawable_object.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # force the clock to wait until 1/60th of a second has passed before starting the newest loop
        dt = (
            clock.tick(60) / 1000
        )  # clock.tick() returns the time in milliseconds since it was last called


if __name__ == "__main__":
    main()
