
pi = 3.141592653589793

##
# @brief Function rounds number to 8 decimal numbers
#
# @param x number to round
# @return rounded number
#

def rounded(x):
    return round(x, 8)

##
# @brief Function adds two numbers
#
#    @param x First number to add
#    @param y Second number to add
#    @return result of adding two numbers
#

def add(x, y):
    return rounded(x + y)

##
# @brief Function substracts y from x
#
# @param x base number
# @param y number to be substracted from base
# @return result of substraction
#

def sub(x, y):
    return rounded(x - y)

##
# @brief Function multiplies two numbers
#
# @param x base
# @param y number to multiply by
# @return result of multiplication
##

def mul(x, y):
    return rounded(x * y)

##
# @brief Function divides x by y
#
# @param x divident
# @param y dividor
# @return result of dividing
#

def div(x, y):
    if y == 0:
        raise ZeroDivisionError("Zero division")
    else:
        return rounded(x / y)

##
# @brief Function calculates factorial of given number
#
# @param x base
# @return factorial result
#

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

##
# @brief Function raises base to the power of e
#
# @param x base
# @param e exponent
# @return x raised to the power of e
#

def pow(x, e):
    if x == 0 and e < 0:
        raise ValueError("Cannot raise zero to negative value")
    return rounded(x ** e)

##
# @brief Function finds n root of base
#
# @param x base
# @param n root exponent
# @return Nth root of given number
#

def root(x, n):
    if x<0:
        raise ValueError("Cannot find root to negative value")
    return rounded(x ** (1 / float(n)))

##
# @brief Function finds modulo of base and
#
# @param x divident
# @param y dividor
# @return modulo of divident
#

def mod(x, y):
    if not isinstance(x, int):
        raise ValueError("Modulo supports only natural numbers")
    elif not isinstance(y, int):
        raise ValueError("Modulo supports only natural numbers")
    elif y == 0:
        raise ValueError("Zero division")
    else:
        return rounded(x % y)

##
# @brief Function find sinus of given number using taylor series
#
# @param x base
# @return result of taylor series
#

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

##
# @brief Function find cosinus of given number using taylor series
# @param x base
# @return result of taylor series
#

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
##
# @brief Function find tangens of given number using previously implemented functio>
#
# @param x base
# @return result of dividing sin(x) by cos(x)
#

def tan(x):
    return rounded(sin(x) / cos(x))
