#!/usr/bin/env python3

import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from punsy import log
from punsy.structs.trie import Trie

import tqdm

LOG = log.get_logger('punsy')

class CMU:
    def __init__(self, cmu_fpath):
        self.fpath = cmu_fpath
        self.trie = Trie()
        self.mapping = {}
        self.n_lines = CMU.__count_lines(self.fpath)

    def run(self):
        with open(self.fpath, 'rb') as istream:
            with tqdm.tqdm(total=self.n_lines) as pbar:
                for _, word, phonemes in CMU.parse(istream):
                    phonemes = phonemes.split(' ')
                    self.trie.insert(phonemes, word)
                    LOG.info(f'inserted {phonemes}, {word}')
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

    def phonemes(self, word):
        try:
            return self.mapping[word]
        except KeyError:
            LOG.info(f'No phonemes found for {word}')
            return None

    def exact_rhymes(self, phonemes):
        return self.phonemes[phonemes]

    @staticmethod
    def __count_lines(fpath):
        i = 0
        with open(fpath) as istream:
            for i, _ in enumerate(istream):
                pass
            else:
                return i


if __name__ == '__main__':
    sentence = 'I searched for God but found none'

    cmu = CMU(sys.argv[1])
    cmu.run()
    ph = cmu.phonemes('NONE')
    print('NONE', ph)
    rh = cmu.exact_rhymes(ph)
    print(rh)
