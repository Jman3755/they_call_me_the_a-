import pygame

# Initialize Pygame
pygame.init()

# --- Configuration ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 50  # Size of each cell in pixels
GRID_COLOR = (0, 0, 0) # Black lines
BG_COLOR = (255, 255, 255) # White background

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Grid")

def draw_grid():
    """Draws the grid lines."""
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

# --- Main Game Loop ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    draw_grid()
    pygame.display.flip() # Update display

pygame.quit()
