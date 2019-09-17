#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  3liczby.py


def main(args):
    l = []
    
    for i in range(3):
        l.append(float(input()))
    if l[0] > l[1]:
        if l[0] > l[2]:
            największa = l[0]
        else:
            największa = l[2]
    elif l[1] > l[2]:
        największa = l[1]
    else:
        największa = l[2]
    print(największa)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
