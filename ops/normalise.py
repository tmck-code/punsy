#!/usr/bin/env python3

import sys

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            raw = line.decode('ISO-8859-1')
            if should_skip(raw):
                continue
            yield [i, *raw.strip().split('  ')]
        except UnicodeDecodeError as e:
            print(line)
            raise e

def should_skip(raw):
    if raw.startswith(';;') or '(1)' in raw:
        return True
    return False

def run(ifpath):
    with open(ifpath, 'rb') as istream, open(ifpath + '.utf8', 'w') as ostream:
        for i, word, phonemes in parse_cmu(istream):
            print(i, word, phonemes.split(' '))
            ostream.write('|'.join([word, phonemes]) + '\n')

if __name__ == '__main__':
    run(sys.argv[1])
