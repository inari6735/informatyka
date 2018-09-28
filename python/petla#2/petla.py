#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py
#
# DANE WEJŚCIOWE:
# zmienne start i stop podane przez uzytkownika(przedział)
# DANE WYJŚCIOWE:
# liczby naturalne z <start, stop>


def main(args):
    
    start = int(input("Start: "))
    stop = int(input("Stop: "))
    
    for i in range(start, stop + 1):
        print(i, " ", end = '')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
