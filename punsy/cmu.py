#!/usr/bin/env python3

import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from punsy import log
from punsy.structs.trie import Trie, SuffixTrie

import tqdm

LOG = log.get_logger('punsy')

class CMU:
    def __init__(self, cmu_fpath):
        self.fpath = cmu_fpath
        self.phonemes = Trie(key_reversed=True)
        self.mapping = {}
        self.n_lines = CMU.__count_lines(self.fpath)

    def run(self):
        with open(self.fpath, 'rb') as istream:
            with tqdm.tqdm(total=self.n_lines) as pbar:
                for i, word, phonemes in CMU.parse(istream):
                    phonemes = phonemes.split(' ')
                    self.phonemes.insert(phonemes, word)
                    self.mapping[word] = phonemes
                    pbar.update(1)

    @staticmethod
    def parse(istream):
        for i, line in enumerate(istream):
            try:
                yield [i, *line.decode('utf8').strip().split('|')]
            except UnicodeDecodeError as e:
                LOG.info(line)
                raise e

    @staticmethod
    def __count_lines(fpath):
        i = 0
        with open(fpath) as istream:
            for i, _ in enumerate(istream):
                pass
            else:
                return i

def collect_rhymes(node):
    if node.final == True:
        return node.data
    else:
        results = set()
        for k, n in node.children.items():
            results += collect_rhymes(n)
        return results


if __name__ == '__main__':
    sentence = 'I searched for God but found none'

    cmu = CMU(sys.argv[1])
    cmu.run()
    ph = cmu.mapping['NONE']
    print('NONE', ph)
    rh = cmu.phonemes[ph]
    print(rh.value, rh.data)

    print('rhymes ending with "ing"')
    print(cmu.phonemes.value, cmu.phonemes.value, cmu.phonemes.children.keys())
    rh = cmu.phonemes['ING']
    print('ING', ph, rh.data)
    print(collect_rhymes(rh))

    print(SuffixTrie.collect_child_data(cmu.phonemes['ING'], 11))
