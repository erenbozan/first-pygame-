import pygame
import random
import time

# Set window dimensions
WIN_WIDTH = 600
WIN_HEIGHT = 400

# Initialize the game window
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Main game loop
running = True
pos = (0, 0)  # Define pos variable initially
while running:
    # Run the game until the window is closed
    for event in pygame.event.get():  # Catch all events
        if event.type == pygame.QUIT:  # If close button is clicked
            running = False  # Exit game loop
            pygame.quit()  # Quit pygame
        elif event.type == pygame.MOUSEBUTTONDOWN:  # If the user clicks the mouse
            # Generate a random color
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            pos = pygame.mouse.get_pos()  

            # Draw a circle at the mouse position
            radius = random.randint(10, 50)
            pygame.draw.circle(window, color, pos, radius)
            pygame.display.update()
            
            # Make the circle randomly move
            for i in range(100):
                pygame.draw.circle(window, WHITE, pos, radius)
                pos = (pos[0] + random.randint(-5, 5), pos[1] + random.randint(-5, 5))  # Random movement

                pygame.draw.circle(window, color, pos, radius)  # Draw the circle in the new position
                
                if i==99:
                    pygame.draw.circle(window, WHITE, pos, radius)  
                
                pygame.display.update()
                time.sleep(0.02)