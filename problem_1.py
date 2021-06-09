# PROBLEM 1
# MULTIPLES OF 3 AND 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# source - https://projecteuler.net/problem=1


def get_sum_of_multiples_of_3_or_5(range_max):
    sum = 0
    for i in range(3, range_max):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


# TEST

assert  get_sum_of_multiples_of_3_or_5(10) == 23

# ANSWER

print(get_sum_of_multiples_of_3_or_5(1000))
