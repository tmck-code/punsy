#!/usr/bin/env python3

import random
import sys
from nltk.corpus.reader import cmudict

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            yield [i, *line.decode('ISO-8859-1').strip().split('  ')]
        except UnicodeDecodeError as e:
            print(line)
            raise e

def run(ifpath):
    with open(ifpath, 'rb') as istream:
        for i, word, phonemes in parse_cmu(istream):
            print(i, word, phonemes)

if __name__ == '__main__':
    run(sys.argv[1])
