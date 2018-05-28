#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)
    # print("Wylosowano:", liczba)
    for i in range(3):
        print("Próba", i + 1)
        odp = input("Podaj liczbę od 1 do 10: ")
        print("Wybrałeś liczbę", odp)

        if liczba == int(odp):
            print("Zgadłeś!")
            break  # przerwanie działania pętli
        elif i == 3:
            print("Wylosowano:", liczba)
        else:
            print("No niestety")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
