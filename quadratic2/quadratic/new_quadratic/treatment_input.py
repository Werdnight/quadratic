import time
from math import *
from my_pattern_interpret.token_number import *
from my_pattern_interpret.token322 import *
from bigfloat import BigFloat
from my_pattern_interpret.interface import pos_zero
from treat_for_bigfloat import *
from solve_quadratic import *

class Input:

    def __init__(self, str):
        self.str = str
        self.prep = Preparation()

    def pattern_interpret(self):
        str_list = [x for x in self.str.split()]
        if len(str_list) != 3:
            return 'Неправильный ввод'
        arr = []
        for i in range(3):
            number = Tokenizer_NUMBER()
            val = number.interpret(str_list[i], pos_zero)
            str_list[i] = val.type
            arr += [val.value]
        if token_error in str_list:
            return 'Неправильный ввод'
        if token_nan in str_list:
            return 'nan\nnan'
        if token_inf in str_list:
            return 'nan\nnan'
        a, b, c = BigFloat(arr[0]), BigFloat(arr[1]), BigFloat(arr[2])
        # return a, b, c
        return solve_equation(a, b, c)
    
# f = Input(input())
# start = time.time()
# print(f.pattern_interpret())
# a, b, c = f.pattern_interpret()
# four = BigFloat(4)
# end = time.time()
# print(a * b)
# print('время: {}'.format(end-start))


