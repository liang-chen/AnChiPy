
# -*- coding: utf-8 -*-

"""anchipy.anchipy: provides entry point main()."""

__version__ = "0.1.2"

import os
import sys
from math import ceil
from pkg_resources import resource_filename
from PyPDF2 import PdfFileReader,PdfFileMerger
from globalv import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import inch


def read_utf8_file(filename):
    """
    Read file contentsq as utf8 characters
    
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
    Locate words in paragraph
    """
    
    n = len(uni_words);
    ll = []
    pl = []

    ### set word locations
    curi = tot_margin + normal_font_size ##increase y-coord
    curp = page
    
    for i in range(len(uni_words)):
        if curi > img_height - tot_margin:
            curi = tot_margin + normal_font_size
            curj -= col_width
        
        if curj < tot_margin:
            curp += 1
            curj = img_width - tot_margin - col_width

        ll.append((curj, curi))
        pl.append(curp)
        curi += normal_font_size

    return ll,pl,curj

def add_border(pdf):
    """
    Add top, bottom, left and right borders to the current doc
    """
    pdf.setStrokeColorRGB(255,0,0)
    
    ### add horizontal borders:
    #outter
    pdf.setLineWidth(outter_border_width)
    i = outter_border_margin
    j1 = i
    j2 = img_width - j1 - outter_border_width/2
    pdf.line(j1,i,j2,i)

    i = img_height - outter_border_margin - outter_border_width/2
    pdf.line(j1,i,j2,i)
    
    #inner
    pdf.setLineWidth(inner_border_width)
    i = outter_border_margin + outter_border_width + inner_border_margin
    j1 = i
    j2 = img_width - j1 - inner_border_width
    pdf.line(j1,i,j2,i)

    i = img_height - outter_border_margin - outter_border_width - inner_border_margin - inner_border_width
    pdf.line(j1,i,j2,i)

    ### add vertical borders
    #outter
    pdf.setLineWidth(outter_border_width)
    j = outter_border_margin
    i1 = j
    i2 = img_height - i1 - outter_border_width/2
    pdf.line(j,i1,j,i2)

    j = img_width - outter_border_margin - outter_border_width/2
    pdf.line(j,i1,j,i2)

    #inner
    pdf.setLineWidth(inner_border_width)
    j = outter_border_margin + outter_border_width + inner_border_margin
    i1 = j
    i2 = img_height - i1 - inner_border_width
    pdf.line(j,i1,j,i2)

    j = img_width - j - inner_border_width
    pdf.line(j,i1,j,i2)

def init_pdf():
    """
    Initialize one pdf page
    """
    
    pdfmetrics.registerFont(TTFont('MyFont', resource_filename(__name__,'font.ttf')))
    
    pdf = canvas.Canvas('anchipy_formatted.pdf')
    pdf.setFont('MyFont' , normal_font_size)
    pdf.setPageSize((img_width, img_height))
    add_border(pdf)
    
    ###background
    #pdf.drawImage(resource_filename(__name__,'image.png'), 0, 0)
    return pdf

def page_merge(pdf):
    """
    Merge new page to the existing pages

    :param pdf: new pdf page
    """
    
    merger = PdfFileMerger()
    if os.path.isfile('anchipy_formatted.pdf'):
        merger.append(PdfFileReader(file('anchipy_formatted.pdf','rb')))
    pdf.save()
    merger.append(PdfFileReader(file('anchipy_formatted.pdf','rb')))
    merger.write("anchipy_formatted.pdf")

def render_pdf_paragraph(pdf, P, loc_list, page_list, curp):
    """
    Render a paragraph
    """
    
    for i in range(len(P)):
        if page_list[i] != curp and curp == 0:
            pdf.save()
            curp = page_list[i]
            pdf = init_pdf()
        elif page_list[i] != curp and curp != 0:
            ### another page
            page_merge(pdf)
            curp = page_list[i]
            pdf = init_pdf()
    
        ### fading effect
        #pdf.setFillColorRGB(0,0,0,0.5 + float(img_height - loc_list[i][1])/2/img_height)

        pdf.drawString(loc_list[i][0], img_height - loc_list[i][1], P[i])
    
        if loc_list[i][1] == tot_margin + normal_font_size:
            ### draw vertical line
            pdf.setStrokeColorRGB(255,0,0)
            pdf.line(loc_list[i][0]-udl_margin, tot_margin, loc_list[i][0]-udl_margin, img_height-tot_margin)
    return pdf, curp


def main():
    """
    Main function
    """
    
    ### read words from text file
    filename = sys.argv[1]
    uni_word_lines = [unicode(line, 'utf8') for line in read_utf8_file(filename)]
    
    ### initialization
    if os.path.isfile('anchipy_formatted.pdf'):
        os.remove('anchipy_formatted.pdf')
    pdf = init_pdf()
    
    ### current page
    curp = 0
    
    ### current horizontal position
    curj = img_width - tot_margin - col_width
    
    ### render text onto svg
    for uni_words in uni_word_lines: 
        ll,pl,curj = locate_paragraph_words(uni_words, curj, curp)
        curj -= col_width #paragraph turn
        pdf, curp= render_pdf_paragraph(pdf, uni_words, ll, pl, curp)
        
    page_merge(pdf)

