import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from punsy.structs.trie import Trie

class SuffixTrie:

    def __init__(self):
        self.trie = Trie()

    def insert(self, word, data):
        self.trie.insert(
            list(reversed(word)),
            data
        )

    def __getitem__(self, word):
        return self.trie.__getitem__(
            list(reversed(word))
        )

    def rhymes_for_suffix(self, word, offset=0, max_depth=10):
        return SuffixTrie._collect_child_data(
            self.__getitem__(word[offset:]),
            max_depth=max_depth,
            results=list()
        )

    @staticmethod
    def _collect_child_data(node, max_depth=10, results=list()):
        if node.final:
            results.extend(node.data)
        for key, child in node.children.items():
            if max_depth > 0:
                SuffixTrie._collect_child_data(child, max_depth-1, results)
        return results

