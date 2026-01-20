# Pygame Drawing
# Author: Sarah
# 5 January 2026

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (100, 0, 255)
    BLACK = (30, 30, 0)
    RED = (60, 0, 0)
    GREEN = (0, 80, 0)
    BLUE = (0, 0, 120)
    GREY = (128, 128, 128)
    PINK = (255, 192, 203)
    YELLOW = (255, 255, 0)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
    # draw a red rectangle in the middle of the screen
        pygame.draw.rect(screen, PINK, (WIDTH / 2 - 50, HEIGHT / 2 - 30, 200, 80))
        # draw a. yellow circle on top of the yellow rectangle
        pygame.draw.circle(screen, YELLOW, (WIDTH / 2, HEIGHT / 2 - 80), 40)


        for offset in range(5):
            pygame.draw.line(screen, YELLOW, (WIDTH / 2 + 20, 20 + offset * 10), (WIDTH - 20, HEIGHT / 2 - 20 + offset * 10))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
