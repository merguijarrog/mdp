def hill_climbing(start_solution, m_distance):
    best_solution = start_solution
    best_fitness = calcular_fitness(start_solution, m_distance)

    while True:
        neighborhood = generate_neighborhood(best_solution)
        best_neighbor = max(neighborhood, key=lambda neighbor: calcular_fitness(neighbor, m_distance))

        if calcular_fitness(best_neighbor, m_distance) > best_fitness:
            best_solution = best_neighbor
            best_fitness = calcular_fitness(best_neighbor, m_distance)
        else:
            break

    return best_solution

def generate_neighborhood(solucion_actual):
    vecindario = []

    for i in range(len(solucion_actual)):
        for j in range(i + 1, len(solucion_actual)):
            vecino = solucion_actual.copy()
            vecino[i], vecino[j] = vecino[j], vecino[i]
            vecindario.append(vecino)

    return vecindario


def calcular_fitness(solution, m_distance):
    return sum(m_distance[i][j] for i in solution for j in solution)