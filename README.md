# git-twiddler

`python twiddle.py P FILE`

Scrambles random words in FILE. Each alphabetic word has a probability of P to
be scrambled. Generates the following files:

- file.twiddled: The same as file with randomly selected words scrambled.
- file.key.yaml: For each word scrambled, the line, position and the word.
- file.report.yaml: For each word scrambled, the line, position and the
  scrambled word.

# Example

```
$ python twiddle.py .1 file
```

Generates `file.twiddled` with the same content as `file` except that each
alphabetic word is scrambled with a probability of 10% (.1). This command
also generates `file.report.yaml`

```
$ cat file.report.yaml
12,24: dba
14,1: asd
```

and `file.key.yaml`

```
$ cat file.originals.yaml
12,24: bad
14,1: sad
```
