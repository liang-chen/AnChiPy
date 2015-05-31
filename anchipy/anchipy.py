
# -*- coding: utf-8 -*-

"""anchipy.anchipy: provides entry point main()."""

__version__ = "0.0.1"

from PIL import ImageFont, ImageDraw,Image
from jianfan import jtof
from glob import *
import sys
from math import ceil
from pkg_resources import resource_filename

def read_utf8_file(filename):
    with open(filename, 'rb') as f:
        return ''.join([ch.strip() for ch in f.read().split()])

def locate_words(uni_words):
    global font_size,img_height,udl_width,udl_margin
    global img_width #unset yet
    n = len(uni_words);
    ll = []
#    print n, " length of words"
    tot_len = n*font_size
    ncols = int(ceil(float(tot_len)/img_height)); 
    #set global image width
    img_width = ncols*(font_size+2*udl_margin+udl_width)
#    print ncols, img_width, img_height

    ##set word locations
    curi = 0 ##increase y-coord
    curj = img_width - font_size  ##decrease x-coord
    for i in range(len(uni_words)):
        if curi + font_size > img_height:
            curi = 0
            curj -= (font_size + 2*udl_margin + udl_width)
        ll.append((curj, curi))
        curi += font_size

    return ll

def render_whole_page(uni_words, loc_list):
    global font_size,img_height,img_width,udl_width,udl_margin
    if img_width == 0:
        return;
    im = Image.new('RGBA', (img_width, img_height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(resource_filename(__name__,'cwTeXQKaiZH-Medium.ttf'), size = font_size, encoding = "unic")
    for i in range(len(uni_words)):
        draw.text(loc_list[i], jtof(uni_words[i]),font=font,fill=(0,0,0,0))
        if(loc_list[i][1] == 0):
            ##draw red vertical line
            draw.line((loc_list[i][0]-udl_margin, 0, loc_list[i][0]-udl_margin, img_height),fill = (255,0,0,0), width = udl_width)
    im.save('anchipy_formatted.jpg','JPEG')

def main():
    filename = sys.argv[1]
    uni_words = unicode(read_utf8_file(filename), 'utf8')
    ll = locate_words(uni_words)
    render_whole_page(uni_words, ll)
   

if __name__ == '__main__':
  main()

