#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py


def main(args):
    suma = 0
    
    while suma <= 75:
        liczba = float(input("Podaj liczbę: "))
        suma = suma + liczba
    print("Suma liczb: ", suma)
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
