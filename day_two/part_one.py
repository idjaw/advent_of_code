
keypad = [
    '123',
    '456',
    '789'
]


def move(curr_pos, directions):

    for direction in directions:

        x = curr_pos[0]
        y = curr_pos[1]

        if direction == 'U':
            idx = x - 1
            curr_pos = (x, y) if idx < 0 else (idx, y)
        elif direction == 'D':
            idx = x + 1
            curr_pos = (x, y) if idx > 2 else (idx, y)
        elif direction == 'L':
            idx = y - 1
            curr_pos = (x, y) if idx < 0 else (x, idx)
        elif direction == 'R':
            idx = y + 1
            curr_pos = (x, y) if idx > 2 else (x, idx)

    return curr_pos


def get_code(position, inputs):
    final_code = ""
    data = get_inputs(inputs)
    for key_presses in data:
        position = move(position, key_presses)
        final_code += keypad[position[0]][position[1]]

    return final_code


def get_inputs(data):
    with open(data) as f:
        return f.read().split('\n')

if __name__ == '__main__':
    print("final code: {}".format(get_code((1, 1), 'inputs.txt')))
    # 44558
