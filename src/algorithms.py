
def select_best_node(m_distance, candidates):
    best_average = []
    
    for candidate in candidates:
        dist_candidate = [m_distance[candidate][i] for i in candidates]
        dist_average = sum(dist_candidate) / len(dist_candidate)
        best_average.append((candidate, dist_average))
    
    best_average.sort(key=lambda x: x[1], reverse=True)
    best_node = best_average[0][0]
    
    return best_node

def calcular_fitness(solution, m_distance):
    return sum(m_distance[i][j] for i in solution for j in solution)

def maxmin_greedy_grasp(m_distance, k):
    solution = []
    candidates = list(range(len(m_distance)))

    start_node = select_best_node(m_distance, candidates)
    solution.append(start_node)
    candidates.remove(start_node)

    for _ in range(k - 1):
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

def old_grasp(m_distance, k, max_iter):
    best_solution = []
    best_fitness = float('-inf')

    for _ in range(max_iter):
        current_solution = maxmin_greedy_grasp(m_distance, k)
        current_fitness = calcular_fitness(current_solution, m_distance)

        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_solution = current_solution

    return best_solution
