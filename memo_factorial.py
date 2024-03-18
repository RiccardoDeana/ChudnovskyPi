from decimal import Decimal

factorial_dict = {0: Decimal(1),
                  1: Decimal(1),
                  2: Decimal(2),
                  3: Decimal(6),
                  'max': 3}


def memo_factorial(n):
    if n <= factorial_dict['max']:
        return factorial_dict[n]
    for i in range(factorial_dict['max'] + 1, n + 1):
        factorial_dict[i] = i * memo_factorial(i - 1)
    factorial_dict['max'] = n
    return factorial_dict[n]


if __name__ == '__main__':
    print(memo_factorial(10000))
