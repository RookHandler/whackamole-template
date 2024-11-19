import pygame
import random

# add a comment
# screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_location = [0, 0]
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_location[0] // 32 == event.pos[0] // 32 and mole_location[1] // 32 == event.pos[1] // 32:
                        mole_location[0] = random.randrange(0, 20) * 32
                        mole_location[1] = random.randrange(0, 16) * 32
            screen.fill("light green")
            for i in range (1, 20):
                pygame.draw.line(screen, "black", (32 * i, 0), (32 * i, 512))
            for i in range (1, 16):
                pygame.draw.line(screen, "black", (0, i * 32), (640, i * 32 ))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_location[0], mole_location[1])))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

