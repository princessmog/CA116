#!/usr/bin/env python3

import sys
args = sys.argv[1:]

s = input()

while s != "end":
   i = 0
   while i < len(s):
      if s[i:i + len(args[0])] == args[0]:
         print(s)
         i = len(s)
      i = i + 1
   s = input()
