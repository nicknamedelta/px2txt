#!/usr/bin/env python3
# pylint: disable=missing-docstring
import math
from PIL import Image

def img_convert(ref, width, height):
    # define shades and range
    shades = [ '.', ':', ';', 'i', 'r']
    s_range = 255 / len(shades)

    # convert pixels in shades
    pixels = []
    for y in range(0, height):
        line = []
        for x in range(0, width):
            point = ref.getpixel((x, y))
            pixel = math.ceil(point[0] + point[1] + point[2] / 3)

            shade = ''
            if (pixel >= s_range * 4):
                shade = shades[0]
            elif (pixel >= s_range * 3):
                shade = shades[1]
            elif (pixel >= s_range * 2):
                shade = shades[2]
            elif (pixel >= s_range * 1):
                shade = shades[3]
            else:
                shade = shades[4]
            
            line.append(shade)
        pixels.append(''.join(line) + '\n')
    write_file(''.join(pixels))

    # remove the comment below to see the result in the terminal
    # print(''.join(pixels))

def write_file(text):
    # open new file in append mode
    f = open('cnv_img.txt', 'w')

    # write and close file
    f.write(text)
    f.close()

def main():
    # get img real path of user
    img_path = input('(≧∀≦)ゞ - Tell to me what\'s the path to image: ')
    img = Image.open(img_path)

    # resize img to 100px x 100px
    img_ref = img.resize((100, 100))

    # resize image and override the file
    img_convert(img_ref, img_ref.width, img_ref.height)
    print('(∩^o^)⊃━☆゜.* - It\'s over, the result are in cnv_img.txt')

main()