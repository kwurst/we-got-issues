# we-got-issues

Programmatically add issues to a GitHub repository from a stream.

[Create an issue API documentation for GitHub](https://developer.github.com/v3/issues/#create-an-issue)

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

*Note: Due to GitHub API rate limits, this will take 3 seconds per issue to report.
The user will be given a time estimate and the chance to continue or abort.*

Dependencies:
- pyGithub - for GitHub API access
- pyYAML - for reading YAML-based incident file
- tqdm - for progress bar

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
