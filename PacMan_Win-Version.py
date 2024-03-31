# von ChatGPT erzeugt, msvcrt gegen Pygame-Abfragen ersetzt

import os
import random
import msvcrt

# Spielfeldgröße
WIDTH = 20
HEIGHT = 10

# Symbole
WALL = '#'
EMPTY = ' '
PACMAN = 'C'
GHOST = 'G'
COIN = '*'

# Initialisierung des Spielfelds
game_map = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]
pacman_x, pacman_y = WIDTH // 2, HEIGHT // 2
game_map[pacman_y][pacman_x] = PACMAN
ghost_x, ghost_y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
game_map[ghost_y][ghost_x] = GHOST
coins = [(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)) for _ in range(5)]
for coin_x, coin_y in coins:
    game_map[coin_y][coin_x] = COIN

def display_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in game_map:
        print(''.join(row))
    print("Use arrow keys to move Pac-Man. Press 'q' to quit.")

def move_pacman(dx, dy):
    global pacman_x, pacman_y
    new_x, new_y = pacman_x + dx, pacman_y + dy
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and game_map[new_y][new_x] != WALL:
        game_map[pacman_y][pacman_x] = EMPTY
        pacman_x, pacman_y = new_x, new_y
        game_map[pacman_y][pacman_x] = PACMAN

def move_ghost():
    global ghost_x, ghost_y
    dx = random.choice([-1, 0, 1])
    dy = random.choice([-1, 0, 1])
    new_x, new_y = ghost_x + dx, ghost_y + dy
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and game_map[new_y][new_x] != WALL:
        game_map[ghost_y][ghost_x] = EMPTY
        ghost_x, ghost_y = new_x, new_y
        game_map[ghost_y][ghost_x] = GHOST

def check_collision():
    if (pacman_x, pacman_y) == (ghost_x, ghost_y):
        return True
    return False

def check_coin():
    global coins
    if (pacman_x, pacman_y) in coins:
        coins.remove((pacman_x, pacman_y))
        return True
    return False

def game_over():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Game Over!")
    print("Score:", 5 - len(coins))
    exit()

def game_loop():
    while True:
        display_game()
        if check_collision():
            game_over()
        if len(coins) == 0:
            print("You won!")
            exit()
        key = msvcrt.getch()
        if key == b'q':
            exit()
        elif key == b'\xe0':  # arrow keys
            key = msvcrt.getch()
            if key == b'H':  # up arrow
                move_pacman(0, -1)
            elif key == b'P':  # down arrow
                move_pacman(0, 1)
            elif key == b'K':  # left arrow
                move_pacman(-1, 0)
            elif key == b'M':  # right arrow
                move_pacman(1, 0)
        move_ghost()
        if check_collision():
            game_over()
        if check_coin():
            print("Coin collected!")

game_loop()
