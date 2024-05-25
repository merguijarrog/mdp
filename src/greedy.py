import random
 
# Implementación del algoritmo greedy modelo MAXMIN
def greedy_construction(m_distance, m):
    n_nodes = len(m_distance)
    solution = []
    
    # Creamos una lista de índices de nodos disponibles
    candidates = list(range(n_nodes))
    
    while len(solution) < m:
        if not solution:
            # Si la solución está vacía, seleccionamos un nodo aleatorio como el primero
            selected_candidate = random.choice(candidates)
        else:
            # Calculamos la distancia mínima para cada candidato con los nodos ya seleccionados
            candidate_min_distances = [(candidate, min(m_distance[candidate][selected_node] for selected_node in solution)) for candidate in candidates]
            
            # Seleccionamos el candidato que maximiza la distancia mínima
            selected_candidate = max(candidate_min_distances, key=lambda x: x[1])[0]
        
        solution.append(selected_candidate)
        candidates.remove(selected_candidate)
    
    return solution
