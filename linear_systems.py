
import math

def bisection(f, a, b, tol=1e-8, max_iter=100):
    if f(a) * f(b) > 0:
        raise ValueError("Intervalo inválido")
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

def newton(f, df, x0, tol=1e-8, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x = x - f(x)/df(x)
        if abs(f(x)) < tol:
            return x
    return x
