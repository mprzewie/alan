import csv
import math


class Machine:
    def __init__(self, rules_dict):
        self.rules_dict = rules_dict
        self.state = 's'
        self.tape = None
        self.position = None

    def process(self, sequence, debug=False, max_iters=math.inf):
        if not sequence:
            raise ValueError
        self.tape = ['.'] + [str(s) for s in sequence] + ['.']
        self.position = 1
        i = 0
        while i < max_iters \
                and self.state != 'y' \
                and self.state != 'n':
            if debug:
                print('Iteration:', i)
                print(self)
                print('State:', self.state)
                print('\n')
            i += 1
            self.step()

        if debug:
            print('Iteration:', i)
            print(self)
            print('State:', self.state)
            print('\n')
        return self.state == 'y'

    def step(self):
        cur_sign = self.tape[self.position]
        new_dict = self.rules_dict[self.state][cur_sign]
        new_dir = new_dict['direction']
        new_sign = new_dict['sign']
        new_state = new_dict['state']
        self.tape[self.position] = new_sign
        self.state = new_state
        self.position += new_dir
        if self.position == 0:
            self.tape = ['.'] + self.tape
            self.position += 1
        elif self.position == len(self.tape) - 1:
            self.tape += ['.']

    def __str__(self):
        pos_array = [' ' * len(x) for x in self.tape]
        pos_array[self.position] = '|' * len(pos_array[self.position])
        return str(self.tape) + '\n' + str(pos_array)


def load_settings_from_csv(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    signs = rows[0][1:]
    rules = rows[1:]

    result = {}

    for row in rules:
        state = row[0]
        tups = row[1:]
        state_dict = {}
        for i in range(len(tups)):
            tup = tups[i]
            try:
                sig, st, dir = tup.split(';')
                st = st if st != '' else state
                sig = sig if sig != '' else signs[i]
                dir = -1 if dir == '-' else 1
            except:
                sig, st, dir = None, None, None
            state_dict[signs[i]] = {
                'sign': sig,
                'state': st,
                'direction': dir
            }

        result[state] = state_dict

    return result
