#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py

def trojkat(a, b ,c):
    """
    Funkcja bada możliwość zbudowania trójkąta z trzech podanych boków
    Funkcja zwraca True jeżeli się da, False w przeciwnym wypadku 
    """
    
    if a + b > c and b + c > a and a + c > b:
        return True
    
    return False
    
    
def main(args):
    
    a = int(input('Długość boku a trójkąta: '))
    b = int(input('Długość boku b trójkąta: '))
    c = int(input('Długość boku c trójkąta: '))
    
    if trojkat(a,b,c):
        print("Powstanie")
    else:
        print("Nie powstanie")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
