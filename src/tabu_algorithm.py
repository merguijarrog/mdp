import random

def select_initial_node(m_distance, candidates):
    max_avg_distance = 0
    best_node = None
    # selecciona el nodo inicial que maximiza la distancia promedio a los otros nodos
    for candidate in candidates:
        avg_distance = sum(m_distance[candidate][i] for i in candidates) / len(candidates)
        if avg_distance > max_avg_distance:
            max_avg_distance = avg_distance
            best_node = candidate
            
    return best_node


def generate_initial_solution (candidates,m_distance,m):
    solution =[]
    solution.append(select_initial_node(m_distance,candidates))
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
"""
    Calcula la distance mínima entre los nodos seleccionados en el subconjunto
"""
def calculate_min_distance(m_distance, subset):
    min_distance = float('inf')
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            distance = m_distance[subset[i]][subset[j]]
            min_distance = min(min_distance, distance)
    return min_distance

def generate_neighbor(current_solution, n_nodes):
    neighbor = current_solution[:]
    node_to_replace = random.choice(current_solution)
    new_node = random.choice(list(set(range(n_nodes)) - set(current_solution)))
    neighbor[current_solution.index(node_to_replace)] = new_node
    return neighbor

def update_tabu_list(tabu_list, neighbor, tabu_size):
    tabu_list.append(neighbor)
    if len(tabu_list) > tabu_size:
        tabu_list.pop(0)

"""
    Implementación del algoritmo de búsqueda tabú para seleccionar un subconjunto de nodos
    que maximice la distance mínima entre ellos.
"""
def tabu_serach(m_distance, subset_size, max_iter, tabu_size):
    n_nodes = len(m_distance)
    candidates = list(range(len(m_distance)))
    current_solution = generate_initial_solution(candidates,m_distance,subset_size)
    best_solution = current_solution[:]
    best_min_distance = calculate_min_distance(m_distance, best_solution)
    tabu_list = []

    for _ in range(max_iter):
        neighbor = generate_neighbor(current_solution, n_nodes)
        neighbor_distance = calculate_min_distance(m_distance, neighbor)

        if neighbor not in tabu_list:
            current_solution = neighbor[:]
            update_tabu_list(tabu_list, neighbor, tabu_size)
            if neighbor_distance > best_min_distance: 
                best_solution = current_solution[:]
                best_min_distance = neighbor_distance

    return best_solution