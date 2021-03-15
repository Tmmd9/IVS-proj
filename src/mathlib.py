# math library IVS


pi = 3.141592653589793


def rounded(x):
    return round(x, 8)


def add(x, y):
    return rounded(x + y)


def sub(x, y):
    return rounded(x - y)


def mul(x, y):
    return rounded(x * y)


def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Zero division")
    else:
        return rounded(x / y)


def fact(x):
    if not isinstance(x, int):
        raise ValueError("Factorial supports only natural numbers")
    elif x < 0:
        raise ValueError("x must be grater than -1")
    elif x == 0:
        return 1
    # recursive call
    else:
        return x * fact(x - 1)


# x = base
# e = exponent
def pow(x, e):
    # zalezi ci budeme podporovat aj negativne cisla/desatine alebo len prirodzene
    """if not isinstance(e, int):
        raise ValueError("error")"""
    """if e <= 0:
        raise ValueError("exponent must be grater than 0")"""
    if x == 0 and e < 0:
        raise ValueError("Cannot raise zero to negative value")
    return rounded(x ** e)


def root(x, n):
    if x<0:
        raise ValueError("Cannot find root to negative value")
    return rounded(x ** (1 / float(n)))


def mod(x, y):
    if not isinstance(x, int):
        raise ValueError("Modulo supports only natural numbers")
    elif not isinstance(y, int):
        raise ValueError("Modulo supports only natural numbers")
    elif y == 0:
        raise ValueError("Zero division")
    else:
        return rounded(x % y)


# taylor series sin
def sin(x):
    iterations = 50
    multiplier = 1
    n = x
    start = 3
    for i in range(start, start + iterations, 2):
        multiplier *= -1
        next_term = (x ** i) / fact(i)
        n += multiplier * next_term
    return rounded(n)


# taylor series cos
def cos(x):
    iterations = 50
    multiplier = 1
    n = 1
    start = 2
    for i in range(start, start + iterations, 2):
        multiplier *= -1
        next_term = (x ** i) / fact(i)
        n += multiplier * next_term
    return rounded(n)


def tan(x):
    return rounded(sin(x) / cos(x))
