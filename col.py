import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
LIGHT_BLUE = (135, 206, 235)
LIGHT_GREEN = (144, 238, 144)
GOLD = (255, 215, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PIXEL_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH // PIXEL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // PIXEL_SIZE
PALETTE_SIZE = 14

pygame.init()
flags = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
pygame.display.set_caption("Pixel Art Game")

grid = [[WHITE] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
palette = [BLACK, WHITE, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, PINK, BROWN, GRAY, LIGHT_BLUE, LIGHT_GREEN, GOLD]
selected_color_index = 0

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            pos = pygame.mouse.get_pos()
            # Convert the position to grid coordinates
            x = pos[0] // PIXEL_SIZE
            y = pos[1] // PIXEL_SIZE
            # Change the color of the pixel at the clicked position
            grid[y][x] = palette[selected_color_index]
        elif event.type == pygame.KEYDOWN:
            # Change the selected color based on the key pressed
            if event.key == pygame.K_LEFT:
                selected_color_index = (selected_color_index - 1) % PALETTE_SIZE
            elif event.key == pygame.K_RIGHT:
                selected_color_index = (selected_color_index + 1) % PALETTE_SIZE
                
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x*PIXEL_SIZE, y*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
            pygame.draw.rect(screen, grid[y][x], rect)
    

    for i in range(PALETTE_SIZE):
        rect = pygame.Rect(i*PIXEL_SIZE, SCREEN_HEIGHT-PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
        pygame.draw.rect(screen, palette[i], rect)
    # Draw a border around the selected color
    rect = pygame.Rect(selected_color_index*PIXEL_SIZE, SCREEN_HEIGHT-PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
    pygame.draw.rect(screen, WHITE, rect, 2)
    
    pygame.display.flip()
pygame.quit()
