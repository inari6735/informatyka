#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zadanko.py


def main(args):
    imie = input("Podaj imię: ")
    nazwisko = input("Podaj nazwisko: ")
    
    print("Witaj " + imie + " " + nazwisko)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
