# von ChatGPT fehlerfrei erzeugt

import random
import pygame

# Initialisierung von Pygame
pygame.init()

# Fenstergröße
WIDTH, HEIGHT = 600, 400

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake Körper
BLOCK_SIZE = 20
snake_speed = 15

# Display erstellen
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initialisieren
snake = [(WIDTH / 2, HEIGHT / 2)]
snake_direction = 'RIGHT'

# Snake Bewegung
def move_snake(direction):
    x, y = snake[0]
    if direction == 'UP':
        y -= BLOCK_SIZE
    elif direction == 'DOWN':
        y += BLOCK_SIZE
    elif direction == 'LEFT':
        x -= BLOCK_SIZE
    elif direction == 'RIGHT':
        x += BLOCK_SIZE
    snake.insert(0, (x, y))
    snake.pop()

# Essen erstellen
food_pos = (random.randrange(0, WIDTH-BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, HEIGHT-BLOCK_SIZE, BLOCK_SIZE))

# Score
score = 0

clock = pygame.time.Clock()

# Hauptspiel Schleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    move_snake(snake_direction)

    # Kollisionserkennung
    if snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT:
        running = False
    for block in snake[1:]:
        if snake[0] == block:
            running = False

    # Essen aufnehmen
    if snake[0] == food_pos:
        food_pos = (random.randrange(0, WIDTH-BLOCK_SIZE, BLOCK_SIZE), random.randrange(0, HEIGHT-BLOCK_SIZE, BLOCK_SIZE))
        snake.append(snake[-1])
        score += 1

    # Hintergrund zeichnen
    win.fill(BLACK)

    # Snake zeichnen
    for block in snake:
        pygame.draw.rect(win, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

    # Essen zeichnen
    pygame.draw.rect(win, RED, (food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Score anzeigen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, (10, 10))

    pygame.display.update()

    # Spielgeschwindigkeit
    clock.tick(snake_speed)

# Spiel beenden
pygame.quit()
