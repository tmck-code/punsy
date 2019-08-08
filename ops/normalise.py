#!/usr/bin/env python3

import sys, re

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            entry = line.decode('ISO-8859-1').strip().split(' ' * 2)
            if not should_skip(entry):
                yield entry
        except UnicodeDecodeError as e:
            print(line)
            raise e

def should_skip(entry):
    skip = False
    if entry[0].startswith(';;') or re.match(r'(\d)', entry[0]):
        print(f'Skipping non-word or multiple definition: {entry}')
        skip = True
    if not entry[0][0].isalpha():
        print(f'Skipping probable non-word: {entry}')
        skip = True
    elif len(entry) != 2:
        print(f'Skipping empty entry: {entry}')
        skip = True
    return skip

def run(ifpath, ofpath):
    with open(ifpath, 'rb') as istream, open(ofpath, 'w') as ostream:
        for word, phonemes in parse_cmu(istream):
            ostream.write('|'.join([word, phonemes]) + '\n')

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])
