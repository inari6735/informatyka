#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lparzyste3.py
#

def main(args):
	for liczby in range(10, 100):
		if liczby % 6 == 0:
			print(liczby)
	
	return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
