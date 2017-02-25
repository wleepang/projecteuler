#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

---

This is a brute force implementation.  It gets the job done in a reasonable amount of time
(approx, 5-10s)
"""

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

def nth_prime(N, dot_char='*', primes_per_dot=10, dots_per_line=80):
    PRIMES = primes()
    
    n_dots = 0
    n_primes = 0
    for n in range(N):
        p = PRIMES.__next__()
        n_primes += 1

        if (n_primes % primes_per_dot) == 0:
            print(dot_char, end='', flush=True)
            n_dots += 1

            if n_dots >= dots_per_line:
                print('', flush=True)
                n_dots = 0
    
    print('')
    print('-- done --')

    return p

if __name__ == "__main__":
    print('test case: find 6th prime (13)')
    P = nth_prime(6)
    print(P)
    assert P == 13

    print('objective: find 10_001th prime')
    P = nth_prime(10_001)
    print(P)

