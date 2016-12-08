import re


def is_valid_tls(data):
    s = re.findall('\[(.*?)\]', data)
    for thing in s:
        i = 0
        while i <= len(thing):
            tm = thing[i:4 + i:]
            i += 1
            if len(tm) == 4 and tm == tm[::-1]:
                return False
    res = re.sub('\[.*?\]', '%', data)
    i = 0
    while i <= len(res):
        tm = res[i:4 + i:]
        i += 1
        if '%' in tm:
            continue
        if len(tm) == 4 and tm == tm[::-1] and len(set(tm)) == 2:
            return True
    return False


def valid_accumulator(data):
    with open(data) as f:
        inputs = [s.strip() for s in f.readlines()]
    accum = 0
    for line in inputs:
        if is_valid_tls(line):
            accum += 1
    return accum

if __name__ == '__main__':
    print(valid_accumulator('inputs.txt'))
    # 115
