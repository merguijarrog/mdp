import random

def objective_function(node_set,distances):
    """Función objetivo: maximizar la distancia mínima entre los nodos del conjunto."""
    min_distance = float('inf')
    for i in range(len(node_set)):
        for j in range(i+1, len(node_set)):
            distance = distances[node_set[i]][node_set[j]]
            min_distance = min(min_distance, distance)
    return min_distance

def generate_neighbor(current_solution,distances):
    """Genera un vecino cambiando aleatoriamente un nodo del conjunto."""
    neighbor = current_solution.copy()
    index_to_change = random.randint(0, len(neighbor) - 1)
    new_node = random.randint(0, len(distances) - 1)
    neighbor[index_to_change] = new_node
    return neighbor

def hill_climbing(initial_solution, max_iterations, distances):
    """Implementación del algoritmo Hill Climbing para maximizar la distancia mínima."""
    # Inicialización: Usa la solución inicial proporcionada.
    current_solution = initial_solution
    
    # Bucle iterativo
    for _ in range(max_iterations):
        # Genera un vecino cambiando un nodo del conjunto actual.
        neighbor = generate_neighbor(current_solution,distances)
        
        # Evalúa la calidad del vecino y compara con el conjunto actual.
        if objective_function(neighbor,distances) > objective_function(current_solution,distances):
            current_solution = neighbor  # Actualiza el conjunto si el vecino es mejor.
    
    return current_solution