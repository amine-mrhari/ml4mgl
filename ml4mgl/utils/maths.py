def numerical_lim(f, x, h):
    return (f(x + h) - f(x)) / h

def numerical(f, x, h):
    return (f(x + h) - f(x)) / h