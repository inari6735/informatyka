#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bubblesort2.py

import random

def main(args):
	tb = []
	for k in range(10):
		tb.append(random.randint(0, 100))
	n = len(tb) - 1

	for j in range(n):
		for i in range(n):
			if tb[i] > tb[i+1]:
				tb[i], tb[i+1] = tb[i+1], tb[i]

	print(tb)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
