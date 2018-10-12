#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides.py

def nww(a, b):
    """Oblicza i zwraca najmniejsząż wspólną wielokrotność"""

def euklides(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)

def main(args):
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))
    print(euklides(a, b))
    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
