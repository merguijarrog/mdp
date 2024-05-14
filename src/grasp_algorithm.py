import random
from hill_climbing import *

def objective_function(node_set, distances):
    """Función objetivo: maximizar la distancia mínima entre los nodos del conjunto."""
    min_distance = float('inf')
    for i in range(len(node_set)):
        for j in range(i+1, len(node_set)):
            distance = distances[node_set[i]][node_set[j]]
            if distance < min_distance:
                min_distance = distance
    return min_distance

def greedy_construction_maxmin(m_distances, subset_size):
    """
    Construcción golosa para generar una solución inicial para el problema de máxima diversidad con el modelo MaxMin.

    Args:
    - m_distances: matriz de distancias entre los elementos.
    - subset_size: tamaño del subconjunto a seleccionar.

    Returns:
    - Una lista que representa la solución inicial.
    """
    n_nodes = len(m_distances)
    solution = []
    
    # Creamos una lista de índices de nodos disponibles
    candidates = list(range(n_nodes))
    
    while len(solution) < subset_size:
        if not solution:
            # Si la solución está vacía, seleccionamos un nodo aleatorio como el primero
            selected_candidate = random.choice(candidates)
        else:
            # Calculamos la distancia mínima para cada candidato con los nodos ya seleccionados
            candidate_min_distances = [(candidate, min(m_distances[candidate][selected_node] for selected_node in solution)) for candidate in candidates]
            
            # Seleccionamos el candidato que maximiza la distancia mínima
            selected_candidate = max(candidate_min_distances, key=lambda x: x[1])[0]
        
        solution.append(selected_candidate)
        candidates.remove(selected_candidate)
    
    return solution

def GRASP(distances, subset_size, max_iterations):
    """Implementación del algoritmo GRASP."""
    best_solution = []
    best_distance = 0
    
    for _ in range(max_iterations):
        candidate_solution = greedy_construction_maxmin(distances, subset_size)
        candidate_solution = hill_climbing(candidate_solution, distances,max_iterations)
        candidate_distance = objective_function(candidate_solution, distances)
        if candidate_distance > best_distance:
            best_solution = candidate_solution
            best_distance = candidate_distance
    
    return best_solution