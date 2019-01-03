#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  search.py


def main(args):
    i = 0
    x = 7
    tb = [4, 5, 2, 3, 7, 8, 9]
    n = len(tb)
    
    if i < n:
        for i in range(n):
            if tb[i] == x:
                print("Znaleziono")
            else:
                i += 1
                print("Nie ma")
    else:
        print("Nie znaleziono")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
