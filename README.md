# git-twiddler

# Twiddle
`python twiddle.py P FILE`

Generates a FILE.TWIDDLED with the contents of FILE with random words twiddled
(scrambled). Each word is twiddled with probability P. Generates two files:

- FILE.TWIDDLED: The same as file with randomly words twiddled.
- FILE.INCIDENTS: Contains information about each twiddled word.

## Example

```
$ python twiddle.py .1 LICENSE
```

Generates `LICENSE.TWIDDLED` with the same content as `LICENSE` except that each
alphabetic word is twiddled with a probability of 10% (.1). Also generates
`LICENSE.INCIDENTS`.

```
$ cat LICENSE.INCIDENTS
- {line: 502, character: 10, twiddled: lbeiaaalv, string: available}
- {line: 614, character: 61, twiddled: dovedirp, string: provided}
```

# Report
`python report.py GITHUB-NAMESPACE/REPOSITORY-NAME GITHUB-USERNAME FILE`

The user will be asked to enter the password for GITHUB-USERNAME.

For each line in the file FILE.INCIDENTS, generate an issue in the GitHub issue tracker
for the repository GITHUB-NAMESPACE/REPOSITORY-NAME.
The author of the issue will be GITHUB-USERNAME.

The issue created will consist of the line number, and the twiddled word:

```
Misspelled word in FILE
    On line number ###, the misspelled word "xxxxxxxx" was found.
```

*Note: Due to GitHub API rate limits, this will take 1 second per issue to report.
The user will be given a time estimate and the chance to continue or abort.*

Dependencies:
- pyGithub
- pyYAML

## Example

```
$ python report.py kwurst/git-twiddler kwurst LICENSE
```

```
$ cat LICENSE.INCIDENTS
- {line: 502, character: 10, twiddled: lbeiaaalv, string: available}
- {line: 614, character: 61, twiddled: dovedirp, string: provided}
```

Generates two issues in the repository kwurst/git-twiddler with the author kwurst:

```
Misspelled word in LICENSE
    On line 502, the misspelled word "lbeiaaalv" was found.

Misspelled word in LICENSE
    On line 614, the misspelled word "dovedirp" was found.
```

