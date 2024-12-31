import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    Player.containers = (drawable, updateable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0,0,0)) 
        for item in drawable:
            item.draw(screen)
        for item in updateable:
            item.update(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
