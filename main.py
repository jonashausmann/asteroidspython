import pygame
import player
import circleshape
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player_x = SCREEN_WIDTH/2
    player_y = SCREEN_HEIGHT/2
    player_now = player.Player(player_x, player_y, PLAYER_RADIUS )

    updatable = pygame.sprite.Group(player_now)
    drawable = pygame.sprite.Group(player_now)

    player.Player.containers = (updatable, drawable)

    i = 1
    while i != 0:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)

        screen.fill("black")
#        player_now.update(dt)
        updatable.update(dt)
#        player_now.draw(screen)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick()/1000

if __name__ == "__main__":
    main()
