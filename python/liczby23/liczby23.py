#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby23.py

def liczby2():
    """
    Funkcja drukuje wszystkie liczby dwucyfrowe, w których cyfry nie powtarzają się. Funkcja zwraca ich liczbę. Wykluczone liczby: 11, 22, 33 itd.
    """
    suma = 0
    liczba = 0
    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                print("{}{} ".format(i, j), end="")
                suma = suma + 1
                print(suma)
    return suma


def main(args):
    print("Liczb 2-cyfrowych:", liczby2())
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
