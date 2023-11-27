from math import nan
import re
from mpmath import mpf, sqrt, mp

mp.dps = 100

two = mpf(2)
four = mpf(4)
zero = mpf(0)

def read_input():
    pattern = r'^\s*(-?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?)\s+(-?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?)\s+(-?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?)\s*$'
    pattern_nan = r'^\s*[-+]?nan\s[-+]?nan\s[-+]?nan\s*$'
    pattern_inf = r'^\s*[-+]?inf\s[-+]?inf\s[-+]?inf\s*$'
    coefficients = input()
    match = re.match(pattern, coefficients)
    match_nan = re.match(pattern_nan, coefficients)
    match_inf = re.match(pattern_inf, coefficients)
    if match:
        global a
        global b
        global c
        a, b, c = map(mpf, coefficients.split())
        return a, b, c
    else:
        return 0, 0, 1


def calculate_discr(a, b, c):
    return b**two - four*a*c

def solve_quadratic(a, b, c):
    d = mpf(calculate_discr(a, b, c))
    print(d)
    if d > zero:
        x1 = (-b + sqrt(d) / (two * a))
        x2 = (-b - sqrt(d) / (two * a))
        return x1, x2
    elif d == zero:
        x = -b / (two * a)
        return x
    else:
        d = -d
        Re = -b / (two * a)
        Im = sqrt(d) / (two * a)
        return f'{Re}-{Im}i\n{Re}+{Im}i'

def solve_linear(a, b, c):
    if b == zero:
        if c == zero:
            return 'любое число'
        else:
            return 'неправильный ввод'
    else:
        if c == zero:
            x1 = zero
            return x1
        else:
            x1 = -c / b
            return x1



def solve_equation(a, b, c):
    if a != zero:
        return solve_quadratic(a, b, c)
    else:
        return solve_linear(a, b, c)

def main():
    values_input = read_input()
    answer = solve_equation(*values_input)
    print(answer)
main()

l = [mpf(1), mpf(1), mpf(1)]
r = mp.polyroots(l)
print(r)