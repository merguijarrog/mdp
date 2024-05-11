import random

"""Función objetivo: maximizar la distancia mínima entre los nodos del conjunto"""
def objective_function(node_set,m_distance):
    min_distance = float('inf')
    for i in range(len(node_set)):
        for j in range(i+1, len(node_set)):
            distance = m_distance[node_set[i]][node_set[j]]
            min_distance = min(min_distance, distance)
    return min_distance

"""Genera un vecino cambiando aleatoriamente un nodo del conjunto"""
def generate_neighbor(current_solution,m_distance):
    neighbor = current_solution[:]
    index_change = random.randint(0, len(neighbor) - 1)
    new_node = random.randint(0, len(m_distance) - 1)
    neighbor[index_change] = new_node
    return neighbor

"""Implementación del algoritmo Hill Climbing para maximizar la distancia mínima"""
def hill_climbing(initial_solution, max_iterations, m_distance):
    # Inicialización: Usa la solución inicial proporcionada
    current_solution = initial_solution
    
    for _ in range(max_iterations):
        # Genera un vecino cambiando un nodo del conjunto actual
        neighbor = generate_neighbor(current_solution,m_distance)
        
        # Evalúa la calidad del vecino y compara con el conjunto actual
        if objective_function(neighbor,m_distance) > objective_function(current_solution,m_distance):
            # Actualiza el conjunto si el vecino es mejor
            current_solution = neighbor 
    
    return current_solution