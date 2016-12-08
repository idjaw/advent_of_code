from collections import Counter, defaultdict


def get_data(filename):
    with open(filename) as f:
        data = f.read().strip().split()
    return [
        (
            i[:-10].replace('-', ''),
            int(i.split('-')[-1].split('[')[0]),
            i[-7:][1:-1]
        ) for i in data
        ]


def get_most_common(data):
    d = defaultdict(list)
    for k, v in Counter(data).items():
        d[v].append(k)
    return ''.join(
        ''.join(sorted(v)) for _, v in sorted(d.items(), reverse=True)
    )[:5]


def sum_of_valid_sector_ids(filename):
    data = get_data('inputs.txt')
    valid_sectors = 0
    for name, sector_id, checksum in data:
        valid_sectors += sector_id if get_most_common(name) == checksum else 0
    return valid_sectors


if __name__ == '__main__':
    print(sum_of_valid_sector_ids('inputs.txt'))
    # 137896
