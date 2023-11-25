import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
width, height = 400, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Timer")

# Set up fonts
font = pygame.font.Font(None, 36)

# Set up colors
white = (255, 255, 255)

# Set up timer variables
current_time = 0  # in seconds
speed = 1  # initial speed
speed_increment = 1  # speed change on arrow key press

# Set up clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = min(3, speed + speed_increment)
            elif event.key == pygame.K_DOWN:
                speed = max(1, speed - speed_increment)

    # Update timer
    current_time += 1 / speed

    # Clear the screen
    screen.fill(white)

    # Render and display the timer
    time_text = f"{int(current_time // 3600):02}:{int((current_time) // 60):02}"
    text_surface = font.render(time_text, True, (0, 0, 0))
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)  # 60 frames per second