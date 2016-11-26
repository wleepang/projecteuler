#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import sys

def primes(start=0):
    N = start
    while True:
        if N > 1:
            for n in range(2, N):
                if (N % n) == 0:
                    break
            else:
                yield N
        N += 1


# get a set of the first 1000 prime numbers
PRIMES = set([])
for i, p in enumerate(primes()):
    if i < 1000:
        PRIMES.add(p)
    else:
        break

def factorize(n, start = 0):
    for p in primes(start):
        if n % p == 0:
            break
    
    # print(n, p, file=sys.stderr)

    r = n // p
    factors = [p]

    if r in PRIMES:
        factors.extend([r])
    else:
        factors.extend(factorize(r, p))

    return factors

assert factorize(13195) == [5,7,13,29]

print(factorize(600851475143))

