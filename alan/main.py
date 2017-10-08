import argparse
import math
from alan.machine import Machine, load_settings_from_csv


def main():
    parser = argparse.ArgumentParser(description='Turing Machine simulator')
    parser.add_argument('-s', dest='settings_src', type=str,
                        help='Path to the .csv file containing settings of the Machine')

    parser.add_argument('-f', dest='words_src', type=str,
                        help='Path to the file containing input words')

    parser.add_argument('-w', dest='word', type=str,
                        help='Single word to process')

    parser.add_argument('-d', dest='debug', type=bool, default=False,
                        help='Whether to print the Machine after every step')

    parser.add_argument('-t', dest='timeout', type=float, default=math.inf)

    args = parser.parse_args()

    settings_src = args.settings_src
    words_src = args.words_src
    word = args.word
    debug = args.debug
    timeout = args.timeout

    print('Simulation of Turing Machine with settings from', settings_src)
    settings = load_settings_from_csv(settings_src)

    machine = Machine(settings)
    words = [word]

    for w in words:
        print('Running simulation on word:')
        print(w)
        result = machine.process(w, debug=debug, max_iters=timeout)
        print('Result of simulation:')
        print(result)
