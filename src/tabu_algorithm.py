import numpy as np
import time
import random

def tabu_search(m_distances, solution_size, max_time):
    start_time = time.time()
    num_points = len(m_distances)
    candidates = set(range(num_points))  # Conjunto de puntos

    # Inicialización de la lista tabú
    tabu_list = {}

    # Algorithm 1: Constructive Algorithm
    def construct_initial_solution():
        initial_point = random.choice(list(candidates))
        solution = {initial_point}
        while len(solution) < solution_size:
            remaining_points = candidates - solution
            candidate = max(remaining_points, key=lambda x: min(m_distances[x][y] for y in solution))
            solution.add(candidate)
        return solution

    # Algorithm 3: Calculation streamlining after adding an element x∗
    def update_distances_after_adding(x_star, min_dist, min_dist_count):
        for x in candidates - {x_star}:
            if m_distances[x][x_star] < min_dist[x]:
                min_dist[x] = m_distances[x][x_star]
                min_dist_count[x] = 1
            elif m_distances[x][x_star] == min_dist[x]:
                min_dist_count[x] += 1

    # Algorithm 4: Update calculations after dropping an element x#
    def update_distances_after_dropping(x_drop, solution, min_dist, min_dist_count):
        for x in candidates - {x_drop}:
            if m_distances[x][x_drop] == min_dist[x]:
                if min_dist_count[x] > 1:
                    min_dist_count[x] -= 1
                else:
                    # Recalculate min distance and count
                    distances = [m_distances[x][y] for y in solution if y != x]
                    min_dist[x] = min(distances)
                    min_dist_count[x] = distances.count(min_dist[x])

    # Function to evaluate the solution (Min distance)
    def evaluate_solution(solution):
        if len(solution) < 2:
            return float('inf')
        return min(m_distances[x][y] for x in solution for y in solution if x != y)

    # Algorithm 2: Drop-Add Simple Tabu Search with improvements
    def drop_add_tabu_search(initial_solution):
        solution = initial_solution.copy()
        best_solution = solution.copy()
        best_distance = evaluate_solution(solution)
        iteration = 0
        min_dist = {x: min(m_distances[x][y] for y in solution if x != y) for x in candidates}
        min_dist_count = {x: sum(1 for y in solution if m_distances[x][y] == min_dist[x]) for x in candidates}
        no_improvement_counter = 0
        dynamic_tabu_size = int(solution_size / 2)

        while time.time() - start_time < max_time:
            if no_improvement_counter > 5:
                # Diversificación: Cambio aleatorio de la solución
                random_point = random.choice(list(candidates - solution))
                solution = {random_point}
                while len(solution) < solution_size:
                    remaining_points = candidates - solution
                    candidate = max(remaining_points, key=lambda x: min(m_distances[x][y] for y in solution))
                    solution.add(candidate)
                no_improvement_counter = 0
            else:
                # Paso de eliminación
                drop_point = random.choice(list(solution))
                while drop_point in tabu_list:
                    drop_point = random.choice(list(solution))
                solution.remove(drop_point)
                update_distances_after_dropping(drop_point, solution, min_dist, min_dist_count)

                # Paso de adición
                remaining_points = candidates - solution
                add_point = max(remaining_points, key=lambda x: min(m_distances[x][y] for y in solution))
                while add_point in tabu_list:
                    remaining_points.remove(add_point)
                    add_point = max(remaining_points, key=lambda x: min(m_distances[x][y] for y in solution))
                solution.add(add_point)
                update_distances_after_adding(add_point, min_dist, min_dist_count)

                # Evaluar nueva solución
                current_distance = evaluate_solution(solution)
                if current_distance > best_distance:
                    best_solution = solution.copy()
                    best_distance = current_distance
                    no_improvement_counter = 0  # Reiniciar contador en caso de mejora
                else:
                    no_improvement_counter += 1

                # Actualizar lista tabú con tamaño dinámico
                tabu_list[drop_point] = iteration
                tabu_list[add_point] = iteration
                iteration += 1

                # Mantener tamaño de lista tabú
                if iteration > dynamic_tabu_size:
                    for key in list(tabu_list.keys()):
                        if iteration - tabu_list[key] > dynamic_tabu_size:
                            del tabu_list[key]

        return best_solution

    # Lógica principal del algoritmo
    initial_solution = construct_initial_solution()
    best_solution = drop_add_tabu_search(initial_solution)
    
    return list(best_solution)