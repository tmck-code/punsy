#!/usr/bin/env python3

import sys

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            raw = line.decode('ISO-8859-1')
            if not raw.startswith(';;'):
                yield [i, *raw.strip().split('  ')]
        except UnicodeDecodeError as e:
            print(line)
            raise e

def run(ifpath):
    with open(ifpath, 'rb') as istream, open(ifpath + '.utf8', 'w') as ostream:
        for i, word, phonemes in parse_cmu(istream):
            print(i, word, phonemes)
            ostream.write('|'.join([word, phonemes]) + '\n')

if __name__ == '__main__':
    run(sys.argv[1])
