import pathlib
import random
import re
import sys


def twiddle_file(p, filename):
    out_fn, report_fn, key_fn = get_filenames(filename)
    with open(filename) as in_f, open(out_fn, 'w') as out_f, open(report_fn, 'w') as report_f, open(key_fn, 'w') as key_f:
        for line, char, token, twiddled in generate_twiddled_tokens(p, in_f):
            if twiddled is not None:
                report_f.write(f'{line},{char}: {twiddled}\n')
                key_f.write(f'{line},{char}: {token}\n')
                out_f.write(f'{twiddled}')
            else:
                out_f.write(f'{token}')


def get_filenames(filename):
    out_filename = filename.with_name(filename.name + '.twiddled')
    report_filename = filename.with_name(filename.name + '.report.yaml')
    key_filename = filename.with_name(filename.name + '.key.yaml')
    return out_filename, report_filename, key_filename


def generate_twiddled_tokens(p, in_f):
    line_no = 1
    for line in in_f:
        char_no = 1
        for token in re.split(r'(\s+)', line):
            yield line_no, char_no, token, maybe_twiddle(p, token)
            char_no += len(token)
        line_no += 1


def maybe_twiddle(p, token):
    if random.random() >= p:
        return None
    if not is_twiddleable(token):
        return None
    return twiddle(token)


def is_twiddleable(string):
    if string is None:
        return False
    if re.fullmatch('(.)\1*', string) is not None:
        return False
    if re.fullmatch(r'[a-zA-Z]+', string) is None:
        return False
    return True


def twiddle(string):
    for i in range(100):
        string_list = list(string)
        random.shuffle(string_list)
        twiddled = ''.join(string_list)
        if twiddled != string:
            break
    if twiddled == string:
        return None
    return twiddled


if __name__ == '__main__':
    p = float(sys.argv[1])
    filename = pathlib.Path(sys.argv[2])
    twiddle_file(p, filename)
