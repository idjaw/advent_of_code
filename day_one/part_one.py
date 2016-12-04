from day_one.common import new_orientation, move, get_directions


def get_final_position(current_orientation, current_position, directions):
    current_coordinates = current_position
    new_direction = current_orientation
    for coordinates in directions:
        new_direction = new_orientation(new_direction, coordinates[0])
        current_coordinates = move(
            new_direction, current_coordinates, coordinates[1]
        )

    return current_coordinates


def get_blocks_from_destination(orientation, coordinates, directions):
    x, y = get_final_position(orientation, coordinates, directions)

    return abs(x) + abs(y)


def main():
    starting_coordinates = (0, 0)
    currently_facing = (0, 1)
    directions = get_directions('inputs.txt')

    return get_blocks_from_destination(
        currently_facing, starting_coordinates, directions
    )

if __name__ == '__main__':
    print(main())
    # 230
