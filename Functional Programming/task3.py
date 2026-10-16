from functools import reduce

def sum_of_squares(l):
    filtered = list(filter(lambda x : not str(x).startswith('#'), l))
    cast_ints = list(map(int, filtered))
    squares = list(map(lambda x : x**2, cast_ints))
    return reduce(lambda x, y: x + y, squares)


print(sum_of_squares([0]))
print(sum_of_squares([1]))
print(sum_of_squares([1, 2, 3]))
print(sum_of_squares([-1]))
print(sum_of_squares([-1, -2, -3]))

print(sum_of_squares(['1', '2', '3']))
print(sum_of_squares(['-1', '-2', '-3']))
print(sum_of_squares(['1', '2', '#100', '3']))


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