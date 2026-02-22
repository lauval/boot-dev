import pygame  # game engine
from logger import log_state  # for automated boot dev testing
from constants import SCREEN_HEIGHT, SCREEN_WIDTH  # dimensions
from player import Player

VERSION = pygame.ver


def main():
    print(f"Starting Asteroids with pygame version: {VERSION}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

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

    # run the game loop
    while run_game:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # make the `close window` button work
                return

        screen.fill("black")

        # update player
        player.update(dt)

        # draw player to the screen
        player.draw(screen)

        # refresh the screen
        pygame.display.flip()

        # force the clock to wait until 1/60th of a second has passed before starting the newest loop
        dt = (
            clock.tick(60) / 1000
        )  # clock.tick() returns the time in milliseconds since it was last called


if __name__ == "__main__":
    main()
