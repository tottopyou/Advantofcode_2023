from data import *

def create_maze(commands):
    maze = [['.' for _ in range(247)] for _ in range(251)]
    current_position = (0, 0)

    for command in commands:
        direction = command[0]
        steps = int(command[2])
        for _ in range(steps):
            if direction == 'R':
                current_position = (current_position[0], current_position[1] + 1)
            elif direction == 'L':
                current_position = (current_position[0], current_position[1] - 1)
            elif direction == 'U':
                current_position = (current_position[0] - 1, current_position[1])
            elif direction == 'D':
                current_position = (current_position[0] + 1, current_position[1])

            row, col = current_position
            maze[row][col] = '#'

    return maze

key = key_data.split('\n')

maze_result = create_maze(key)

# Print the resulting maze
for row in maze_result:
    print(''.join(row))
