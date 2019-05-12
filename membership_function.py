def currying(f):
    def curried(*args):
        if len(args) >= f.__code__.co_argcount:
            return f(*args)
        return lambda *args2: curried(*(args+args2))
    return curried

@currying
def triangular(a, b, m,x):
    if x <= a or x >= b:
        return 0
    elif a < x <= m:
        return (x-a)/(m-a)
    return (b-x)/(b-m)

@currying
def pi(a, b, c, d,x):
    if x <= a or x >= d:
        return 0
    elif a< x<= b:
        return (x-a)/(b-a)
    return (d-x)/(b-c)


