#!/usr/bin/env python3
'''
A python implementation of the Trie data structure, specialising in searching by suffix.

    https://en.wikipedia.org/wiki/Trie

The Trie is a memory-optimised data store for strings. It stores strings using a
k-ary tree structure (a tree in which each node has up to `k` children)

e.g. to store the words `car`, `cat`, 'bar' and 'bat'

       /- t
  b - a - r
/
- c - a -|- r
       \- t

This trie has the ability to store and search words in reverse

e.g. to find words rhyming with '-at', the search is reversed to 'ta' and then
the child nodes 'b' (bat) and 'c' (cat) are returned.

t - a - b
      \ c

Usage:

t = Trie()  # create a trie

t.insert('cat')                   # insert a word into the trie
t.insert('cat', 'feline')         # insert a word and associated metadata into the trie
'cat' in t,     t.contains('cat') # check if the trie contains a word
t['cat'],       t.get('cat')      # retrieve a node from the trie
t,              print(t)          # print the contents of the trie
'''
from functools import wraps

import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from punsy import log

LOG = log.get_logger('trie')

class SuffixTrie:

    @staticmethod
    def collect_child_data(node, max_depth=10):
        results = set()
        LOG.info(f'at node: {node.value}, {node.data}, final: {node.final} - max depth: {max_depth}')
        for key, child in node.children.items():
            if max_depth > 0:
                LOG.info(f'recursing into {key}, {child} with max_depth {max_depth}')
                print(child.data)
                results |= child.data
                return SuffixTrie.collect_child_data(child, max_depth-1)
        return results

def reversible(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args[0].key_reversed:
            new_arg = list(reversed(args[1]))
            if len(args) == 3:
                return f(args[0], new_arg, args[2])
            else:
                return f(args[0], new_arg)
        return f(*args, **kwargs)
    return wrapper

class Trie(object):
    '''
    A Trie class which implements insert, contains, and has_prefix methods.
    Currently with ZERO dependencies.
    '''

    def __init__(self, value=None, data='', key_reversed=False):
        self.value = value
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

    @reversible
    def insert(self, word, data=None):
        current = self
        for i, letter in enumerate(word):
            try:
                current = current.children[letter]
            except KeyError:
                current.children[letter] = Trie()
                current = current.children[letter]
            current.value = letter
        current.final = True
        if data:
            current.data = set(data)

    @reversible
    def __getitem__(self, word):
        curr, *remain = word

        if curr not in self.children.keys():
            raise KeyError
        elif remain:
            return self.children[curr].__getitem__(remain)
        return self

    def asdict(self):
        d = {}
        for k in ['value', 'final', 'data']:
            if self.__dict__[k]:
                d[k] = self.__dict__[k]
        if self.children:
            d['children'] = {k: v.asdict() for k, v in self.children.items()}
        return d

    def __repr__(self):
        if self.value is None:
            return f'(root) -> {self.children}'
        else:
            return f'{self.value} ({self.data}) -> {self.children}'

    def __contains__(self, value):
        try:
            return self[value].final
        except (KeyError, IndexError):
            return False


if __name__ == '__main__':
    from IPython import embed
    print(__doc__)
    embed()

