#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ascii.py


def main(args):
    cm = int(input("Ile cm: "))
    
    print("   ___  ")
    print("  / | \ ")
    print(" |     | ")
    print("  \   / ")
    for i in range(cm):
        print("  |   | ")
    print(" /     \ ")
    print("|   |   | ")
    print(" \ / \ / ")
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
