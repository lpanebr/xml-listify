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
def main() :
    parser = argparse.ArgumentParser(description='Transforma lista identada por tabs em lista XML.')
    parser.add_argument('-filename',help='Caminho para o arquivo que contém apenas a lista.', required=True)
    args = parser.parse_args()
    filename = args.filename
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
        r.text=lines[0]
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
    listf=etree.Element('list')
    listf.attrib['list-type']='simple'
    content = []
    with open(filepath,'r') as f:
        for line in f:
            content.append(re.sub(r'^<p>(\t*)(.+)</p>$', r'\1<p>\2</p>', line.rstrip())) # move tabs to start of line and get rid of trailling emty chars.
    e=etree.SubElement(listf,'list-item') #Create element for the first item
    e.text=content[0]
    parse_file(content[1:],listf)
    output=etree.tostring(listf, pretty_print=True, with_tail=True, method="xml") #Convert tree to XML
    print(unescape(output))
if __name__ == '__main__':
    main()