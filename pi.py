from memo_factorial import memo_factorial
from decimal import Decimal, localcontext


def pi_chudnovsky(digits: int) -> str:

    with localcontext() as ctx:
        ctx.prec = max(100, digits + 10)

        s = Decimal(0)
        sign = Decimal(1)
        last_s = ''

        for i in range(digits // 10 + 3):
            num = memo_factorial(6 * i) * (Decimal(545140134) * Decimal(i) + Decimal(13591409))
            den = memo_factorial(3 * i) * memo_factorial(i) ** Decimal(3) * Decimal(640320) ** Decimal(3 * i)
            s += sign * num / den

            if str(s)[-10:] == last_s:
                break
            last_s = str(s)[-10:]
            sign = -sign

        pi = Decimal(426880) * Decimal(10005) ** Decimal(0.5) / s
    return str(pi)[:digits+1]


if __name__ == '__main__':
    text_width = 100
    digits = 3000

    pi = pi_chudnovsky(digits)
    [print(pi[i:i + text_width]) for i in range(0, len(pi), text_width)]

