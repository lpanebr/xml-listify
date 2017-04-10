#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import itertools
import re
from xml.sax.saxutils import escape, unescape
try:
    #Python 2.7+
    from lxml import etree
except ImportError:
    try:
        #Python 2.5+
        from xml.etree.cElementTree import etree 
    except ImportError:
        print("No LXML") 
# original code modified from: http://stackoverflow.com/a/12164449/372722
dots = None
def main() :
    global dots
    parser = argparse.ArgumentParser(description='Transforma lista identada por tabs em lista XML.')
    parser.add_argument('-filename',help='Caminho para o arquivo que contém apenas a lista.', required=True)
    parser.add_argument('-dots', nargs='?', const=0, help='Normaliza a quantidade de pontos. Omita para ou use 0 (zero) para preservar original.')
    args = parser.parse_args()
    filename = args.filename
    dots = args.dots
    if dots is None:
        dots = 0
    listify(filename)
def parse_file(lines,tree,depth=0):
    if(len(lines)<=0): #We are done here
        return
    if(len(lines[0].strip())<=0): #Skip empty lines
        parse_file(lines[1:],tree,depth) #Recursive call
    newDepth=sum(1 for i in itertools.takewhile(lambda c: c=='\t', lines[0]))
    #print("LOC: %d, ND: %d, D: %d"%(loc,newDepth,depth))
    if(newDepth>depth): #Create a list-item with a list and a list-item in it
        c=tree
        if(tree.tag=='list-item'):
            c=tree.getparent()
        e=etree.SubElement(c,'list-item')
        ee=etree.SubElement(e,'list')
        ee.attrib['list-type']='simple'
        r=etree.SubElement(ee,'list-item')
        r.text=remove_control_characters(lines[0])
        parse_file(lines[1:],r,newDepth) #Recursive call
    elif(depth>newDepth): #Move back to parent root and add the current child there
        p=tree.getparent()
        for i in range(depth-newDepth): #Move back to Original Parent
            if(p.tag=='list'):
                p=p.getparent().getparent()
        ee=etree.SubElement(p,'list-item')
        ee.text=lines[0]
        parse_file(lines[1:],ee,newDepth) #Recursive call
    elif(depth==newDepth):#Add item to the current item's parent
        e=etree.SubElement(tree.getparent(),'list-item')
        e.text=lines[0]
        parse_file(lines[1:],e,depth) #Recursive call
def listify(filepath):
    global dots
    listf=etree.Element('list')
    listf.attrib['list-type']='simple'
    content = []
    with open(filepath,'r') as f:
        for line in f:
            # fix: trailling emty chars.
            line = line.rstrip()
            # fix: …
            line = re.sub(r'…', r'...', line)
            # fix: bad chars
            line = re.sub(r'–', r'-', line)
            line = re.sub(r'’', r'\'', line)
            # fix: <italic>... 
            line = re.sub(r'(\.*)<italic>(\.+) *', r'\1\2<italic>', line)
            # Normalize dots
            if dots > 0:
                dots = int(dots)
                line = re.sub(r'\.{2,}', '.'*dots, line)
            # move tabs to start of line and get
            line = re.sub(r'^<p>(\t*)(.+)</p>$', r'\1<p>\2</p>', line)
            content.append(line) 
    e=etree.SubElement(listf,'list-item') #Create element for the first item
    e.text=content[0]
    parse_file(content[1:],listf)
    output=etree.tostring(listf, pretty_print=True, with_tail=True, method="xml") #Convert tree to XML
    print(unescape(output))
def remove_control_characters(html):
    def str_to_int(s, default, base=10):
        if int(s, base) < 0x10000:
            return unichr(int(s, base))
        return default
    html = re.sub(ur"&#(\d+);?", lambda c: str_to_int(c.group(1), c.group(0)), html)
    html = re.sub(ur"&#[xX]([0-9a-fA-F]+);?", lambda c: str_to_int(c.group(1), c.group(0), base=16), html)
    html = re.sub(ur"[\x00-\x08\x0b\x0e-\x1f\x7f]", "", html)
    return html
if __name__ == '__main__':
    main()