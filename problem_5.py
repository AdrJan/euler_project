# PROBLEM 5
# SMALLEST MULTIPLE
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#
# source - https://projecteuler.net/problem=5

# TODO: fix bug with importing problem_3 - now it's printing everything from imported file

from typing import Counter
from problem_3 import get_prime_factors


def get_lcm(val_1, val_2):
    prime_factors_1 = Counter(get_prime_factors(val_1))
    prime_factors_2 = Counter(get_prime_factors(val_2))

    prime_factors = prime_factors_1 | prime_factors_2

    lcm = 1
    for factor in prime_factors:
        lcm *= factor ** prime_factors[factor]

    return lcm

    
def get_smallest_multiple(max_val):
    lcm = 1
    for val in range(2, max_val + 1):
        lcm = get_lcm(lcm, val)
    return lcm


assert get_smallest_multiple(10) == 2520

# ANSWER

print(get_smallest_multiple(20))
