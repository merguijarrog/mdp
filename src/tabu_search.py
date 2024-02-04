import numpy as np

def maxmin_greedy_tabu(m_distance, k, tabu_size):
  solution = []
  candidates = list(range(len(m_distance)))
  tabu_list = []  # Lista Tabu para almacenar los puntos prohibidos

  # Elegir el punto inicial de forma aleatoria
  #punto_inicial = np.random.choice(candidates)
  start_node = select_best_node(m_distance,candidates)
  solution.append(start_node)
  candidates.remove(start_node)

  # Iterar para seleccionar los k-1 puntos restantes
  for _ in range(k - 1):
    max_distance = 0
    current_node = None

    # Encontrar el punto con la máxima distancia mínima a los seleccionados
    for candidate in candidates:
      min_distance = min(m_distance[candidate][i] for i in solution)

      # Verificar si el candidato está en la lista Tabu
      if candidate in tabu_list:
        continue

      if min_distance > max_distance:
        max_distance = min_distance
        current_node = candidate

    # Añadir el nuevo seleccionado a la lista y actualizar la lista Tabu
    solution.append(current_node)
    candidates.remove(current_node)
    tabu_list.append(current_node)

    # Actualizar la lista Tabu eliminando elementos más antiguos
    tabu_list = [node for node in tabu_list if tabu_list.index(node) < tabu_size]

  return solution


def select_best_node(m_distance, candidates):
    best_average = []
    
    for candidate in candidates:
        dist_candidate = [m_distance[candidate][i] for i in candidates]
        dist_average = sum(dist_candidate) / len(dist_candidate)
        best_average.append((candidate, dist_average))
    
    best_average.sort(key=lambda x: x[1], reverse=True)
    best_node = best_average[0][0]
    
    return best_node
