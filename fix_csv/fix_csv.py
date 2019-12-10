'''
- take file names as arguments
- open the first file, add to an array splitting on pipe
- open the second file, read from array (generator?) and write to file using csv
'''

import csv
import sys
import argparse


def list_from_file(filename, delimiter):
    with open(filename) as pipe_file:
        lines = [
            line.rstrip().split(delimiter)
            for line in pipe_file
        ]
        return lines


def csv_from_generator(generator, filename, in_quote):
    quote_char = in_quote if in_quote is not None else "'"
    with open(filename, 'w') as csv_file:
        file_writer = csv.writer(
            csv_file, delimiter=',', quotechar=f'{quote_char}')
        for line in generator:
            file_writer.writerow(line)
    return


def fix_csv(*args):
    # original file = args[0]
    # new file = args[1]
    print(args[0])
    de_piped = list_from_csv(args[0])
    for line in de_piped:
        print(line)
    csv_from_generator(de_piped, args[1], )


if __name__ == '__main__':
    print(sys.argv)
    fix_csv(sys.argv[1], sys.argv[2])
