#!/usr/bin/env python

import sys
import math

num_test_cases = 0
test_cases = []

for line in sys.stdin:
    line = line.strip()
    if not num_test_cases:
        num_test_cases = int(line)
        continue
    test_cases.append(map(int, line.split()))

for case in test_cases:
    upper = int(math.ceil(math.sqrt(case[1]))) + 1
    primes = range(2, case[1] + 1)
    i = 0
    len_primes = len(primes)
    p_index = i

    while p_index < upper and p_index < len_primes:
        i = p_index
        p = primes[p_index]
        i += p
        while i < len_primes:
            primes[i] = -1
            i += p

        p_index += 1
        while p_index < len_primes and primes[p_index] == -1:
            p_index += 1

    primes = filter(lambda prime: prime >= case[0] and prime <= case[1], primes)
    for prime in primes:
        print prime
    print





