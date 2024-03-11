def solution_accuracy(solution, m_distance):
  # Obtener la distancia mínima entre los elementos de la solución
  min_distance = min(m_distance[i][j] for i in solution for j in solution if i < j)

  # Obtener la distancia máxima entre todos los elementos
  max_distance = max(m_distance[i][j] for i in range(len(m_distance)) for j in range(len(m_distance)) if i < j)

  # Calcular el accuracy
  accuracy = min_distance / max_distance

  return accuracy