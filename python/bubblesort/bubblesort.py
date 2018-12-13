#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bubblesort.py

def main(args):
    x = True
    tb = [2, 3, 5, 6, 10, 9, 4]
    ltb = len(tb)-1
    while ltb > 0 and x:
        x = False
        for i in range(ltb):
            if tb[i] > tb[i+1]:
                x = True
                d = tb[i]
                tb[i] = tb[i+1]
                tb[i+1] = d
    print(tb)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
