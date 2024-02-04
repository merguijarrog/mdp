import matplotlib.pyplot as plt

def printGrap(coord_x,coord_y,solution):
    coord_solution_x=[]
    coord_solution_y=[]
    #creamos una lista con con las coordenadas de la solución
    for i in solution:
        coord_solution_x.append(coord_x[i])
        coord_solution_y.append(coord_y[i])

    plt.plot(coord_x,coord_y, "o",color="b")
    plt.plot(coord_solution_x,coord_solution_y, "o",color="r")
    
    print(coord_solution_x)
    print(coord_solution_y)
    plt.show()
    
    
def print_all_solutions(coord_x, coord_y, solutions):
  """
  Pintar 4 gráficos con diferentes soluciones.

  Argumentos:
    coord_x: Lista de coordenadas X.
    coord_y: Lista de coordenadas Y.
    solutions: Lista de listas, donde cada lista representa una solución.
  """
  # Creamos una figura con 2 filas y 2 columnas
  fig, axes = plt.subplots(2, 2)

  titles =["Greedy","Tabu Search","GRASP","Greedy + Hill climbing"]
  # Recorremos las soluciones y pintamos un gráfico para cada una
  for i, solution in enumerate(solutions):
    # Obtenemos las coordenadas de la solución actual
    coord_solution_x = [coord_x[i] for i in solution]
    coord_solution_y = [coord_y[i] for i in solution]

    # Pintamos el gráfico en el subplot actual
    axes[i // 2, i % 2].plot(coord_x, coord_y, "o", color="b")
    axes[i // 2, i % 2].plot(coord_solution_x, coord_solution_y, "o", color="r")
    axes[i // 2, i % 2].set_title(titles[i])

  # Mostramos la figura
  plt.show()