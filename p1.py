#!/usr/bin/env python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def p1(N):
    nums = set(range(0, N, 3)).union(range(0, N, 5))
    return sum(nums)

# ensure the test condition passes
assert p1(10) == 23

print(p1(1000))

