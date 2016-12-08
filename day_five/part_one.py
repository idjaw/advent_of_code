from hashlib import md5


def get_code(data):
    count = 0
    code = ""
    for _ in range(len(data)):
        while True:
            hex_ = md5((data + str(count)).encode()).hexdigest()
            count += 1
            if hex_.startswith('00000'):
                code += hex_[5]
                break
    return code

if __name__ == '__main__':
    print(get_code('uqwqemis'))
