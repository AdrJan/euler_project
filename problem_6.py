# PROBLEM 6
# SUM SQUARE DIFFERENCE
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.
#
# source - https://projecteuler.net/problem=2


def get_sum_of_square(val):
    result = 0
    for num in range(1, val + 1):
        result += num ** 2
    return result


def get_square_of_sum(val):
    result = 0
    for num in range(1, val + 1):
        result += num
    return result ** 2


def get_sum_square_difference(val):
    return get_square_of_sum(val) - get_sum_of_square(val)


# TEST

assert get_sum_square_difference(10) == 2640

# RESULT

print(get_sum_square_difference(100))
