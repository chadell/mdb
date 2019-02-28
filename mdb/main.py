#!/usr/bin/env python3
#prova git
import argparse
from mdb.classes import MyClass


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', help='File to be processed',
                        required=True)
    return parser.parse_args()

def process_input(input_file):
    photos = {
        'H': [],
        'V': []
    }
    # import pdb; pdb.set_trace()
    id = 0
    for line in input_file:
        line = line.strip()
        fields = line.split(' ')
        # H 3 cat beach sun
        try:    
            photos[fields[0]].append([id, False ,[ fields[i+2] for i in range(0, int(fields[1])) ]])
            id += 1
        except:
            pass
        

    return photos


def logic(obj):
    return obj

def process_output(res, output):

    # 3
# 0
# 3
# 1 2
# The slideshow has 3 slides
# First slide contains photo 0
# Second slide contains photo 3
# Third slide contains photos 1 and 2
    output.write(str(len(res)) + "\n")
    for slides in res:
        for photo in slides:
            output.write(str(photo) + " ")
        output.write("\n")


def main():
    args = parse_arguments()
    photos = {}
    with open(args.filename, 'r') as input_file:
        photos = process_input(input_file)
    

    # crear slideshow
    slideshow = []
    for slide in photos['H']:
        slideshow.append((slide[0],))
        slide[1] = True

    i = 0
    while i < len(photos['V']):
        slideshow.append((photos['V'][i][0], photos['V'][i+1][0]))
        photos['V'][i][1] = True
        photos['V'][i+1][1] = True
        i += 2


    with open(args.filename + '.out', 'w') as output:
        process_output(slideshow, output)


if __name__ == '__main__':
    main()
