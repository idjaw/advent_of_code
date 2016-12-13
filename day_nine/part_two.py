import re


def text_decompression(text):

    if '(' not in text:
        return len(text)

    decompressed_text = re.search('.*?(?=\()', text).group()
    to_decompress = text[len(decompressed_text):]

    repeater = re.findall('(\(.*?\))', to_decompress)[0]
    repeater_tup = tuple(map(int, repeater[1:-1].split('x')))

    next_part = to_decompress[len(repeater):]

    return \
        len(decompressed_text) + \
        repeater_tup[1] * text_decompression(next_part[0:repeater_tup[0]]) + \
        text_decompression(next_part[repeater_tup[0]:])

if __name__ == '__main__':
    with open('inputs.txt') as f:
        d = f.read().strip()
    print(text_decompression(d))
    # 11658395076
