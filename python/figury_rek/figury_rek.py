#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  turtle.py

import turtle as t

def potega_re():
    if warunek brzegowy
    `   return

def figura(bok, kat, ile):
    for i in range(ile):
        t.forward(bok)
        t.right(kat)

def figura_rek(bok, kat, ile):
    t.forward(bok)
    t.right(kat)
    if ile > 0:
        figura_rek(bok, kat, ile - 1)

def main(args):
    t.setup(800, 600)
    t.color('blue', 'red')
    t.begin_fill()
    t.speed(0)
    
    figura_rek(100, 10r, 100)
    
    t.end_fill()
    t.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
