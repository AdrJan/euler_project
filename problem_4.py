# PROBLEM 4
# LARGEST PALINDROME PRODUCT
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# source - https://projecteuler.net/problem=4

def get_largest_palindrome(val_min, val_max):
    products = set()
    for i in range(val_min, val_max):
        for j in range(val_min, val_max):
            products.add(i * j)

    products = set([
        product for product 
        in products 
        if str(product)[::-1] == str(product)
        ])

    return max(products)


# TEST

assert get_largest_palindrome(10, 100) == 9009

# ANSWER

print(get_largest_palindrome(100, 1000))
