from hashlib import md5
from operator import itemgetter


def get_code(data):
    count = 0
    password_length = 8
    password = {}
    for _ in range(len(data)):
        while True:
            hex_ = md5((data + str(count)).encode()).hexdigest()
            count += 1
            if hex_[5].isdigit() and hex_.startswith('00000') and int(hex_[5]) < password_length:
                if not int(hex_[5]) in password.keys():
                    password[int(hex_[5])] = hex_[6]

            if len(password) == 8:
                break
    # ugh...whatever. Maybe I'll make this nicer/faster....
    list(password.items()).sort(key=itemgetter(0))
    return ''.join(password.values())

if __name__ == '__main__':
    print(get_code('uqwqemis'))
    # 694190cd
