import random
 
# Implementación del algoritmo greedy modelo MAXMIN
def maxmin_greedy(m_distance, m):
    solution = []
    candidates = list(range(len(m_distance)))

    # Elegir el punto inicial de forma aleatoria
    random.seed(8)
    start_node = random.choice(candidates)
    #añadimos el elemento a la solución y lo quitamos de los no seleccionados
    solution.append(start_node)
    candidates.remove(start_node)

    # Iterar para seleccionar los m-1 puntos restantes
    for _ in range(m - 1):
        max_distance = 0
        current_node = None

        # Encontrar el punto con la máxima distancia mínima a los seleccionados
        for candidate in candidates:
            min_distance = min(m_distance[candidate][i] for i in solution)
            if min_distance > max_distance:
                max_distance = min_distance
                current_node = candidate

        solution.append(current_node)
        candidates.remove(current_node)

    return solution
