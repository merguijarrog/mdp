import random
import time

def select_initial_node(m_distance, candidates):
    max_avg_distance = 0
    best_node = None
    for candidate in candidates:
        avg_distance = sum(m_distance[candidate][i] for i in candidates) / len(candidates)
        if avg_distance > max_avg_distance:
            max_avg_distance = avg_distance
            best_node = candidate
            
    return best_node

def generate_initial_solution(candidates, m_distance, m):
    solution = []
    solution.append(select_initial_node(m_distance, candidates))
    for _ in range(m - 1):
        max_distance = 0
        current_node = None
        for candidate in candidates:
            min_distance = min(m_distance[candidate][i] for i in solution)
            if min_distance > max_distance:
                max_distance = min_distance
                current_node = candidate
        solution.append(current_node)
        candidates.remove(current_node)
    return solution

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

def diversify_solution(m_distances, current_solution, n_nodes, diversification_factor):
    # Diversificar seleccionando algunos nodos al azar y reemplazándolos
    num_changes = max(1, int(len(current_solution) * diversification_factor))
    diversified_solution = current_solution[:]
    for _ in range(num_changes):
        node_to_replace = random.choice(diversified_solution)
        new_node = random.choice(list(set(range(n_nodes)) - set(diversified_solution)))
        diversified_solution[diversified_solution.index(node_to_replace)] = new_node
    return diversified_solution

def reintensify_solution(m_distances, best_solution, m):
    # Generar una nueva solución basada en la mejor solución encontrada
    candidates = list(set(range(len(m_distances))) - set(best_solution))
    return generate_initial_solution(candidates, m_distances, m)

def tabu_search(m_distances, m, max_time, tabu_size, diversification_factor=0.3, reintensify_interval=10):
    n_nodes = len(m_distances)
    candidates = list(range(n_nodes))
    current_solution = generate_initial_solution(candidates, m_distances, m)
    best_solution = current_solution[:]
    best_min_distance = calculate_min_distance(m_distances, best_solution)
    tabu_list = []
    start_time = time.time()
    iteration = 0
    last_improvement = 0

    while time.time() - start_time < max_time:
        neighbor = generate_neighbor(current_solution, n_nodes)
        neighbor_distance = calculate_min_distance(m_distances, neighbor)

        if neighbor not in tabu_list:
            current_solution = neighbor[:]
            update_tabu_list(tabu_list, neighbor, tabu_size)
            if neighbor_distance > best_min_distance:
                best_solution = current_solution[:]
                best_min_distance = neighbor_distance
                last_improvement = iteration
        
        # Diversificación cada cierto número de iteraciones sin mejora
        if iteration - last_improvement >= reintensify_interval:
            current_solution = diversify_solution(m_distances, current_solution, n_nodes, diversification_factor)
            last_improvement = iteration

        # Reintensificación periódica basada en la mejor solución
        if iteration % reintensify_interval == 0 and iteration != 0:
            current_solution = reintensify_solution(m_distances, best_solution, m)

        iteration += 1

    return best_solution, iteration