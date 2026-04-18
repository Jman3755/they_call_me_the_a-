# --- With the help of Mel, Soency, and Bunny ---

import pygame
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

CELL_SIZE = 50  # Size of each cell in pixels
GRID_COLOR = (0, 0, 0) # Black lines



FPS = 60

# --- Variables ---



# Classes / objects

class Cell:
    def __init__(self, color, rect):
        self.color = color
        self.rect = rect
        self.dragging = False
        self.drag_offset = (0, 0)
    
    def StartDrag(self, mouse_pos):
        self.dragging = True
        self.drag_offset = (self.rect.x - mouse_pos[0], self.rect.y - mouse_pos[1])

    def StopDrag(self):
        self.dragging = False
        # Snap back to nearest grid position
        self.rect.x = round(self.rect.x / CELL_SIZE) * CELL_SIZE
        self.rect.y = round(self.rect.y / CELL_SIZE) * CELL_SIZE
        return None
    
    def UpdateDrag(self, mouse_pos):
        if self.dragging:
            self.rect.x = mouse_pos[0] + self.drag_offset[0]
            self.rect.y = mouse_pos[1] + self.drag_offset[1]

    def Draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

def DrawGrid(surface, cellSize):
    for x in range(0, SCREEN_WIDTH, cellSize):
        for y in range(0, SCREEN_HEIGHT, cellSize):
            rect = pygame.Rect(x, y, cellSize, cellSize)
            pygame.draw.rect(surface, (0, 0, 0), rect, 1)
            continue


# - init -

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tracking System")
clock = pygame.time.Clock()
running = True



def draw_grid():
    """Draws the grid lines."""
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))




# Create cells once, before the game loop so drag state is preserved
cells = [
    Cell((255, 0, 0), pygame.Rect(CELL_SIZE * 0, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE)),
    Cell((0, 255, 0), pygame.Rect(CELL_SIZE * 1, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE)),
    Cell((0, 0, 255), pygame.Rect(CELL_SIZE * 2, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE)),
]

dragged_cell = None


rectangle1 = pygame.rect.Rect(0, 100, 50, 50)
rectangle2 = pygame.rect.Rect(50, 100, 50, 50)
rectangle3 = pygame.rect.Rect(100, 100, 50, 50)
rectangle1_dragging = False
rectangle2_dragging = False
rectangle3_dragging = False

cell_size = 50    
# - mainloop -


clock = pygame.time.Clock()

running = True

while running:

    
    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rectangle1.collidepoint(event.pos):
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle1.x - mouse_x
                    offset_y = rectangle1.y - mouse_y
                    rectangle1_dragging = True
                
                

                if rectangle2.collidepoint(event.pos):
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle2.x - mouse_x
                    offset_y = rectangle2.y - mouse_y
                    rectangle2_dragging = True
                
            

                if rectangle3.collidepoint(event.pos):
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle3.x - mouse_x
                    offset_y = rectangle3.y - mouse_y
                    rectangle3_dragging = True

                    # snapped_x = (mouse_x // CELL_SIZE) * CELL_SIZE
                    # snapped_y = (mouse_y // CELL_SIZE) * CELL_SIZE

                for cell in cells:
                    if cell.rect.collidepoint(event.pos):
                        cell.StartDrag(event.pos)
                        dragged_cell = cell

        
                        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle1_dragging = False
                rectangle2_dragging = False
                rectangle3_dragging = False



            if dragged_cell:
                dragged_cell.StopDrag()
                dragged_cell = None


        elif event.type == pygame.MOUSEMOTION:
            
            if rectangle1_dragging:
                mouse_x, mouse_y = event.pos
                rectangle1.x = mouse_x + offset_x
                rectangle1.y = mouse_y + offset_y
                
               
            if rectangle2_dragging:
                mouse_x, mouse_y = event.pos
                rectangle2.x = mouse_x + offset_x
                rectangle2.y = mouse_y + offset_y

            
            if rectangle3_dragging:
                mouse_x, mouse_y = event.pos
                rectangle3.x = mouse_x + offset_x
                rectangle3.y = mouse_y + offset_y

            if dragged_cell:
                dragged_cell.UpdateDrag(event.pos)
                
            

    # - draws (without updates) -
    


    screen.fill(WHITE)

    for rectangle_1 in cells:
        rectangle_1.Draw(screen)
    draw_grid()

    for rectangle_2 in cells:
        rectangle_2.Draw(screen)
    draw_grid()

    for rectangle_3 in cells:
        rectangle_3.Draw(screen)
    draw_grid()

    
    pygame.draw.rect(screen, RED, rectangle1)
    pygame.draw.rect(screen, GREEN, rectangle2)
    pygame.draw.rect(screen, BLUE, rectangle3)
    pygame.display.flip()
    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
