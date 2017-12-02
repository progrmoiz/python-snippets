#!/usr/bin/env python3

"""
File: formats.py
Various specialized string display formatting utilities.
Test me with canned self-test or command-line argumnets.
To do: add parans for negative money, and more feature.
"""


def commas(N):
    """
    Format positive integer-like N for display with
    commas between digits grouping: "XXX,YYY,ZZZ"
    """
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result


def commas1(N):
    """
    The more easiest way to format digits
    """
    return '{:,}'.format(N)


def money(N, numwidth=0, currency="$"):
    """
    Format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: "$ -xxx,yyy.zz".
    numwidth=0 for no space padding, currency='' to omit symbol,
    and non-ASCII for others (e.g., pound=u'\xA3' or u'\u00A3').
    """
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%2f' % N)[-2:]
    number = '%s%s.%s' % (sign, whole, fract)
    return '%s%*s' % (currency, numwidth, number)

if __name__ == '__main__':
    def selftest():
        tests = 0, 1             # fails -1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))

        print("-" * 80)

        for test in tests:
            print(commas1(test))

        print("-" * 80)

        tests = 0, 1, -1, 1.23, 1., 1.2, 3.1341
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, (2 ** 32 + .2342)
        tests += 1.2324, 1.2, 0.2345
        tests += -1.242, -1.2, -15.2
        tests += -(2 ** 32), -(2 ** 32 + 0.2324)
        tests += 2 ** 100, -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))
