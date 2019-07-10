#!/usr/bin/env python3

import sys
from structs.trie import Trie
import json

from tqdm import tqdm
import log

LOG = log.get_logger('punsy')

def run(ifpath):
    nlines = __file_len(ifpath)
    with open(ifpath, 'rb') as istream:
        t, mapping = parse_cmu_file(istream, nlines)
    return t, mapping

def parse_cmu(istream):
    for i, line in enumerate(istream):
        try:
            yield [i, *line.decode('utf8').strip().split('|')]
        except UnicodeDecodeError as e:
            LOG.warning(line)
            raise e

def parse_cmu_file(istream, nlines):
    t = Trie()
    mapping = {}
    with tqdm(total=nlines) as pbar:
        for i, word, phonemes in parse_cmu(istream):
            phoneme_seq = phonemes.split(' ')
            t.insert(''.join(phoneme_seq), word)
            mapping[word] = phoneme_seq
            pbar.update(1)
    return t, mapping

def __file_len(fpath):
    with open(fpath) as istream:
        for i, _ in enumerate(istream):
            pass
    return i + 1

if __name__ == '__main__':
    sentence = '! searched for god, but found none'
    t, mapping = run(sys.argv[1])

