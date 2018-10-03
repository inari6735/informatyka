#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sumacyfr.py

def sumuj_cyfry1(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = liczba // 10
    return suma
def main(args):
    liczba = int(input("Podaj liczbę 2-cyfrową: "))
    print("Suma: ", sumuj_cyfry(liczba))
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
