#!/usr/bin/env python

# Convert a string to ascii: useful for composing brainfuck...

import sys

target = sys.argv[1]

print [ord(c) for c in target]
