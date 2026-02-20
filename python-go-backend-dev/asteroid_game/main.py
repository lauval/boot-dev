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


if __name__ == "__main__":
    main()
