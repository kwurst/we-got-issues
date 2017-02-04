# git-twiddler

A tool to generate an activity for students learning git and GitHub.


## twiddle.py

`python twiddle.py [--max=M] N FILE`

Twiddles N words in FILE. If --max is given, maximum M words per line.
Modifies FILE in place. Generates FILE.twiddles.yaml that lists the location and
twiddle of each word twiddled. Generates FILE.originals.yaml that lists the
location and original word for each word twiddled.

For example

```
$ python twiddle.py 2 file
```

This generates file.twiddles.yaml

```
$ cat file.twiddles.yaml
12, 24: dba
14, 1: asd
```

and file.originals.yaml

```
$ cat file.originals.yaml
12, 24: bad
14, 1: sad
```
