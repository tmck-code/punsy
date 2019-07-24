# punsy
A rhyming pun generator for Python

## An initial idea, and scope.

Scope is pretty important here, otherwise we'll never end up finishing a complete version, we can then add the future if we really need to.

Here were my initial thoughts on the problem

* Wowser, there are a lot of different ways make punsy.
  - ergo, we should start with the easiest pun and work from there.

## POC

> The POC takes in a sentence, picks out the last word, finds a random rhyming match and inserts it in place.

You can download and clean the CMU files using

```bash
make fetch
```

Then, you can use the `punsy/cmu.py` command with the following format:

```text
./punsy/cmu.py <cmu_file_path> <sentence> <offset>
```

An example run:

```text
./punsy/cmu.py cmudict-0.7b.utf8 'Napoleon Dynamite' 4

125700it [00:02, 56726.98it/s]
2019-07-24 15:07:38,575 punsy.punsy INFO Pronunciation is ['D', 'AY1', 'N', 'AH0', 'M', 'AY2', 'T']
2019-07-24 15:07:38,575 punsy.punsy INFO Fetching rhymes, applying offset=4: ['M', 'AY2', 'T']
2019-07-24 15:07:38,575 punsy.punsy INFO Rhymes for ['DOLOMITE', 'DYNAMITE', 'EPSOMITE', 'HASHEMITE', 'VEGEMITE']
2019-07-24 15:07:38,576 punsy.punsy INFO Punified! "Napoleon Dynamite" -> "Napoleon VEGEMITE"
```

### The Suffix trie

You can experiment with the suffix trie by running it directly with

```bash
./punsy/structs/suffix_trie.py
```

OR, the regular trie with

```bash
./punsy/structs/trie.py
```
