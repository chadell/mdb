#!/usr/bin/env python3
import argparse
from mdb.classes import MyClass


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='File to be processed',
                        required=True)
    return parser.parse_args()

def process_input(line):
    line.strip()
    fields = line.split(',')
    obj = MyClass(
        name=fields[0],
        surname=fields[1]
    )
    return obj

def logic(obj):
    return obj

def process_output(res, output):
    output.write(res.__str__())

def main():
    args = parse_arguments()

    with open(args.filename, 'r') as input, \
         open('output.txt', 'w') as output:
        for line in input:
            obj = process_input(line)

            res = logic(obj)

            process_output(res, output)

if __name__ == '__main__':
    main()
