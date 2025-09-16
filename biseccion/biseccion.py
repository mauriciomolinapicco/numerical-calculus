def f(x):
    return x**3 - x - 2

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

raiz = bisection(1, 2)
print(f"raiz aproximada: {raiz}")
