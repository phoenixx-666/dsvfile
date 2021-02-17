def eq(arg):
    return lambda x: x == arg


def ne(arg):
    return lambda x: x != arg


def g(num):
    return lambda x: x > num


def ge(num):
    return lambda x: x >= num


def decr(num=1):
    return lambda x: x - num


def mul(num=1):
    return lambda x: x * num


def decrmul(mul=1, decr=1):
    return lambda x: (x - decr) * mul
