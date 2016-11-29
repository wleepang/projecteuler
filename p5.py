#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys
from functools import reduce

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

def factorize(n, start=0):
    PRIMES = set([])
    for p in primes():
        if p <= n:
            PRIMES.add(p)
        else:
            break

    for p in primes(start):
        if n % p == 0:
            break

    r = n // p
    factors = [p]
    
    if r > 1:
        if r in PRIMES:
            factors.extend([r])
        else:
            factors.extend(factorize(r, p))

    return factors

def min_divisible(nums, verbose=False):
    pcount = {}
    for i in nums:
        p_i = factorize(i)
    
        if verbose:
            print(i, p_i)

        for p_u in set(p_i):
            if pcount.get(p_u) is None:
                pcount.update({p_u: p_i.count(p_u)})
            else:
                pcount[p_u] = max(pcount[p_u], p_i.count(p_u))

    factors = [int(k)**v for k, v in pcount.items()]
    N = reduce(lambda x, y: x*y, factors)

    if verbose:
        print(pcount)
        print(factors)
        print(N)

    return N

assert min_divisible(range(2, 11)) == 2520

min_divisible(range(2, 21), verbose=True)

