#!/usr/bin/env python3

import sys
from structs.trie import Trie

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            yield [i, *line.decode('ISO-8859-1').strip().split('|')]
        except UnicodeDecodeError as e:
            print(line)
            raise e

def run(ifpath):
    t = Trie()
    with open(ifpath, 'rb') as istream:
        for i, word, phonemes in parse_cmu(istream):
            print(i, word, phonemes.split(' '))
            t.insert(''.join(phonemes.split(' ')), word)
    return t


if __name__ == '__main__':
    run(sys.argv[1])
