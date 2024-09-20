import numpy as np
import random


def initialize_grid():
    grid_size = 10
    grid = np.zeros((grid_size, grid_size), dtype=int)

    player_pos = (0, 0)
    grid[player_pos] = 1

    target_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    while target_pos == player_pos:
        target_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    grid[target_pos] = 9

    num_obstacles = int(grid_size * grid_size * 0.15)
    obstacle_indices = np.random.choice(grid_size * grid_size, num_obstacles, replace=False)
    grid.flat[obstacle_indices] = -1

    grid[player_pos] = 1
    grid[target_pos] = 9

    return grid, player_pos, target_pos


def display_grid(grid):
    print(grid)


def move_player(grid, player_pos, direction):
    new_pos = np.array(player_pos)

    if direction == 'w':  # up
        new_pos[0] -= 1
    elif direction == 's':  # down
        new_pos[0] += 1
    elif direction == 'a':  # left
        new_pos[1] -= 1
    elif direction == 'd':  # right
        new_pos[1] += 1

    if (0 <= new_pos[0] < grid.shape[0]) and (0 <= new_pos[1] < grid.shape[1]) and grid[tuple(new_pos)] != -1:
        grid[player_pos] = 0
        grid[tuple(new_pos)] = 1
        return tuple(new_pos)

    return player_pos


def game():
    grid, player_pos, target_pos = initialize_grid()
    score = 1000  # max

    print("Start!")
    display_grid(grid)

    while player_pos != target_pos:
        move = input("Move -- w = up, s = down, a = left, d = right: ").strip().lower()
        if move in ['w', 's', 'a', 'd']:
            player_pos = move_player(grid, player_pos, move)
            display_grid(grid)
            score -= 1

        if player_pos == target_pos:
            print("WEEHOO! Target reached!!")
            break

    print(f"That's it! Your score is: {score}")


game()
