# coding=utf-8
'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largest_palindrome_product(n):
    # Calculate the upper and lower limits
    max_num = int(('9' * n))
    min_num = (max_num + 1) / 10

    # Create list to store palindrome numbers
    # Set i and j for while loops to multiply numbers within the limits
    products = []
    i = max_num
    j = max_num

    # Loop through all possible product possibilities
    # If product is the same as product reverse, push to list
    # Finally print out max of the products list
    while i >= min_num:
        j = max_num
        while j >= min_num:
            product = i * j
            product_reverse = int(str(product)[::-1])

            if product == product_reverse:
                products.append(product)
            j -= 1
        i -= 1

    print(max(products))


largest_palindrome_product(3)
