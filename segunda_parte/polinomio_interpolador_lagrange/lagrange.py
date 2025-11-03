def polinomio_lagrange(x_nodos, y_valores, x_eval):
    """
    Evalúa el polinomio de interpolación de Lagrange en un punto x_eval.

    Args:
        x_nodos (list o array): Nodos de interpolación (valores de x).
        y_valores (list o array): Valores de la función en los nodos (valores de y o f(x)).
        x_eval (float): El valor donde se evaluará el polinomio P(x_eval).

    Returns:
        float: El valor del polinomio de interpolación P(x_eval).
    """
    n = len(x_nodos)
    p_x = 0.0 # Inicializa el polinomio P(x) en cero

    # Itera sobre cada nodo para calcular la suma (i de 0 a n)
    for i in range(n):
        # Calcula el i-ésimo polinomio base de Lagrange, L_i(x)
        L_i_x = 1.0 
        
        # Calcula la productoria para L_i(x) (j de 0 a n, j != i)
        for j in range(n):
            if i != j:
                # Término: (x - x_j) / (x_i - x_j)
                numerador = x_eval - x_nodos[j]
                denominador = x_nodos[i] - x_nodos[j]
                
                # Manejo de posible división por cero (aunque no debería ocurrir
                # si los nodos x_nodos son distintos, que es un requisito)
                if denominador == 0:
                    raise ValueError("Error: Los nodos de interpolación (x_nodos) deben ser distintos.")
                    
                L_i_x *= (numerador / denominador)
        
        # Suma el término y_i * L_i(x) al polinomio total
        p_x += y_valores[i] * L_i_x
        
    return p_x