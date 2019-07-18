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

from punsy import log

LOG = log.get_logger('trie')

class SuffixTrie:

    @staticmethod
    def collect_child_data(node, max_depth=1):
        results = set()
        LOG.info(f'at node: {node.value}, {node.data}, final: {node.final} - max depth: {max_depth}')
        for key, child in node.children.items():
            if max_depth > 0:
                LOG.info(f'recursing into {key}, {child} with max_depth {max_depth}')
                results |= child.data
                results |= SuffixTrie.collect_child_data(child, max_depth-1)
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

    @reversible
    def insert(self, word, data=None):
        value, *string = word
        self.value.add(value)

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
            if data:
                self.data.add(data)

    def __repr__(self):
        return f'{self.value} ({self.data}) -> {self.children}'

    def __contains__(self, value):
        try:
            return self[value].final
        except (KeyError, IndexError):
            return False

    @reversible
    def __getitem__(self, word):
        curr, *remain = word

        if curr not in self.value:
            LOG.warn(f'{self.value}, {self.children.keys()}')
            raise KeyError
        if remain:
            return self.children[remain[0]].__getitem__(remain)
        return self

if __name__ == '__main__':
    from IPython import embed
    print(__doc__)
    embed()

