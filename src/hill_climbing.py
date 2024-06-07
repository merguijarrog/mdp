import random

def objective_function(node_set, m_distance):
    """Función objetivo: maximizar la distancia mínima entre los nodos del conjunto."""
    min_distance = float('inf')
    for i in range(len(node_set)):
        for j in range(i+1, len(node_set)):
            distance = m_distance[node_set[i]][node_set[j]]
            if distance < min_distance:
                min_distance = distance
    return min_distance

def find_worst_node(solution, m_distance):
    """Encuentra el peor nodo en la solución actual."""
    worst_node = None
    worst_value = float('inf')
    for node in solution:
        min_distance = min(m_distance[node][other_node] for other_node in solution if other_node != node)
        if min_distance < worst_value:
            worst_value = min_distance
            worst_node = node
    return worst_node

def find_best_neighbor(current_solution, m_distance, num_neighbors):
    """Encuentra el mejor vecino para la solución actual."""
    worst_node = find_worst_node(current_solution, m_distance)
    if worst_node is None:
        return current_solution, None  # No hay más nodos para probar

    neighbor_distances = [(neighbor, m_distance[worst_node][neighbor]) for neighbor in range(len(m_distance)) if neighbor not in current_solution]
    neighbor_distances.sort(key=lambda x: x[1])

    best_neighbor = current_solution[:]
    best_score = objective_function(best_neighbor, m_distance)
    for neighbor, _ in neighbor_distances[:num_neighbors]:
        new_neighbor = current_solution[:]
        new_neighbor[current_solution.index(worst_node)] = neighbor
        new_score = objective_function(new_neighbor, m_distance)
        if new_score > best_score:
            best_neighbor = new_neighbor
            best_score = new_score
    
    return best_neighbor, worst_node

def diversify_solution(current_solution, m_distance):
    """Diversifica la solución actual intercambiando un nodo de la solución con un nodo fuera de ella."""
    worst_node = find_worst_node(current_solution, m_distance)
    if worst_node is None:
        return current_solution
    
    # Seleccionar un nodo aleatorio que no esté en la solución actual
    available_nodes = [node for node in range(len(m_distance)) if node not in current_solution]
    random_node = random.choice(available_nodes)
    
    # Intercambiar el peor nodo con el nodo seleccionado aleatoriamente
    new_solution = current_solution[:]
    new_solution[current_solution.index(worst_node)] = random_node
    
    return new_solution

def hill_climbing(initial_solution, m_distance, num_neighbors, max_iterations=30, diversification_interval=10):
    """Implementación del algoritmo Hill Climbing con diversificación de vecindario."""
    best_solution = initial_solution[:]
    best_score = objective_function(best_solution, m_distance)
    current_solution = initial_solution[:]
    consecutive_iterations = 0

    for iteration in range(max_iterations):
        neighbor, worst_node = find_best_neighbor(current_solution, m_distance, num_neighbors)
        if neighbor != current_solution:
            current_solution = neighbor
            current_score = objective_function(current_solution, m_distance)
            if current_score > best_score:
                best_solution = current_solution[:]
                best_score = current_score
            consecutive_iterations = 0
        else:
            consecutive_iterations += 1
            if consecutive_iterations >= diversification_interval:
                current_solution = diversify_solution(current_solution, m_distance)
                consecutive_iterations = 0

    return best_solution