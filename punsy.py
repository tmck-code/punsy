#!/usr/bin/env python3

import random
import sys

sentence = sys.argv[1]

words = {
    'ahn': ['naan', 'none', 'nun']
}

def pattern_for_word(word, words):
    for pattern, matches in words.items():
        if any(el == word for el in matches):
            return pattern

pun = []
for word in sentence.split(' '):
    pattern = pattern_for_word(word, words)
    if pattern:
        pun.append(random.choice(words[pattern]))
    else:
        pun.append(word)
print(' '.join(pun))

        
