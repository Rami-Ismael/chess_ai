#import

import pygame
from constant import WIDTH,HEIGHT, SQUARE_SIZE

FPS = 60
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")

def main():
    run=True
    clock = pygame.time.Clock()
    while run:
        clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    pygame.display().update()

main()
            