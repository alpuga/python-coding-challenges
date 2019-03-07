'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def largest_prime_factor(n):
    # Declare smallest prime
    prime = 2

    '''
    if number is divisible by 2 (the smallest prime number),
    divide that number by the prime, in this case 2. Each time a
    number is not divisible by a number add 1 to it and check for
    divisibility. Once a number is found divide it by that number.
    Continue to do it until the number is one and that will be
    the largest prime factor.
    '''
    while n != 1:
        if n % prime == 0:
            n = n / prime
        else:
            prime += 1

    print(prime)


largest_prime_factor(13195)  # test
