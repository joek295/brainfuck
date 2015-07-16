#!/usr/bin/env python

# take a string, output brainfuck code to print that string.

import sys
from collections import Counter

try:
    string = sys.argv[1]
except IndexError:
    print "Fatal Error: Brainfuck expected a source file."
    sys.exit(1)
    
try:
    with open(string,"r") as srcfile:
        string = srcfile.read()
except IOError:
    pass
codes = [ord(c) for c in string]

def bfify(codes):
    c = Counter(codes)
    sorted_codes = []
    for i in c.most_common():
        sorted_codes.append(i[0])
    source = ">"
    prevcode = 0
    change = ""
    for i in sorted_codes:
        codediff = (max(i,prevcode) - min(i,prevcode))
        # if we would make a saving by copy and alter, rather than writing from scratch, do so...
        alter = "<[->+>+<<]>>[-<<+>>]"
        if i > prevcode:
            alter += "<" + "+"*codediff + ">"
        elif i < prevcode:
            alter += "<" + "-"*codediff + ">"
        tenth = i/10
        new = ">" + "+"*10 + "[<" + "+" * tenth + ">-]<" + "+" * (i - 10*tenth) + ">"
        prevcode = i
        if len(new) < len(alter):
            source += new 
        else:
            source += alter
    source += "<"
    for i in codes:
        if sorted_codes.index(i) < len(sorted_codes)/2:
            if sorted_codes.index(prevcode) <= sorted_codes.index(i):
                move = (sorted_codes.index(i) - sorted_codes.index(prevcode))*">" + "."
            elif (sorted_codes.index(prevcode) - sorted_codes.index(i)) < sorted_codes.index(i):
                move = (sorted_codes.index(prevcode) - sorted_codes.index(i))*"<" + "."
            else:
                move = "[<]>" + ">"*sorted_codes.index(i) + "."
        else:
            if sorted_codes.index(prevcode) >= sorted_codes.index(i):
                move = (sorted_codes.index(prevcode) - sorted_codes.index(i))*"<" + "."
            elif (sorted_codes.index(i) - sorted_codes.index(prevcode)) < len(sorted_codes) - sorted_codes.index(i):
                move = (sorted_codes.index(i) - sorted_codes.index(prevcode))*">" + "."
            else:
                move = "[>]<" + "<"*(len(sorted_codes) -  sorted_codes.index(i) - 1) + "."
        source += move
        prevcode = i
    cleansource(source)

def cleansource(source):
    cleansource = ""
    last = ""
    for i in source:
        if i == "<" and last == ">":
            cleansource = cleansource [0:-1]
            last = ""
        elif i == ">" and last == "<":
            cleansource = cleansource [0:-1]
            last = ""
        else:
            cleansource += i
            last = i
    print cleansource

bfify(codes)
