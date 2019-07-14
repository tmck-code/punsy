import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from punsy.structs.trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.words = {
            'NONE': ['N', 'AH1', 'N'],
            'NAAN': ['N', 'AH1', 'N'],
            'ONCE': ['W', 'AH1', 'N', 'S'],
            'PUN':  ['P', 'AH1', 'N'],
        }
        self.trie = Trie()
        for word, pronunciation in self.words.items():
            self.trie.insert(pronunciation, word)

    def test_insert_suffixes(self):
        words = [
            'cat',
            'bat',
            'catinthehat',
            'rat',
        ]
        struct = Trie(key_reversed=True)
        for word in words:
            struct.insert(word)


        result = struct['at']
        self.assertEqual(set('a'), result.value)
        self.assertEqual(['c', 'b', 'h', 'r'], list(result.children.keys()))
        # cat, bat & rat are all 'final'
        self.assertTrue(result.children['c'].final)
        self.assertTrue(result.children['b'].final)
        self.assertTrue(result.children['r'].final)
        # h should contain 'catinthehat'
        # self.assertFalse(result.children['h'].final)
        # print(result.children['h']['e']['h'])

    def testInsert(self):
        self.assertEqual({'NONE', 'NAAN'}, self.trie['N', 'AH1', 'N'].data)
        self.assertEqual({'ONCE'}, self.trie['W', 'AH1', 'N', 'S'].data)
        self.assertEqual({'PUN'}, self.trie['P', 'AH1', 'N'].data)

    def testGetItem(self):
        trie = Trie()
        trie.insert('A', 123)
        self.assertEqual({123}, trie['A'].data)
        self.assertTrue('A' in trie['A'].value)

