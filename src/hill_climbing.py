def objective_function(node_set, m_distance):
    """Función objetivo: maximizar la distancia mínima entre los nodos del conjunto."""
    min_distance = float('inf')
    for i in range(len(node_set)):
        for j in range(i+1, len(node_set)):
            distance = m_distance[node_set[i]][node_set[j]]
            if distance < min_distance:
                min_distance = distance
    return min_distance

def find_worst_node(solution, m_distance, last_worst_node):
    """Encuentra el siguiente peor nodo en la solución actual."""
    worst_node = None
    worst_value = float('-inf')
    for node in solution:
        min_distance = min(m_distance[node][other_node] for other_node in solution if other_node != node)
        if node != last_worst_node:
            if min_distance > worst_value:
                worst_value = min_distance
                worst_node = node
    return worst_node

def find_best_neighbor(current_solution, m_distance, num_neighbors, last_worst_node):
    """Encuentra el mejor vecino para la solución actual."""
    # Encontrar el peor nodo en la solución actual
    worst_node = find_worst_node(current_solution, m_distance, last_worst_node)
    if worst_node is None:
        return current_solution, None  # No hay más nodos para probar
    
    # Calcular las distancias de los vecinos con respecto al peor nodo
    neighbor_distances = [(neighbor, m_distance[worst_node][neighbor]) for neighbor in range(len(m_distance)) if neighbor not in current_solution]
    # Ordenar las distancias de forma ascendente
    neighbor_distances.sort(key=lambda x: x[1])

    # Tomar los k vecinos más cercanos
    best_neighbor = current_solution.copy()
    for neighbor, _ in neighbor_distances[:num_neighbors]:
        new_neighbor = current_solution[:]
        new_neighbor[current_solution.index(worst_node)] = neighbor
        if objective_function(new_neighbor, m_distance) > objective_function(best_neighbor, m_distance):
            best_neighbor = new_neighbor
    
    return best_neighbor, worst_node

def hill_climbing(initial_solution, m_distance, num_neighbors,max_iterations=30):
    """Implementación del algoritmo Hill Climbing."""
    current_solution = initial_solution
    last_worst_node = None
    for _ in range(max_iterations):
        neighbor, worst_node = find_best_neighbor(current_solution, m_distance, num_neighbors, last_worst_node)
        if neighbor != current_solution:
            current_solution = neighbor
            last_worst_node = None
        else:
            last_worst_node = worst_node
            if worst_node is None:
                break  # No hay más nodos para probar
    return current_solution