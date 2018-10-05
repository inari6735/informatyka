#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ascii2.py

def prostokat1(x, y):
    for i in range(x):
        for j in range(y):
            print("#", end='')
        print()    
        
def prostokat2(x, y):
    for i in range(x):
        for j in range(y):
            if j == 0 or j == y - 1:
                print("#", end='')
            else:
                print(" ", end='')    
        print()

def choinka1(h, znak):
    
    for i in range(h):
        for j in range(i + 1):
            print(znak, end = '')
        print()
        
def choinka2(h, znak):
    
    for i in range(h):
        for j in range(h - i):
            print(znak, end = '')
        print()
    
    
def main(args):
    x = int(input("X: "))
    y = int(input("Y: "))
    h = int(input("Wysokość choinki: "))
    znak = input("Znak: ")
    prostokat1(x, y)
    prostokat2(x,y)
    choinka1(h, znak)
    choinka2(h, znak)
    print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
