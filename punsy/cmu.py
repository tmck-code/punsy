#!/usr/bin/env python3

import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from punsy import log
from punsy.structs.suffix_trie import SuffixTrie

import tqdm

LOG = log.get_logger('punsy')

class CMU:
    def __init__(self, cmu_fpath):
        self.fpath = cmu_fpath
        self.phonemes = SuffixTrie()
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

    def pronunciation(self, word):
        return self.mapping[word]

    def rhymes_for(self, suffix, offset=3, max_depth=10):
        pron = self.mapping[suffix]
        LOG.info(f'Pronunciation is {pron}')
        LOG.info(f'Fetching rhymes, applying offset={offset}: {pron[offset:]}')
        ph = self.phonemes.rhymes_for_suffix(
            pron,
            offset=offset,
            max_depth=10
        )
        LOG.info(f'Rhymes for {ph}')
        return ph

    @staticmethod
    def parse(istream):
        for i, line in enumerate(istream):
            try:
                yield [i, *line.decode('utf8').strip().split('|')]
            except UnicodeDecodeError as e:
                LOG.info(line)
                raise e

    def pronunciation(self, word):
        return self.mapping[word.upper()]

    @staticmethod
    def __count_lines(fpath):
        i = 0
        with open(fpath) as istream:
            for i, _ in enumerate(istream):
                pass
            else:
                return i

class POC:
    def __init__(self, cmu_fpath):
        self.cmu = CMU(cmu_fpath)
        self.cmu.run()

    def poc(self, sentence, offset=1, max_depth=10):
        import random
        parts = sentence.split(' ')
        parts[-1] = random.choice(self.cmu.rhymes_for(
            parts[-1].upper(), offset=offset, max_depth=max_depth
        ))
        return ' '.join(parts)

if __name__ == '__main__':
    LOG.info(
        POC(sys.argv[1]).poc(
            sentence=sys.argv[2],
            offset=int(sys.argv[3])
        )
    )
