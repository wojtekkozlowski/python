# iterative
def list_sum_it(inp):
    result = 0
    for i in inp:
        result += i
    return result


# recursive
def list_sum_rec(inp):
    if len(inp) == 0:
        return 0
    else:
        return inp[-1] + list_sum_rec(inp[:-1])


# recursive prettified
def list_sum_rec_prettified(inp):
    return 0 if len(inp) == 0 else inp[-1] + list_sum_rec(inp[:-1])
