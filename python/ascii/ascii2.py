#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ascii2.py
def prostokat1(x, y):
    for i in range(y):
        for j in range(x):
            if j == 0 or j == y - 1:
                print("#", end='')
            else:
                print(" ")    
        print()    

    
    
    
def main(args):
    x = int(input("X: "))
    y = int(input("Y: "))
    prostokat1(x,y)
    print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
