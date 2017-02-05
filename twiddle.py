import pathlib
import random
import re
import sys


def twiddle_file(p, in_filename, out_filename, report_filename, key_filename):
    line_number = 1
    start_character = 0
    with open(in_filename) as in_file, open(report_filename, 'w') as report_file, open(out_filename, 'w') as out_file, open(key_filename, 'w') as key_file:
        for line in in_file:
            for token in re.split(r'(\s+)', line):
                if not token.isspace() and token:
                    if random.random() < p:
                        try:
                            twiddled = twiddle(token)
                            report_file.write(str(line_number) + " " + twiddled + '\n')
                            key_file.write(str(line_number) + " " + token + '\n')
                            token = twiddled
                        except Exception:
                            print("Couldn't twiddle '" + token + "'")
                out_file.write(token)
            line_number += 1


def twiddle(string):
    for i in range(100):
        string_list = list(string)
        random.shuffle(string_list)
        twiddled = ''.join(string_list)
        if twiddled != string:
            break
    if twiddled == string:
        raise Exception('Untwittleable?')
    return twiddled


if __name__ == '__main__':
    p = float(sys.argv[1])
    in_filename = pathlib.Path(sys.argv[2])
    out_filename = in_filename.with_name(in_filename.name + '.twiddled.yaml')
    report_filename = in_filename.with_name(in_filename.name + '.report.yaml')
    key_filename = in_filename.with_name(in_filename.name + '.key.yaml')
    twiddle_file(p, in_filename, out_filename, report_filename, key_filename)
