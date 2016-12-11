import re


def text_decompression(text):

    if '(' not in text:
        return text

    decompressed_text = re.search('.*?(?=\()', text).group()
    sliced = text[len(decompressed_text):]
    repeater = re.findall('(\(.*?\))', sliced)[0]
    repeater_tup = tuple(map(int, repeater[1:-1].split('x')))

    next_part = sliced[len(repeater):]
    sub_str_repeat = ""

    for i in range(repeater_tup[0]):
        sub_str_repeat += next_part[i]

    sub_str_repeat = sub_str_repeat*repeater_tup[1]
    remainder = next_part[repeater_tup[0]:]

    decompressed_text += sub_str_repeat

    return decompressed_text + text_decompression(remainder)

if __name__ == '__main__':
    with open('inputs.txt') as f:
        d = f.read().strip()
    print(len(text_decompression(d)))
    # 120765
