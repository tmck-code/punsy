import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from punsy.structs.trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.words = {
            'NONE': ['N', 'AH1', 'N'],
            'ONCE': ['W', 'AH1', 'N', 'S'],
            'NAAN': ['N', 'AH1', 'N'],
            'PUN': ['P', 'AH1', 'N'],
        }
        self.trie = Trie()
        for word, pronunciation in self.words.items():
            self.trie.insert(pronunciation, word)

    def testInsert(self):
        self.assertEqual({'NONE', 'NAAN'}, self.trie['N', 'AH1', 'N'].data)
        self.assertEqual({'ONCE'}, self.trie['W', 'AH1', 'N', 'S'].data)
        self.assertEqual({'PUN'}, self.trie['P', 'AH1', 'N'].data)

    def testGetItem(self):
        trie = Trie()
        trie.insert('A', 123)
        print(trie['A'])
        self.assertEqual(123, trie['A'].value)

