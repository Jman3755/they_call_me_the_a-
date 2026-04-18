# Example file showing a basic pygame "game loop"
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
CELL_SIZE = 50

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

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Create cells once, before the game loop so drag state is preserved
cells = [
    Cell((255, 0, 0), pygame.Rect(CELL_SIZE * 0, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE)),
    Cell((0, 255, 0), pygame.Rect(CELL_SIZE * 1, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE)),
    Cell((0, 0, 255), pygame.Rect(CELL_SIZE * 2, CELL_SIZE * 0, CELL_SIZE, CELL_SIZE)),
]

dragged_cell = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for cell in cells:
                if cell.rect.collidepoint(event.pos):
                    cell.StartDrag(event.pos)
                    dragged_cell = cell
                    break

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragged_cell:
                dragged_cell.StopDrag()
                dragged_cell = None

        elif event.type == pygame.MOUSEMOTION:
            if dragged_cell:
                dragged_cell.UpdateDrag(event.pos)

    # Fill the screen with a color to wipe away anything from last frame
    SCREEN.fill("skyBlue")

    # Draw grid first, then cells on top
    DrawGrid(SCREEN, CELL_SIZE)
    for cell in cells:
        cell.Draw(SCREEN)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()