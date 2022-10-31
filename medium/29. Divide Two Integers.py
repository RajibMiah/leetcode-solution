import sys

"""
time complixty O(log n) and space complxity constant

"""


def divide(dividend, divisor):

    d = abs(dividend)
    div = abs(divisor)
    result = 0

    while d >= div:
        tmp = div
        mul = 1

        while d >= tmp:
            d -= tmp
            result += mul
            mul += mul
            tmp += tmp

    if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):

        result = -result

    return min(2147483647, max(-2147483648, result))


print(divide(10, 3))  # output 3


"""
approch two using bit manupulation 
"""


def divide(dividend, divisor):

    if (dividend == 1 << 31 and divisor == -1):
        return sys.maxsize

    sign = True if (dividend >= 0) == (divisor >= 0) else False

    dividend = abs(dividend)
    divisor = abs(divisor)
    result = 0
    while(dividend - divisor >= 0):
        count = 0
        while(dividend - (divisor << 1 << count) > 0):
            count += 1

        result += 1 << count
        dividend -= divisor << count
    return result if sign else -result


print(divide(10, 3))
