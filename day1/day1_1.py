import math
from functional import seq


# no packages
# iterative
def solution_1_1_1(l):
    result = 0
    for x in l:
        result += math.floor(x / 3.0) - 2
    return result


# just maps
def solution_1_1_2(l):
    divided = list(map(lambda x: x / 3.0, l))
    floored = list(map(lambda x: math.floor(x), divided))
    subtracted = list(map(lambda x: x - 2, floored))
    result = sum(subtracted)
    return result


# recursive
def solution_1_1_3(l):
    return 0 if len(l) == 0 else (math.floor(l[-1] / 3) - 2) + solution_1_1_3(l[:-1])


# 3rd party
# pyfunctional
def solution_1_1_4(l):
    return seq(l).map(lambda x: x / 3.0).map(lambda x: math.floor(x)).map(lambda x: x - 2).sum()
