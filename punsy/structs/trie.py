#!/usr/bin/env python3
'''
A python implementation of the Trie data structure.

    https://en.wikipedia.org/wiki/Trie

The Trie is a memory-optimised data store for strings. It stores strings using a
k-ary tree structure (a tree in which each node has up to `k` children)

e.g. to store the words `car` and `cat`

c - a -|- r
       \- t

Usage:

t = Trie()  # create a trie

t.insert('cat')                   # insert a word into the trie
'cat' in t,     t.contains('cat') # check if the trie contains a word
t['cat'],       t.get('cat')      # retrieve a node from the trie
t,              print(t)          # print the contents of the trie
'''

from punsy import log

LOG = log.get_logger('trie')

class SuffixTrie:

    @staticmethod
    def collect_child_data(node):
        results = []
        for key, child in node.children.items():
            if not child.final:
                return SuffixTrie.collect_child_data(child)
            else:
                results.append(child.value)
        return results

class Trie(object):
    '''
    A Trie class which implements insert, contains, and has_prefix methods.
    Currently with ZERO dependencies.
    '''

    def __init__(self, value='', data='', key_reversed=False):
        self.value = set(value)
        self.children = dict()
        self.final = False
        self.data = set(data)
        self.key_reversed = key_reversed

    def has_suffix(self, word):
        try:
            self[word]
        except KeyError:
            return False
        return True

    def insert(self, word, data=None):
        if self.key_reversed:
            word = list(reversed(word))
        self._insert(word, data)

    def _insert(self, word, data=None):
        value, *string = word
        self.value.add(value)

        try:
            # Recurse down
            self.children[string[0]]._insert(string, data)
        except KeyError:
            # Create a new node if one doesn't exist
            n = Trie()
            self.children[string[0]] = n
            n._insert(string, data)
        # We have reached the end of the word
        except IndexError:
            self.final = True
            if data:
                self.data.add(data)
            LOG.debug(f'Assigning data -> {data}')

    def __repr__(self):
        return f'{self.value} ({self.data}) -> {self.children}'

    def __contains__(self, value):
        try:
            return self[value].final
        except (KeyError, IndexError):
            return False

    def __getitem__(self, word):
        if self.key_reversed:
            word = list(reversed(word))
        return self._getitem(word)

    def _getitem(self, word):
        print(word)
        curr, *remain = word

        if curr not in self.value:
            LOG.warn(f'{self.value}, {self.children.keys()}')
            raise KeyError
        if remain:
            print(remain, self.children)
            return self.children[remain[0]]._getitem(remain)
        return self

if __name__ == '__main__':
    from IPython import embed
    print(__doc__)
    embed()

