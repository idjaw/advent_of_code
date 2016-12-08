from collections import Counter


def get_code(data):
    code = []
    with open(data) as f:
        file_data = f.readlines()
    for line in list(map(list, zip(*file_data)))[:-1]:
        code.append(Counter(''.join(line).strip()).most_common(1)[0][0])
    return ''.join(code)

if __name__ == '__main__':
    print(get_code('inputs.txt'))
    # ikerpcty
