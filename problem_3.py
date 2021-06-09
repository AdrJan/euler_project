# PROBLEM 3
# LARGEST PRIME FACTOR
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#
# source - https://projecteuler.net/problem=3


def get_prime_factors(val):
    prime_factors = []
    divisor = 2
    while val > 1:
        if val % divisor == 0:
            prime_factors.append(divisor)
            val //= divisor
        else:
            divisor += 1

    return prime_factors


def get_max_prime_factor(val):
    return max(get_prime_factors(val))


# TEST

assert get_max_prime_factor(13195) == 29

# ANSWER

print(get_max_prime_factor(600851475143))
