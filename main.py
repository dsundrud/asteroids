import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
               if event.type == pygame.QUIT:
                      return
        screen.fill(pygame.Color('pink'))
        pygame.display.flip()
        
        dt = (clock.tick(60)) / 1000
		 # 3 seconds	
if __name__ == "__main__":
    main()
