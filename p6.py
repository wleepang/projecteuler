#!/usr/bin/env python

"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sq_diff(nums):
    ssq = sum([n**2 for n in nums])
    sqs = sum(nums)**2

    return sqs - ssq

assert sq_diff(range(1, 11)) == 2640

print(sq_diff(range(1, 101)))

