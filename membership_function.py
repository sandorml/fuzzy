def currying(f):
    def curried(*args):
        if len(args) >= f.__code__.co_argcount:
            return f(*args)
        return lambda *args2: curried(*(args+args2))
    return curried


@currying
def triangular(a, b, m, x):
    if x <= a or x >= b:
        return 0
    elif a < x <= m:
        return (x-a)/(m-a)
    return (b-x)/(b-m)


@currying
def pi(a, b, c, d, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    if c <= x <= d:
        return (d - x) / (d - c)
    return 1 if b <= x <= c else 0


# trapecio = pi(1,2,3,5)

# import numpy as np
# import matplotlib.pyplot as pl

# x = np.arange(0,10,0.01)
# y = [trapecio(i) for i in x]

# pl.plot(x,y)
# pl.show()
