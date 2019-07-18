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
        trie = Trie(key_reversed=True)
        for word in words:
            trie.insert(word)

        result = trie['at']
        self.assertEqual(set('a'), result.value)
        self.assertEqual(['c', 'b', 'h', 'r'], list(result.children.keys()))
        # cat, bat & rat are all 'final'
        self.assertTrue(result.children['c'].final)
        self.assertTrue(result.children['b'].final)
        self.assertTrue(result.children['r'].final)
        # h should contain 'catinthehat'
        self.assertFalse(result.children['h'].final)
        self.assertTrue(trie['catinthehat'].final)

    def testInsert(self):
        trie = Trie(key_reversed=True)
        words = {
            'NONE': ['N', 'AH1', 'N'],
            'NAAN': ['N', 'AH1', 'N'],
            'ONCE': ['W', 'AH1', 'N', 'S'],
            'PUN':  ['P', 'AH1', 'N'],
        }
        for word, pronunciation in words.items():
            trie.insert(pronunciation, word)
        self.assertEqual({'NONE', 'NAAN'}, trie['N', 'AH1', 'N'].data, trie['N', 'AH1', 'N'].data - {'NONE', 'NAAN'})
        self.assertEqual({'ONCE'}, trie['W', 'AH1', 'N', 'S'].data)
        self.assertEqual({'PUN'}, trie['P', 'AH1', 'N'].data)

    def testGetItem(self):
        trie = Trie(key_reversed=True)
        trie.insert('A', 123)
        self.assertEqual({123}, trie['A'].data)
        self.assertTrue('A' in trie['A'].value)

