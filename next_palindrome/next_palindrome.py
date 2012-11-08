#!/usr/bin/env python
import sys

# spoj 5 - PALIN - The Next Palindrome

def is_palindrome(num):
    num = str(num)
    i, j = 0, len(num) - 1
    while i < j:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1
    return True

sys.stdin.readline() # skip first line
for line in sys.stdin:
    num = int(line.strip()) + 1
    while not is_palindrome(num):
        num += 1
    print num
