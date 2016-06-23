
# -*- coding: utf-8 -*-

"""anchipy.anchipy: provides entry point main()."""

__version__ = "0.1.1"

import os
import sys
from math import ceil
from pkg_resources import resource_filename
from PIL import ImageFont, ImageDraw,Image
from PyPDF2 import PdfFileReader,PdfFileMerger
from globv import *


def read_utf8_file(filename):
    """
    Read file contents as utf8 characters
    
    :param filename: input file name
    :type filename: string
    :return: array of utf-8 characters
    :rtype: list
    """
    with open(filename, 'rb') as f:
        lines = f.readlines()
        return [''.join([ch.strip() for ch in line.split()]) for line in lines]

def locate_paragraph_words(uni_words, curj, page):
    """
    
    """
    global normal_font_size,img_height,img_width,udl_width,udl_margin,col_width,tot_margin
    n = len(uni_words);
    ll = []
    pl = []
    ##set word locations
    curi = tot_margin ##increase y-coord
    curp = page
    #curj = img_width - tot_margin - font_size  ##decrease x-coord
    for i in range(len(uni_words)):
        if curi + normal_font_size > img_height - tot_margin:
            curi = tot_margin
            curj -= col_width
        
        if curj < tot_margin:
            curp += 1
            curj = img_width - tot_margin - col_width

        ll.append((curj, curi))
        pl.append(curp)
        curi += normal_font_size
    
    return ll,pl,curj

def add_border(draw):
    """
    Add top, bottom, left and right borders to the current doc
    """
    
    #add horizontal ones:
    #outter
    global inner_border_margin, inner_border_width, outter_border_margin, outter_border_width, img_height, img_width
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
    
def init_image():
    """
    Initialize one page
    """
    global img_height,img_width
    im = Image.new('RGB', (img_width, img_height), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    add_border(draw)
    return im, draw

def new_page_merge(im):
    """
    Merge new page to the existing pages

    :param im: new page
    :type: PIL.image
    """
    im.save('temp.pdf',resolution = 200.0)
    merger = PdfFileMerger()
    merger.append(PdfFileReader(file('anchipy_formatted.pdf','rb')))
    merger.append(PdfFileReader(file('temp.pdf','rb')))
    merger.write("anchipy_formatted.pdf")
    os.remove('temp.pdf')

def render_paragraph(im, draw, P, loc_list, page_list, curp):
    global normal_font_size,img_height,img_width,udl_width,udl_margin
    font = ImageFont.truetype(resource_filename(__name__,'font.ttf'), size = normal_font_size, encoding = "unic")
    for i in range(len(P)):
        if page_list[i] != curp and curp == 0:
            im.save('anchipy_formatted.pdf', resolution = 200.0)
            curp = page_list[i]
            im, draw = init_image()
        elif page_list[i] != curp and curp != 0:
            #new page
            new_page_merge(im)
            curp = page_list[i]
            im, draw = init_image()
        
        draw.text(loc_list[i], P[i],font=font,fill=(0,0,0,0))#jtof(uni_words[i]),font=font,fill=(0,0,0,0))
        if loc_list[i][1] == tot_margin:
            ##draw red vertical line
            draw.line((loc_list[i][0]-udl_margin, tot_margin, loc_list[i][0]-udl_margin, img_height-tot_margin),fill = (255,0,0,0), width = udl_width)

    return im,draw,curp

def main():
    """
    Main function
    """
    filename = sys.argv[1]
    uni_word_lines = [unicode(line, 'utf8') for line in read_utf8_file(filename)]
    
    im, draw = init_image()
    global img_width,col_width
    curp = 0 #current page
    curj = img_width - tot_margin - col_width #current horizontal position
    for uni_words in uni_word_lines: 
        ll,pl,curj = locate_paragraph_words(uni_words, curj, curp)
        #print curj
        curj -= col_width #paragraph turn
        im, draw, curp = render_paragraph(im, draw, uni_words, ll, pl, curp)
    new_page_merge(im)
