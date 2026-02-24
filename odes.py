
import numpy as np

def trapezoid(f, a, b, n):
    x = np.linspace(a,b,n+1)
    y = f(x)
    h = (b-a)/n
    return h*(0.5*y[0] + sum(y[1:-1]) + 0.5*y[-1])

def simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n debe ser par")
    x = np.linspace(a,b,n+1)
    y = f(x)
    h = (b-a)/n
    return (h/3)*(y[0] + y[-1] + 4*sum(y[1:-1:2]) + 2*sum(y[2:-2:2]))
