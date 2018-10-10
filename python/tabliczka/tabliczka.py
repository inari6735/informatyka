#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka.py

def tabliczka():
    for i in range(10):
        for j in range(10):
            print("{:>3} ".format((i+1)*(j+1)), end="")
        print()

def main(args):
    tabliczka()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
