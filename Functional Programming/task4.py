from functools import reduce
from multiprocessing import Pool
import random
random.seed(10)

def square(x):
    for _ in range(100_000):
        x ** 2
    return x ** 2

def sum_of_squares(l, pool):
    filtered = list(filter(lambda x : not str(x).startswith('#'), l))
    cast_ints = list(map(int, filtered))

    squares = pool.map(square, cast_ints)

    return reduce(lambda x, y: x + y, squares)

if __name__ == "__main__":

    li = random.sample(range(1, 1001), 800)

    with Pool(8) as pool:

        print(sum_of_squares([0], pool))
        print(sum_of_squares([1], pool))
        print(sum_of_squares([1, 2, 3], pool))
        print(sum_of_squares([-1], pool))
        print(sum_of_squares([-1, -2, -3], pool))

        print(sum_of_squares(['1', '2', '3'], pool))
        print(sum_of_squares(['-1', '-2', '-3'], pool))
        print(sum_of_squares(['1', '2', '#100', '3'], pool))

        print(sum_of_squares(li, pool))




"""
the above print statements should yield:
0
1
14
1
14
14
14
14
"""