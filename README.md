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

#### Running interactively

* Enter the docker container with

```bash
make build shell
```

Then, launch the `ipython` command and use as follows:

```python
root@fbcb68a6ce93:/home/punsy# ipython

Python 3.7.3 (default, May  8 2019, 05:31:59)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.6.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from punsy import cmu

In [2]: poc = cmu.POC('cmudict-0.7b.utf8')
125700it [00:03, 37833.83it/s]

In [3]: poc.poc('NAPOLEON DYNAMITE', offset=2)
2019-08-01 22:58:11,368 punsy.punsy INFO Pronunciation is ['D', 'AY1', 'N', 'AH0', 'M', 'AY2', 'T']
2019-08-01 22:58:11,369 punsy.punsy INFO Fetching rhymes, applying offset=2: ['N', 'AH0', 'M', 'AY2', 'T']
2019-08-01 22:58:11,369 punsy.punsy INFO Rhymes for ['DYNAMITE']
Out[4]: 'NAPOLEON DYNAMITE'
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
