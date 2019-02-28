#!/usr/bin/env python3

import argparse


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
    
    photos['V'].sort(key=lambda x: len(x[2]), reverse=True)
    slides_verticals = []
    i = 0
    while i < len(photos['V']):
        slides_verticals.append(
            [
                # -1*(i+1
                (photos['V'][i][0], photos['V'][i+1][0]), 
                False, 
                list ( set(photos['V'][i][2] + photos['V'][i+1][2]) )
            ]
        )
        i += 2


    # crear slideshow
    slideshow = []
    # import pdb;pdb.set_trace()
    photos['H'].extend(slides_verticals)

    photos['H'].sort(key=lambda x: len(x[2]), reverse=True)
    count = 0

    for slide in photos['H']:
        if count%10 == 0:
            print(count)
        count += 1
        if slide[1] == True:
            continue
        inner_count = 0
        for slide_comp in photos['H']:
            if slide_comp[1] == True or slide[0] == slide_comp[0]:
                continue
            # 
            # inner_count to skip lasting iterations
            # 
            compare = 2
            interaccio = list( set(slide[2]) & set(slide_comp[2]))
            slide1 = list(set(slide[2]).difference(interaccio))
            slide2 = list(set(slide_comp[2]).difference(interaccio))
            interes = min (len(interaccio), len(slide1), len(slide2) )
            if interes > compare or inner_count == 100:
                # print interes

                # if inner_count == 100:
                #     compare = 4
                # if inner_count == 300:
                #     compare = 3
                # if inner_count == 500:
                #     compare = 2
                # if inner_count == 800:
                #     compare = 1

                inner_count = 0
                if isinstance(slide[0], tuple):
                    slideshow.append(slide[0])
                else:
                    slideshow.append((slide[0],))
                if isinstance(slide_comp[0], tuple):
                    slideshow.append(slide_comp[0])
                else:
                    slideshow.append((slide_comp[0],))
                slide[1] = True
                slide_comp[1] = True
                break
            inner_count += 1
    
    for slide in photos['H']:
        if slide[1] == True:
            continue
        if isinstance(slide[0], tuple):   
            slideshow.append(slide[0])
        else:
            slideshow.append((slide[0],))
        slide[1] = True           



    with open(args.filename + '.out', 'w') as output:
        process_output(slideshow, output)


if __name__ == '__main__':
    main()
