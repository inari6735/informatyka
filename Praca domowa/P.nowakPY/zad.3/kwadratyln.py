#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kwadratyln.py
#  


def main(args):
	liczba = int(input("Podaj liczbę naturalną: "))
	for liczby in range(liczba + 1):
		wynik = liczby ** 2
		print(wynik)	
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
