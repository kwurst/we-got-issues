from github import Github
from getpass import getpass
import yaml
import sys
import pathlib
import time


def main():
    repository_name = sys.argv[1]
    username = sys.argv[2]
    file_path = pathlib.Path(sys.argv[3])
    incidents_path = append_to_path(file_path, '.INCIDENTS')

    password = getpass()
    repository = Github(username, password).get_repo(repository_name)

    with open(incidents_path, 'r') as stream:
        incidents = yaml.load(stream)
        print('Due to GitHub API limits, this will take '+ str(len(incidents)/60) + ' minutes to complete.')
        response = input('Do you want to report these issues [y]/n? ')
        if len(response) == 0 or response[0].lower() == 'y':
            for incident in incidents:
                issue_title = 'Misspelled word in ' + str(file_path)
                issue_comment = 'On line number ' + str(incident['line']) + \
                                ', the misspelled word "' + str(incident['twiddled']) + \
                                '" was found.'
                repository.create_issue(issue_title, issue_comment)
                time.sleep(1)  # rate-limit the requests so we don't run afoul of GitHub's API limits
        else:
            print('No issues reported')


def append_to_path(file_path, string):
    return file_path.with_name(file_path.name + string)


if __name__ == '__main__':
    main()
