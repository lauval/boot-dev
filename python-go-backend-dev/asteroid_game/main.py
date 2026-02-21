import pygame  # game engine
from logger import log_state  # for automated boot dev testing
from constants import SCREEN_HEIGHT, SCREEN_WIDTH  # dimensions

VERSION = pygame.ver


def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialise the pygame instance
    pygame.init()

    clock = pygame.time.Clock()  # to set a refresh rate (see end of game loop below)

    dt = 0

    # define screen params
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set condition for game loop
    run_game = True

    # run the game loop
    while run_game:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # make the `close window` button work
                return

        screen.fill("black")

        pygame.display.flip()  # refresh the screen

        dt = clock.tick(60) / 1000 # clock.tick() returns the time in milliseconds since it was last called

        print(dt)

if __name__ == "__main__":
    main()
