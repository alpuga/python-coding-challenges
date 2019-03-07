'''
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1
and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum
of the even-valued terms.
'''


def fibo_even_sum(term):
    # Declare variables
    sum = 0
    current = 1
    previous = 1
    i = 0
    j = 0
    list = []

    # Calculate the fib numbers and append them to list.
    while i < term:
        if current == 1:
            list.append(1)
        current += previous
        previous = current - previous
        list.append(current)
        i += 1

    # Check to see if the fib number is even. If so add to sum.
    while j < len(list):
        if list[j] % 2 == 0:
            sum += list[j]
        j += 1

    print(sum)


fibo_even_sum(43)
