import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from punsy.structs.trie import Trie

class TestTrie(unittest.TestCase):

    def test_insert_suffixes(self):
        words = [
            'cat',
            'bat',
            'catinthehat',
            'rat',
        ]
        trie = Trie()
        for word in words:
            trie.insert(word)

        for word in words:
            self.assertTrue(trie[word].final)

    def test_insert(self):
        trie = Trie()
        words = {
            'NONE': ['N', 'AH1', 'N'],
            'NAAN': ['N', 'AH1', 'N'],
            'ONCE': ['W', 'AH1', 'N', 'S'],
            'PUN':  ['P', 'AH1', 'N'],
        }
        for word, pronunciation in words.items():
            trie.insert(pronunciation, word)
        self.assertEqual(['NONE', 'NAAN'], trie[['N', 'AH1', 'N']].data, trie)
        self.assertEqual(['ONCE'], trie['W', 'AH1', 'N', 'S'].data)
        self.assertEqual(['PUN'], trie['P', 'AH1', 'N'].data)

    def testGetItem(self):
        trie = Trie(key_reversed=True)
        trie.insert('A', 123)
        self.assertEqual([123], trie['A'].data)
        self.assertTrue('A' in trie['A'].value)

