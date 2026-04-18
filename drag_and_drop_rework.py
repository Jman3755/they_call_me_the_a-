# Source - https://stackoverflow.com/a/41336876
# Posted by furas, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-10, License - CC BY-SA 3.0

import pygame
import sys
# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
FPS = 60

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -

rectangle1 = pygame.rect.Rect(50, 50, 50, 50)
rectangle2 = pygame.rect.Rect(100, 50, 50, 50)
rectangle3 = pygame.rect.Rect(150, 50, 50, 50)
rectangle1_draging = False
rectangle2_draging = False
rectangle3_draging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # - object 1 -
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                if rectangle1.collidepoint(event.pos):
                    rectangle1_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle1.x - mouse_x
                    offset_y = rectangle1.y - mouse_y

                if rectangle2.collidepoint(event.pos):
                    rectangle2_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle2.x - mouse_x
                    offset_y = rectangle2.y - mouse_y

                if rectangle3.collidepoint(event.pos):
                    rectangle3_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle3.x - mouse_x
                    offset_y = rectangle3.y - mouse_y



        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle1_draging = False
                rectangle2_draging = False
                rectangle3_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle1_draging:
                mouse_x, mouse_y = event.pos
                rectangle1.x = mouse_x + offset_x
                rectangle1.y = mouse_y + offset_y

            if rectangle2_draging:
                mouse_x, mouse_y = event.pos
                rectangle2.x = mouse_x + offset_x
                rectangle2.y = mouse_y + offset_y

            if rectangle3_draging:
                mouse_x, mouse_y = event.pos
                rectangle3.x = mouse_x + offset_x
                rectangle3.y = mouse_y + offset_y


   
    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, rectangle1)
    pygame.draw.rect(screen, GREEN, rectangle2)
    pygame.draw.rect(screen, BLUE, rectangle3)
    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
