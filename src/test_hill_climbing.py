"""Función objetivo: maximizar la distancia mínima entre los nodos del conjunto."""
def find_best_neighbor(worst_node, distances, solution):
    best_neighbor = None
    max_min_distance = float('-inf')
    for neighbor in range(len(distances)):
        if neighbor not in solution:
            # Calcula la distancia mínima entre el nuevo vecino y los nodos en la solución actual
            min_distance = min(distances[neighbor][node] for node in solution if worst_node != node)
            # Actualiza el máximo de las distancias mínimas
            if min_distance > max_min_distance:
                max_min_distance = min_distance
                best_neighbor = neighbor
    return best_neighbor

"""Encuentra el peor nodo en la solución actual."""
def find_worst_node(solution, distances):
    worst_node = None
    worst_value = float('inf')
    for node in solution:
        min_distance = min(distances[node][other_node] for other_node in solution if other_node != node)
        if min_distance < worst_value:
            worst_value = min_distance
            worst_node = node
    return worst_node

def generate_kneighborhood(worst_node, distances, k):
    neighbors = []
    distances_node = distances[worst_node]
    sort_distances = sorted(enumerate(distances_node), key=lambda x: x[1])
    for neighbor, distance in sort_distances[1:k+1]:
        neighbors.append(neighbor)
    return neighbors

def generate_distance_neighborhood(worst_node, distances, x_distance):
    neighbors = []
    distances_node = distances[worst_node]
    for neighbor, distance in distances_node.items():
        if distance < x_distance:
            neighbors.append(neighbor)
    return neighbors

"""Implementación del algoritmo Hill Climbing."""
def hill_climbing(initial_solution, max_iterations, distances):
    current_solution = initial_solution[:]
    for _ in range(max_iterations):
        worst_node = find_worst_node(current_solution, distances)
        worst_node_index = current_solution.index(worst_node)
        neighbor = find_best_neighbor(worst_node, distances, current_solution)
        if neighbor not in current_solution:
            current_solution[worst_node_index] = neighbor
                
    return current_solution
