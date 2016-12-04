from day_one.common import new_orientation, move, get_directions


def get_location(current_orientation, current_position, directions):
    history = set()
    current_coordinates = current_position
    new_direction = current_orientation
    x = 0
    y = 0
    for coordinates in directions:
        new_direction = new_orientation(new_direction, coordinates[0])
        current_coordinates = move(
            new_direction, current_coordinates, coordinates[1]
        )
        for _ in range(coordinates[1]):
            x += 1 * new_direction[0]
            y += 1 * new_direction[1]
            if (x, y) in history:
                return x, y
            else:
                history.add((x, y))
    return current_coordinates


def main():
    starting_coordinates = (0, 0)
    currently_facing = (0, 1)
    directions = get_directions('inputs.txt')

    return get_location(
        currently_facing, starting_coordinates, directions
    )

if __name__ == '__main__':
    dest_x, dest_y = main()
    print(abs(dest_x) + abs(dest_y))
    # 154
