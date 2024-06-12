import numpy as np
import time
import random

def tabu_search(dist_matrix, solution_size, max_time):
    start_time = time.time()
    num_points = len(dist_matrix)
    Z = set(range(num_points))  # Conjunto de puntos

    # Inicialización de la lista tabú
    tabu_list = {}

    # Algorithm 1: Constructive Algorithm
    def construct_initial_solution():
        initial_point = random.choice(list(Z))
        X = {initial_point}
        while len(X) < solution_size:
            remaining_points = Z - X
            candidate = max(remaining_points, key=lambda x: min(dist_matrix[x][y] for y in X))
            X.add(candidate)
        return X

    # Algorithm 3: Calculation streamlining after adding an element x∗
    def update_distances_after_adding(x_star, min_dist, min_dist_count):
        for x in Z - {x_star}:
            if dist_matrix[x][x_star] < min_dist[x]:
                min_dist[x] = dist_matrix[x][x_star]
                min_dist_count[x] = 1
            elif dist_matrix[x][x_star] == min_dist[x]:
                min_dist_count[x] += 1

    # Algorithm 4: Update calculations after dropping an element x#
    def update_distances_after_dropping(x_drop, X, min_dist, min_dist_count):
        for x in Z - {x_drop}:
            if dist_matrix[x][x_drop] == min_dist[x]:
                if min_dist_count[x] > 1:
                    min_dist_count[x] -= 1
                else:
                    # Recalculate min distance and count
                    distances = [dist_matrix[x][y] for y in X if y != x]
                    min_dist[x] = min(distances)
                    min_dist_count[x] = distances.count(min_dist[x])

    # Function to evaluate the solution (Min distance)
    def evaluate_solution(X):
        if len(X) < 2:
            return float('inf')
        return min(dist_matrix[x][y] for x in X for y in X if x != y)

    # Algorithm 2: Drop-Add Simple Tabu Search with improvements
    def drop_add_tabu_search(initial_solution):
        X = initial_solution.copy()
        best_solution = X.copy()
        best_distance = evaluate_solution(X)
        iteration = 0
        min_dist = {x: min(dist_matrix[x][y] for y in X if x != y) for x in Z}
        min_dist_count = {x: sum(1 for y in X if dist_matrix[x][y] == min_dist[x]) for x in Z}
        no_improvement_counter = 0
        dynamic_tabu_size = int(solution_size / 2)

        while time.time() - start_time < max_time:
            if no_improvement_counter > 5:
                # Diversificación: Cambio aleatorio de la solución
                random_point = random.choice(list(Z - X))
                X = {random_point}
                while len(X) < solution_size:
                    remaining_points = Z - X
                    candidate = max(remaining_points, key=lambda x: min(dist_matrix[x][y] for y in X))
                    X.add(candidate)
                no_improvement_counter = 0
            else:
                # Paso de eliminación
                drop_point = random.choice(list(X))
                while drop_point in tabu_list:
                    drop_point = random.choice(list(X))
                X.remove(drop_point)
                update_distances_after_dropping(drop_point, X, min_dist, min_dist_count)

                # Paso de adición
                remaining_points = Z - X
                add_point = max(remaining_points, key=lambda x: min(dist_matrix[x][y] for y in X))
                while add_point in tabu_list:
                    remaining_points.remove(add_point)
                    add_point = max(remaining_points, key=lambda x: min(dist_matrix[x][y] for y in X))
                X.add(add_point)
                update_distances_after_adding(add_point, min_dist, min_dist_count)

                # Evaluar nueva solución
                current_distance = evaluate_solution(X)
                if current_distance > best_distance:
                    best_solution = X.copy()
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