#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  selectionsort.py

def main(args):
    tab = [5, 3, 4, 2, 7, 8]
    n = len(tab) - 1
    
    for i in range(n):
        k = i
        j = k + 1
        for j in range(n):
            if tab[j] < tab[k]:
                k = j
    
    print(tab)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
