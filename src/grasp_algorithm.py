import random

def objective_function(node_set, distances):
    """Función objetivo: maximizar la distancia mínima entre los nodos del conjunto."""
    min_distance = float('inf')
    for i in range(len(node_set)):
        for j in range(i+1, len(node_set)):
            distance = distances[node_set[i]][node_set[j]]
            if distance < min_distance:
                min_distance = distance
    return min_distance

def construct_initial_solution(distances, subset_size):
    """Construye una solución inicial aleatoria."""
    nodes = list(range(len(distances)))
    solution = []
    while len(solution) < subset_size:
        node = random.choice(nodes)
        solution.append(node)
        nodes.remove(node)
    return solution

def local_search(solution, distances):
    """Búsqueda local para mejorar la solución actual."""
    improved = True
    while improved:
        improved = False
        for i in range(len(solution)):
            for j in range(len(distances)):
                if j not in solution:
                    new_solution = solution[:]
                    new_solution[i] = j
                    if objective_function(new_solution, distances) > objective_function(solution, distances):
                        solution = new_solution
                        improved = True
                        break
            if improved:
                break
    return solution

def GRASP(distances, subset_size, max_iterations):
    """Implementación del algoritmo GRASP."""
    best_solution = []
    best_distance = 0
    
    for _ in range(max_iterations):
        candidate_solution = construct_initial_solution(distances, subset_size)
        candidate_solution = local_search(candidate_solution, distances)
        candidate_distance = objective_function(candidate_solution, distances)
        if candidate_distance > best_distance:
            best_solution = candidate_solution
            best_distance = candidate_distance
    
    return best_solution