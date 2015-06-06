
# -*- coding: utf-8 -*-

"""anchipy.anchipy: provides entry point main()."""

__version__ = "0.0.1"

from PIL import ImageFont, ImageDraw,Image
from jianfan import jtof
from glob import *
import sys
from PyPDF2 import PdfFileReader,PdfFileMerger
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
    ncols = int(ceil(float(tot_len)/float(img_height-2*tot_margin))); 
    #set global image width
    img_width = ncols*(font_size+2*udl_margin+udl_width) + 2*tot_margin
#    print ncols, img_width, img_height

    ##set word locations
    curi = tot_margin ##increase y-coord
    curj = img_width - tot_margin - font_size  ##decrease x-coord
    for i in range(len(uni_words)):
        if curi + font_size > img_height - tot_margin:
            curi = tot_margin
            curj -= (font_size + 2*udl_margin + udl_width)
        ll.append((curj, curi))
        curi += font_size

    return ll

def add_border(draw):
    #add horizontal ones:
    #outter
    i = outter_border_margin
    j1 = i
    j2 = img_width - j1 - outter_border_width/2
    draw.line((j1,i,j2,i),fill = (255,0,0,0), width = outter_border_width)

    i = img_height - outter_border_margin - outter_border_width/2
    draw.line((j1,i,j2,i),fill = (255,0,0,0), width = outter_border_width)
    
    #inner
    i = outter_border_margin + outter_border_width + inner_border_margin
    j1 = i
    j2 = img_width - j1 - inner_border_width
    draw.line((j1,i,j2,i),fill = (255,0,0,0), width = inner_border_width)

    i = img_height - outter_border_margin - outter_border_width - inner_border_margin - inner_border_width
    draw.line((j1,i,j2,i),fill = (255,0,0,0), width = inner_border_width)

    ##vertical ones
    #outter
    j = outter_border_margin
    i1 = j
    i2 = img_height - i1 - outter_border_width/2
    draw.line((j,i1,j,i2), fill = (255,0,0,0), width = outter_border_width)

    j = img_width - outter_border_margin - outter_border_width/2
    draw.line((j,i1,j,i2), fill = (255,0,0,0), width = outter_border_width)

    #inner
    j = outter_border_margin + outter_border_width + inner_border_margin
    i1 = j
    i2 = img_height - i1 - inner_border_width
    draw.line((j,i1,j,i2), fill = (255,0,0,0), width = inner_border_width)

    j = img_width - j - inner_border_width
    draw.line((j,i1,j,i2), fill = (255,0,0,0), width = inner_border_width)
    
def render_whole_page(uni_words, loc_list):
    global font_size,img_height,img_width,udl_width,udl_margin
    if img_width == 0:
        return;
    im = Image.new('RGB', (img_width, img_height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(resource_filename(__name__,'eduSong_Unicode.ttf'), size = font_size, encoding = "unic")
    for i in range(len(uni_words)):
        draw.text(loc_list[i], jtof(uni_words[i]),font=font,fill=(0,0,0,0))
        if loc_list[i][1] == tot_margin:
            ##draw red vertical line
            draw.line((loc_list[i][0]-udl_margin, tot_margin, loc_list[i][0]-udl_margin, img_height-tot_margin),fill = (255,0,0,0), width = udl_width)
    add_border(draw)
    im.save('temp.jpg','JPEG')
    im.save('temp.pdf')

    merger = PdfFileMerger()
    merger.append(PdfFileReader(file('temp.pdf','rb')))
    merger.append(PdfFileReader(file('anchipy_formatted.pdf','rb')))
    merger.write("anchipy_formatted.pdf")
    
def main():
    filename = sys.argv[1]
    uni_words = unicode(read_utf8_file(filename), 'utf8')
    ll = locate_words(uni_words)
    render_whole_page(uni_words, ll)
   

if __name__ == '__main__':
  main()

