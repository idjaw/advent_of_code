from collections import defaultdict

devices = {}

output_bins = defaultdict(list)


def output_bot(bot):
    print(bot)


class Bot:
    def __init__(self, bot_id, low=None, high=None):
        self.bot_id = bot_id
        self.low = low
        self.high = high

        self.chips = []

    def add_chip(self, chip):
        self.chips.append(int(chip))
        if len(self.chips) == 2 and self.low and self.high:

            if sorted(self.chips) == [17, 61] or sorted(self.chips) == [2, 5]:
                output_bot(str(self))

            self.send_low()
            self.send_high()

    def send_low(self):
        global devices
        global output_bins

        low = min(self.chips)
        self.chips.remove(low)
        devices[self.bot_id] = self

        if "bot" in self.low:
            devices[self.low.split()[1]].add_chip(low)
            devices[self.bot_id] = devices[self.low.split()[1]]
        else:
            output_bins[self.low.split()[1]].append(low)

    def send_high(self):
        global devices
        global output_bins

        high = max(self.chips)
        self.chips.remove(high)
        devices[self.bot_id] = self

        if "bot" in self.high:
            devices[self.high.split()[1]].add_chip(high)
            devices[self.bot_id] = devices[self.high.split()[1]]
        else:
            output_bins[self.high.split()[1]].append(high)

    def __str__(self):
        return '''{{"bot_id": {}, "low": {}, "high": {}, "chips": {}}}'''.\
            format(self.bot_id, self.low, self.high, self.chips)

    def __repr__(self):
        return self.__str__()


def create_all_bot_data_and_get_instructions(data):
    global devices

    instructions = []
    for line in data:
        s = line.split()
        if s[0] == "bot":
            if s[1] not in devices:
                devices[s[1]] = Bot(s[1])
            devices[s[1]].low = "{} {}".format(s[5], s[6])
            devices[s[1]].high = "{} {}".format(s[10], s[11])
        else:
            command = line.split()
            instructions.append((command[5], int(command[1])))
    return instructions


def move_chips(d):
    for bot, chip in d:
        if bot not in devices:
            devices[bot] = Bot(bot_id=bot)
        devices[bot].add_chip(chip)


def get_data(data):
    with open(data) as f:
        return [s.strip() for s in f.readlines()]

if __name__ == '__main__':
    inputs = get_data('inputs.txt')
    bot_instructions = create_all_bot_data_and_get_instructions(inputs)
    move_chips(bot_instructions)
    # part one: "bot_id": 93
    result = output_bins['0'][0] * output_bins['1'][0] * output_bins['2'][0]
    print("output bin result {}".format(result))
    # part two: 47101

