from treatment_input import *
from pytest import *
import time
import random
import tqdm

print('lol')


def main(str_input: str):
    d = Input(str_input)
    return d.pattern_interpret()


print(main(input()))


# for _ in tqdm.trange(100):
#     a = random.uniform(-1000, 1000)
#     b = random.uniform(-1000, 1000)
#     c = random.uniform(-1000, 1000)
#     str_input = str(a) + ' ' + str(b) + ' ' + str(c)
#     print(f'{str_input}\n{main(str_input)}')
#
#
# for _ in tqdm.trange(15):
#     a = random.uniform(-1000, 1000)
#     a_e = random.randint(-1000, 1000)
#     b = random.uniform(-1000, 1000)
#     b_e = random.randint(-1000, 1000)
#     c = random.uniform(-1000, 1000)
#     c_e = random.randint(-1000, 1000)
#     str_input = str(a) + 'e' + str(a_e) + ' ' + str(b) + 'e' + str(b_e) + ' ' + str(c) + 'e' + str(c_e)
#     print(f'{str_input}\n{main(str_input)}')


# start_time = time.time()
# d = Input(input())
# print(d.pattern_interpret())
# end = time.time()
# print("--- %s seconds ---" % (time.time() - start_time))
