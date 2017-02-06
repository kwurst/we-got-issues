import pathlib
import random
import re
import sys


def main():
    probability_word_is_twiddled = float(sys.argv[1])
    file_path = pathlib.Path(sys.argv[2])
    twiddled_path = append_to_path(file_path, '.TWIDDLED')
    incidents_path = append_to_path(file_path, '.INCIDENTS')
    lines = read_lines(file_path)
    tokens = tokenize_lines(lines)
    tokens = twiddle_random_words(probability_word_is_twiddled, tokens)
    with open(twiddled_path, 'w') as twiddled_file, open(incidents_path, 'w') as incidents_file:
        for t in tokens:
            if t.is_twiddled():
                string = t.get_twiddled()
                incidents_file.write(t.get_incident_string() + '\n')
            else:
                string = t.get_string()
            twiddled_file.write(string)


def append_to_path(file_path, string):
    return file_path.with_name(file_path.name + string)


def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line


def tokenize_lines(lines):
    for line_number, line in enumerate(lines, start=1):
        character_number = 1
        for string in re.split(r'(\s+)', line):
            yield Token(line_number, character_number, string)
            character_number += len(string)


def twiddle_random_words(probability_word_is_twiddled, tokens):
    for token in tokens:
        if token.is_tiddleable():
            if random.random() < probability_word_is_twiddled:
                token.try_to_twiddle()
        yield token


class Token:
    def __init__(self, line_number, character_number, string):
        self._line_number = line_number
        self._character_number = character_number
        self._string = string
        self._twiddled = None

    def is_tiddleable(self):
        if self._string is None:
            return False
        if re.fullmatch('(.)\1*', self._string) is not None:
            return False
        if re.fullmatch(r'[a-zA-Z]+', self._string) is None:
            return False
        return True

    def try_to_twiddle(self):
        for i in range(100):
            string_list = list(self._string)
            random.shuffle(string_list)
            self._twiddled = ''.join(string_list)
            if self._twiddled != self._string:
                break
        if self._twiddled == self._string:
            self._twiddled = None

    def is_twiddled(self):
        return self._twiddled is not None

    def get_string(self):
        return self._string

    def get_twiddled(self):
        return self._twiddled

    def get_incident_string(self):
        return f'- {{line: {self._line_number}, character: {self._character_number}, twiddled: {self._twiddled}, string: {self._string}}}'


if __name__ == '__main__':
    main()
