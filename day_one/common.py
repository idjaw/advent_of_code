def get_directions(filename):
    with open(filename) as f:
        return [(s[0], int(s[1:])) for s in f.read().split(', ')]


def move(current_direction, current_position, blocks):
    movement = blocks * sum(current_direction)
    if current_direction[0] == 0:
        return current_position[0], current_position[1] + movement
    else:
        return current_position[0] + movement, current_position[1]


def new_orientation(current_orientation, movement):
    if current_orientation == (0, 1):
        return (-1, 0) if movement == 'L' else (1, 0)
    elif current_orientation == (0, -1):
        return (1, 0) if movement == 'L' else (-1, 0)
    elif current_orientation == (1, 0):
        return (0, 1) if movement == 'L' else (0, -1)
    elif current_orientation == (-1, 0):
        return (0, -1) if movement == 'L' else (0, 1)