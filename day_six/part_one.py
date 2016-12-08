from collections import Counter


def get_code(data, get_highest=True):
    code = []
    gh = 0 if get_highest else -1
    with open(data) as f:
        file_data = f.readlines()
    for line in list(map(list, zip(*file_data)))[:-1]:
        code.append(Counter(''.join(line).strip()).most_common()[gh][0])
    return ''.join(code)

if __name__ == '__main__':
    print(get_code('inputs.txt'))
    # ikerpcty
    print(get_code('inputs.txt', get_highest=False))
    # uwpfaqrq
