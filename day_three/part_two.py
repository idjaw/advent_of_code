from day_three.common import valid_triangle_count


def get_data(filename):
    d = []
    with open(filename) as f:
        data = [
            list(map(int, data.strip().split()))
            for data in f.readlines() if data != '\s'
        ]

        for i in range(0, len(data), 3):
            d.extend([list(sl) for sl in zip(*data[i:i + 3])])
    return d

if __name__ == '__main__':
    print(valid_triangle_count(get_data('inputs.txt')))
    # 1838



