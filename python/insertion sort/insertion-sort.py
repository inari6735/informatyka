#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  insertion-sort.py


def main(args):
    A = [5, 6, 8, 9]
    n = len(A)
    
    for i in range(1, n): 
  
        key = A[i] 
        j = i-1
        while j >= 0 and key < A[j] : 
                arr[j+1] = A[j] 
                j -= 1
        A[j+1] = key 
    
    print(A)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
