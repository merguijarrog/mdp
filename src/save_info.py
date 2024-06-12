import time
import json
from greedy import *
from hill_climbing import *
from print_graphic import *
from tabu_algorithm import *
from grasp_algorithm import *
import pandas as pd
import os

#columnas para el excel
columns = ["Algoritmo","Instancia", "n","m", "Solucion","Tiempo","Distancia minima","Iteraciones"]

def save_info(m_distance,m,size_problem,filename,coord_x,coord_y):
    print_solutions =[]
    solutions = []
    if size_problem < 500:
        max_time = size_problem
        iter = size_problem
    else:
        max_time = 500
        iter = 500
    num_neighbors = m
    
#GREEDY
    start = time.time()
    solution_greedy = greedy_construction(m_distance, m, 1)
    end = time.time()
    print_solutions.append(solution_greedy)
    execution_time= round(end-start, 2)
    solution_greedy_str = json.dumps([str(element) for element in solution_greedy]) #para guardar la solución en bd  
        
    solutions.append(["Greedy",filename,size_problem,m,solution_greedy_str,
                      execution_time,get_min_distance(solution_greedy,m_distance),0])
    
    print("Generada solucion para la instancia: "+filename+ " - Algoritmo Greedy")
   

#TABU SEARCH
    start = time.time()
    solution_tabu= tabu_search(m_distance,m,max_time)
    end = time.time()
    print_solutions.append(solution_tabu)
    execution_time= round(end-start, 2)
    solution_tabu_str = json.dumps([str(element) for element in solution_tabu])
        
    solutions.append(["Tabu Search",filename,size_problem,m,solution_tabu_str,execution_time,
                      get_min_distance(solution_tabu,m_distance),iter])

    print("Generada solucion para la instancia: "+filename+ " - Tabu Search")

#GRASP
    start = time.time()
    solution_grasp,iter= GRASP(m_distance,m,max_time,num_neighbors) 
    end = time.time()
    execution_time= round(end-start, 2)
    print_solutions.append(solution_grasp)
    solution_grasp_str = json.dumps([str(element) for element in solution_grasp])
    
    solutions.append(["GRASP",filename,size_problem,m,solution_grasp_str,execution_time,
                      get_min_distance(solution_grasp,m_distance),iter])
    
    print("Generada solucion para la instancia: "+filename+ " - GRASP")

   
#HILL CLIMBING  
    start = time.time()
    solution_hill_climbing = hill_climbing(solution_greedy,m_distance,num_neighbors,iter,size_problem)
    end = time.time()
    execution_time= round(end-start, 2)
    print_solutions.append(solution_hill_climbing)
    solution_hill_climbing_str = json.dumps([str(element) for element in solution_hill_climbing])
    
    solutions.append(["Hill Climbing",filename,size_problem,m,solution_hill_climbing_str,execution_time,
                      get_min_distance(solution_hill_climbing,m_distance),100])
    
    print("Generada solucion para la instancia: "+filename+ " - Hill climbing")
    
    if os.path.exists('resultados.xlsx'):
        with pd.ExcelWriter('resultados.xlsx', engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            for solution in solutions:
                name = solution[0]
                df = pd.DataFrame([solution], columns=columns)
                try:
                    existing_df = pd.read_excel('resultados.xlsx', sheet_name=name)
                    df = pd.concat([existing_df, df], ignore_index=True)
                except ValueError:
                    # Si la hoja no existe, creamos una nueva
                    pass
                df.to_excel(writer, index=False, sheet_name=name)
    else:
        with pd.ExcelWriter('resultados.xlsx', engine='openpyxl', mode='w') as writer:
            for solution in solutions:
                name = solution[0]
                df = pd.DataFrame([solution], columns=columns)
                df.to_excel(writer, index=False, sheet_name=name)
            
    #print_all_solutions(coord_x,coord_y,print_solutions)
    #printGrap(coord_x,coord_y,tabuAlgSolution)
    
    
    """
    Calcula la distancia mínima entre todos los pares de nodos en la solución.
    
    Parameters:
    solution (list): Lista de nodos en la solución.
    m_distance (list of list): Matriz de distancias entre los nodos.
    
    Returns:
    float: La distancia mínima entre los nodos en la solución.
    """
def get_min_distance(solution, m_distance):
    min_distance = float('inf')

    # Itera sobre todos los pares de nodos en la solución
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            distance = m_distance[solution[i]][solution[j]]
            # Actualiza la distancia mínima si la distancia actual es menor
            if distance < min_distance:
                min_distance = distance
    
    return min_distance
        
           