# punsy

A rhyming pun generator for Python

## Initial POC

> The POC takes in a sentence, picks out the last word, finds a random rhyming match and inserts it in place.
> E.g. `"Napoleon Dynamite" -> "Napoleon VEGEMITE"`

You build the docker image and run the POC with

```bash
make poc
```

Or, if you wish, use `make shell` to build the image and enter a BASH shell. Then, you can use the `punsy/cmu.py` command with the following format:

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
2019-07-24 15:07:38,576 punsy.punsy INFO Napoleon VEGEMITE
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

### Hall of Fame

As time passes, this will hopefully fill with some legitimately funny examples! Until then, we have these :)

| command | output |
|---------|--------|
| 'Adventure Time' | "Adventure PART-TIME" |
| 'A Good Day To Die Hard' | "A Good Day To Die AVANT-GARDE" |
| 'The Rolling Stones' | "The Rolling CLONES" |
