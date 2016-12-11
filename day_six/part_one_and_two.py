from collections import Counter


def get_code(data):
    most = []
    least = []
    with open(data) as f:
        file_data = f.readlines()
    for line in list(map(list, zip(*file_data)))[:-1]:
        common_counts = Counter(''.join(line).strip()).most_common()
        most.append(common_counts[0][0])
        least.append(common_counts[-1][0])
    return {'most_common': ''.join(most), 'least_common': ''.join(least)}

if __name__ == '__main__':
    print(get_code('inputs.txt'))
    # ikerpcty (most)
    # uwpfaqrq (least)
