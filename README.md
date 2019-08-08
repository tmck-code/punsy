# punsy

A rhyming pun generator for Python

## Initial POC

> The POC takes in a sentence, picks out the last word, finds a random rhyming match and inserts it in place.
> E.g. `"Napoleon Dynamite" -> "Napoleon VEGEMITE"`

To install, run:
```
pip install punsy
```

You can then run punsy with:
```
punsy --sentence 'napoleon dynamite'
```

An example run:

```
 20:10:22 │ ☯ ~ punsy --sentence 'napoleon dynamite'
2019-08-09 00:55:24,851 punsy.punsy INFO Parsing & loading 125699 entries from CMU dictionary file
125700it [00:02, 58591.59it/s]
2019-08-09 00:55:27,005 punsy.punsy INFO Pronunciation of "DYNAMITE" is "D-AY1-N-AH0-M-AY2-T"
2019-08-09 00:55:27,005 punsy.punsy INFO Fetching rhymes, applying offset=2: "N-AH0-M-AY2-T"
2019-08-09 00:55:27,005 punsy.punsy INFO Rhymes for DYNAMITE: ['DYNAMITE']
2019-08-09 00:55:27,005 punsy.punsy INFO Generated pun for napoleon dynamite: napoleon DYNAMITE (DYNAMITE -> DYNAMITE)
2019-08-09 00:55:27,181 punsy.punsy INFO napoleon DYNAMITE
```

### Docker

You build the docker image and run the POC with

```bash
make poc
```

#### Running interactively

* Enter the docker container with

```bash
make build shell
```

Option 1: 

You can use the `punsy/cmu.py` command with the following format:

```text
./punsy/cmu.py <cmu_file_path> <sentence> <offset>
```

Option 2: ipython

Then, launch the `ipython` command and use as follows (output omitted):

```python
In [1]: from punsy import cmu
In [2]: poc = cmu.POC()
In [3]: poc.run('NAPOLEON DYNAMITE', offset=2)
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
