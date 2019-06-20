#!/usr/bin/env python3

import random
import sys
from nltk.corpus.reader import cmudict

def run(ifpath):
    with open(ifpath, 'r') as istream:
        parsed = cmudict.read_cmudict_block(istream)
    print(parsed)

if __name__ == '__main__':
    run(sys.argv[1])
