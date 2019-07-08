#!/usr/bin/env python3

import sys
from punsy import log, trie

LOG = log.get_logger('punsy')

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            yield [i, *line.decode('utf8').strip().split('|')]
        except UnicodeDecodeError as e:
            LOG.info(line)
            raise e

def run(ifpath):
    t = trie.Trie()
    words = {}
    with open(ifpath, 'rb') as istream:
        for i, word, phonemes in parse_cmu(istream):
            phonemes = phonemes.split(' ')
            LOG.info([i, word, phonemes])
            t.insert(phonemes, word)
            if i > 1000:
                break
    return t

if __name__ == '__main__':
    run(sys.argv[1])
