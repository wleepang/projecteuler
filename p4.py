#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

def palindromes(start, stop):
    for n in range(stop, start - 1, -1):
        for m in range(n, start - 1, -1):
            p = n * m
            # print(n, m, p, file=sys.stderr)

            if str(p) == str(p)[::-1]:
                #print(n, m, p, file=sys.stderr)
                yield p

# note for this problem it is important to 
# find the palindrome with the maximum value
# which is non-intuitively different from the
# palindrome product of the two largest numbers
assert max(palindromes(1, 99)) == 9009

print(max(palindromes(100, 999)))

