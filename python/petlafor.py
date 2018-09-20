#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petlafor.py


def main(args):
    
    start = int(input("Od: "))
    stop = int(input("Do: "))
    
    while start >= stop: # nieskończona pętla
        start = int(input("Od: "))
        stop = int(input("Do: "))
        
    
    for liczba in range(start, stop): #dzielenie modulo % przez 2 daje 0 albo 1
        if liczba % 2 == 0:
            print(liczba)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
