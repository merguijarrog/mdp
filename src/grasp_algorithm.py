import random
import time
from greedy import *
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

"""Implementación del algoritmo GRASP."""
def GRASP(m_distances, m, max_time,num_neighbors):
    best_solution = []
    best_distance = 0
    start_time = time.time()
    iter=0
    
    while time.time() - start_time < max_time:
        candidate_solution = greedy_construction(m_distances, m)
        candidate_solution = hill_climbing(candidate_solution, m_distances,num_neighbors)
        candidate_distance = objective_function(candidate_solution, m_distances)
        if candidate_distance > best_distance:
            best_solution = candidate_solution
            best_distance = candidate_distance
        iter=iter+1
        
    return best_solution,iter