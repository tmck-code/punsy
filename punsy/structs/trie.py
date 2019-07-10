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

class Trie(object):
    '''
    A Trie class which implements insert, contains, and has_prefix methods.
    Currently with ZERO dependencies.
    '''

    def __init__(self, value=None, data=None):
        self.value = value
        self.children = dict()
        self.final = False
        self.data = data

    def contains(self, word):
        return self.__contains__(word)

    def has_prefix(self, word):
        try:
            return not self[word].final
        except (KeyError, IndexError):
            return False

    def insert(self, word, data=None):
        value, *string = word
        self.value = value

        try:
            # Recurse down
            self.children[string[0]].insert(string, data)
        except KeyError:
            # Create a new node if one doesn't exist
            n = Trie()
            self.children[string[0]] = n
            n.insert(string, data)
        # We have reached the end of the word
        except IndexError:
            self.final = True
            self.data = data
            LOG.info(f'Inserted {self.value} -> {self.data}')

    def __repr__(self):
        return f'{self.value} ({self.data}) -> {self.children}'

    def __contains__(self, value):
        try:
            return self[value].final
        except (KeyError, IndexError):
            return False

    def __getitem__(self, word):
        curr, *remain = word

        if curr != self.value:
            raise KeyError
        elif remain:
            return self.children[remain[0]].__getitem__(remain)
        return self

    def _get(self, word, insert=False):
        pass

if __name__ == '__main__':
    from IPython import embed
    print(__doc__)
    embed()

