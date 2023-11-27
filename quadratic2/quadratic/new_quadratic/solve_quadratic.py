from bigfloat import *
zero = BigFloat('0')
four = BigFloat(4)
two = BigFloat(2)
one = BigFloat('1')


def solve_equation(a, b, c):
    if a != zero:
        return solve_quadratic(a, b, c)
    else:
        return solve_linear(b, c)


def solve_linear(b, c):
    if b == zero:
        if c == zero:
            return 'Любое число'
        else:
            return 'Корней нет'
    else:
        if c == zero:
            x1 = zero
            return f'{x1}'
        else:
            x1 = BigFloat.float(zero - c / b)
            return f'{x1}'


def solve_quadratic(a, b, c):
    d = (calculate_discr(a, b, c))
    if d > zero:
        sqrtd = BigFloat.sqrt(d)
        denominator = two * a
        numerator1 = (zero - b) - sqrtd
        numerator2 = (zero - b) + sqrtd
        x1 = numerator1 / denominator
        x2 = numerator2 / denominator
        if x1 > x2:
            x1, x2 = x2, x1
        x1 = BigFloat.float(x1)
        x2 = BigFloat.float(x2)
        return f'{x1}\n{x2}'
    elif d == zero:
        x = zero - b / (two * a)
        x = BigFloat.float(x)
        return f'{x}\n{x}'
    else:
        d = zero - d
        Re_num = zero - b
        denom = two * a
        sqrtd = BigFloat.sqrt(d)
        Re = Re_num / denom
        Im = sqrtd / denom
        if Im < zero:
            Im = zero - Im
        Re = BigFloat.float(Re)
        Im = BigFloat.float(Im)
        minus = '-'
        plus = '+'
        if Im == '0' or Im == '1':
            Im = ''
        if Re == '0':
            Re = ''
            plus = ''
        return f'{Re}{minus}{Im}i\n{Re}{plus}{Im}i'


def calculate_discr(a, b, c):
    return b * b - four * a * c
