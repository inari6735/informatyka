#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py

def silnia_it(n):
    """
    n! = 1* ... * n
    """
    
    wynik = 1
    for i in range(n):
        wynik *= i + 1
    return wynik

def main(args):
    n = int(input("wprowadź liczbę: ")) # wielokrotne przypisanie
    print("{}! silnia wynosi {}".
            format(n, silnia_it(n)))
    silnia_it(n) # wywołanie funkcji
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
