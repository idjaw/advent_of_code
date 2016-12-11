from collections import deque

import re


class Display:

    def __init__(self, screen_x=50, screen_y=6):
        self.grid = deque(
            [
                deque(['' for _ in range(screen_x)])
                for _ in range(screen_y)
            ]
        )

    def enable_pixels(self, row, col):
        for row_ in range(row):
            for col_ in range(col):
                self.grid[row_][col_] = '#'

    def rotation(self, row_or_column, index, rotations):
        if row_or_column == 'column':
            data = deque([row[index] for row in self.grid])
            data.rotate(rotations)

            for i, v in enumerate(data):
                self.grid[i][index] = v
        else:
            self.grid[index].rotate(rotations)

    def enabled_pixel_count(self):
        count = 0
        for ro in self.grid:
            count += ro.count('#')
        return count

    def display_pixels(self):
        for row in self.grid:
            print(''.join('#' if p else ' ' for p in row))


def get_data(inputs):
    with open(inputs) as f:
        data_split = re.split('rect', f.read().strip())

        data_list = [
            [
                i.strip().split('\n')
                for i in re.split('(\d{1,}x\d{1,})', ro, 1)[1:] if i
                ]
            for ro in data_split if ro
            ]

        da = []
        for line in data_list:
            x, y = line[0][0].split('x')
            rect = (int(x), int(y))
            tmp = []
            for ops in line[1]:
                tmp_list = ops.split()
                tmp.append({
                    'rc': tmp_list[1],
                    'pos': int(tmp_list[2].split('=')[1]),
                    'rot': int(tmp_list[4])
                })
            da.append({
                'rect': rect,
                'ops': tmp
            })
    return da


if __name__ == '__main__':
    res = get_data('inputs.txt')
    display = Display()

    for d in res:
        display.enable_pixels(d['rect'][1], d['rect'][0])
        for r in d['ops']:
            display.rotation(r['rc'], r['pos'], r['rot'])

    print("pixel count: {}\n".format(display.enabled_pixel_count()))
    # 115

    print("pixel display:\n")
    display.display_pixels()
    # EFEYKFRFIJ
