#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Nowak_liniowe.py

import random

def main(args):
    n = int(input("Podaj liczbę: "))
    tab = [0, 1, 2, 3, 4]
    i = 0
    tab[n] = szuk
    
    while tab[i] == szuk:
        if i < n:
            print("Element znaleziony")
            return 0
        print("Element nieznaleziony")
    else:
        i = i + 1
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
