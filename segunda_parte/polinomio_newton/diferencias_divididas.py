def diferencias_divididas(x, y):
    """
    Calcula los coeficientes de las diferencias divididas para el polinomio de Newton.
    Args:
        x (list o array): Nodos de interpolación (valores de x).
        y (list o array): Valores de la función en los nodos (valores de y o f(x)).
    Returns:
        list: La lista de coeficientes (las diferencias divididas en la diagonal).
    """
    n = len(x)
    # Inicializa la matriz de diferencias divididas. Solo necesitamos la diagonal superior.
    # d[i] contendrá la diferencia dividida f[x_0, x_1, ..., x_i]
    d = list(y)  # Copiamos la primera columna (f[x_i])

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            # Fórmula: f[x_i, ..., x_{i-j}] = (f[x_i, ..., x_{i-j+1}] - f[x_{i-1}, ..., x_{i-j}]) / (x_i - x_{i-j})
            # En la implementación in-place, d[i] se convierte en f[x_{i}, ..., x_{i-j}]
            # y d[i-1] es f[x_{i-1}, ..., x_{i-j}]
            d[i] = (d[i] - d[i - 1]) / (x[i] - x[i - j])
    
    # La lista 'd' ahora contiene los coeficientes necesarios:
    # d[0] = f[x_0]
    # d[1] = f[x_1, x_0]
    # d[2] = f[x_2, x_1, x_0]
    # ...
    return d

def polinomio_newton(x, coeficientes, x_eval):
    """
    Evalúa el polinomio de interpolación de Newton en un punto x_eval.

    Args:
        x (list o array): Nodos de interpolación (valores de x).
        coeficientes (list): Coeficientes de las diferencias divididas (obtenidos de la función anterior).
        x_eval (float): El valor donde se evaluará el polinomio P(x_eval).

    Returns:
        float: El valor del polinomio de interpolación P(x_eval).
    """
    n = len(x)
    # El valor inicial es el primer término: f[x_0]
    p_x = coeficientes[n - 1] 

    # Aplicamos la forma anidada (Horner) para la evaluación:
    # P(x) = d[0] + (x - x_0)(d[1] + (x - x_1)(d[2] + ... + (x - x_{n-2})d[n-1]))
    # Al iterar desde el final hacia el principio, usamos:
    # P(x) = (...((d_{n-1})*(x - x_{n-2}) + d_{n-2})*(x - x_{n-3}) + ... )*(x - x_0) + d_0
    
    for i in range(n - 2, -1, -1):
        p_x = p_x * (x_eval - x[i]) + coeficientes[i]
        
    return p_x