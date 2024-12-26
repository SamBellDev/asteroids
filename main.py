import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
