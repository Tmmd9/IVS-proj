
pi = 3.141592653589793


def rounded(x):
    """
    Function rounds number to 8 decimal numbers
    :param x: number to round
    :return: rounded number
    """
    return round(x, 8)


def add(x, y):
    """
    Function adds two numbers
    :param x: First number to add
    :param y: Second nuber to add
    :return: result of adding two numbers
    """
    return rounded(x + y)


def sub(x, y):
    """
    Function substracts y from x
    :param x: base number
    :param y: number to be substracted from base
    :return: result of substraction
    """
    return rounded(x - y)


def mul(x, y):
    """
    Function multiplies two numbers
    :param x: base
    :param y: number to multiply by
    :return: result of multiplication
    """
    return rounded(x * y)


def div(x, y):
    """
    Function divides x by y
    :param x: divident
    :param y: dividor
    :return: result of dividing
    """
    if y == 0:
        raise ZeroDivisionError("Zero division")
    else:
        return rounded(x / y)


def fact(x):
    """
    Function calculates factorial of given number
    :param x: base
    :return: factorial result
    """
    if not isinstance(x, int):
        raise ValueError("Factorial supports only natural numbers")
    elif x < 0:
        raise ValueError("x must be grater than -1")
    elif x == 0:
        return 1
    # recursive call
    else:
        return x * fact(x - 1)


def pow(x, e):
    """
    Function raises base to the power of e
    :param x: base
    :param e: exponent
    :return: x raised to the power of e
    """
    if x == 0 and e < 0:
        raise ValueError("Cannot raise zero to negative value")
    return rounded(x ** e)


def root(x, n):
    """
    Function finds n root of base
    :param x: base
    :param n: root exponent
    :return: Nth root of given number
    """
    if x<0:
        raise ValueError("Cannot find root to negative value")
    return rounded(x ** (1 / float(n)))


def mod(x, y):
    """
    Function finds modulo of base and
    :param x: divident
    :param y: dividor
    :return: modulo of divident
    """
    if not isinstance(x, int):
        raise ValueError("Modulo supports only natural numbers")
    elif not isinstance(y, int):
        raise ValueError("Modulo supports only natural numbers")
    elif y == 0:
        raise ValueError("Zero division")
    else:
        return rounded(x % y)


def sin(x):
    """
    Function find sinus of given number using taylor series
    :param x: base
    :return: result of taylor series
    """
    iterations = 50
    multiplier = 1
    n = x
    start = 3
    for i in range(start, start + iterations, 2):
        multiplier *= -1
        next_term = (x ** i) / fact(i)
        n += multiplier * next_term
    return rounded(n)


def cos(x):
    """
    Function find cosinus of given number using taylor series
    :param x: base
    :return: result of taylor series
    """
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
    """
    Function find tangens of given number using previously implemented functions sin and cos
    :param x: base
    :return: result of dividing sin(x) by cos(x)
    """
    return rounded(sin(x) / cos(x))
