#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alf_mors.py

kod = {'a': '+-', 'ą': '+-+-',
           'b': '-+++',
           'c': '-+-+', 'ć': '-+-++', 'ch': '----',
           'd': '-++',
           'e': '+', 'ę': '++-++',
           'f': '++-+',
           'g': '--+',
           'h': '++++',
           'i': '++',
           'j': '+---',
           'k': '-+-',
           'l': '+-++', 'ł': '+-++-',
           'm': '--',
           'n': '-+',
           'ń': '--+--',
           'o': '---', 'ó': '---+',
           'p': '+--+',
           'q': '--+-',
           'r': '+-+',
           's': '+++', 'ś': '+++-+++',
           't': '-',
           'u': '++-',
           'v': '+++-',
           'w': '+--',
           'x': '-++-',
           'y': '-+--',
           'z': '--++', 'ź': '--+-', 'ż': '--++-+'}

def koduj():
    text = input("Wprowadź wyraz: ").lower()
    
    for litera in text:
        print(kod[litera], end='')

def dekoduj():
    text = []
    lit = ' '
    while lit > '':
        lit = input("Podaj kod Morse'a: ")
        text.append(lit)
    klucze = list(kod.values())
    litery = list(kod.keys())
    for i in text:
        print(litery[klucze.index(i)])

def main(args):
    dekoduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
