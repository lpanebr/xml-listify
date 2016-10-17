#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import itertools
import re

# original code modified from: http://stackoverflow.com/a/12164449/372722

def main() :

    parser = argparse.ArgumentParser(description='Transforma lista identada por tabs em lista XML.')
    parser.add_argument('-filename',
                                            help='Caminho para o arquivo que contém apenas a lista.',
                                            required=True)
    args = parser.parse_args()
    filename = args.filename

    listify(filename)


def listify(filepath):
    depth = 0
    print '<list list-type="simple">'*(depth+1)
    for line in open(filepath):
        # line = line.rstrip()
        line = re.sub(r'^<p>(\t*)(.+)</p>$', r'\1<p>\2</p>', line.rstrip())
        newDepth = sum(1 for i in itertools.takewhile(lambda c: c=='\t', line))
        if newDepth > depth:
            print '\t'*newDepth+'<list-item><list list-type="simple">'*(newDepth-depth),
        elif depth > newDepth:
            print '\t'*newDepth+"</list></list-item>"*(depth-newDepth+1),
        print '\t'*newDepth+"<list-item>%s</list-item>" %(line.strip())
        depth = newDepth
    print "</list>"*(depth)


if __name__ == '__main__':
    main()