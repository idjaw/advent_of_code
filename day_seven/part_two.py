import re


def supports_ssl(data):
    aba_collection = set()
    aba_matches = re.findall('\[(.*?)\]', data)
    for s in aba_matches:
        i = 0
        while i <= len(s):
            chunk = s[i:3 + i:]
            i += 1
            if len(chunk) == 3 and chunk[0] == chunk[2]:
                aba_collection.add(chunk)
    res = re.sub('\[.*?\]', '%', data)
    for aba in aba_collection:
        bab_check = aba[1] + aba[0] + aba[1]
        if bab_check in res:
            return True
    return False


def valid_accumulator(data):
    with open(data) as f:
        inputs = [s.strip() for s in f.readlines()]
    accum = 0
    for line in inputs:
        if supports_ssl(line):
            accum += 1
    return accum


if __name__ == '__main__':
    print(valid_accumulator('inputs.txt'))
    # 231

