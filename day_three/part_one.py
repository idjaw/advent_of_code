from day_three.common import valid_triangle_count


def get_data(file_name):
    with open(file_name) as f:
        return [
            list(map(int, data.strip().split()))
            for data in f.readlines() if data.strip()
        ]

if __name__ == '__main__':
    print(valid_triangle_count(get_data('inputs.txt')))
    # 1032
