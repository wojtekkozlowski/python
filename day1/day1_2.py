import math
from functional import seq


# iterative
def solution_1_2_1(l):
    def fuel_for_step(m):
        return math.floor(m / 3) - 2

    def fuel_for_item(mass):
        fuel = fuel_for_step(mass)
        f_delta = fuel
        while f_delta >= 0:
            f_delta = fuel_for_step(f_delta)
            if f_delta >= 0:
                fuel += f_delta
        return fuel

    result = 0
    for i in l:
        result += fuel_for_item(i)
    return result


# half recursive
def solution_1_2_2(l):
    def fuel_for_item(mass):
        fuel = math.floor(mass / 3) - 2
        return 0 if fuel <= 0 else fuel + fuel_for_item(fuel)

    return seq(l).map(lambda x: fuel_for_item(x)).sum()


# full recursive
def solution_1_2_3(l):
    def fuel_for_item(mass):
        fuel = math.floor(mass / 3) - 2
        return 0 if fuel <= 0 else fuel + fuel_for_item(fuel)

    return 0 if len(l) == 0 else fuel_for_item(l[-1]) + solution_1_2_2(l[:-1])
