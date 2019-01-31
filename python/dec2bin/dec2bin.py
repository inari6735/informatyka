#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dec2bin.py


def main(args):
    a = float(input("Podaj liczbę: "))
    b = 0
    tab = []
    while a == 0:
        b = a % 2
        tab.append(b)
        a = a / 2
    print(tab)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
