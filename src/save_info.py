import time
import json
from greedy import *
from hill_climbing import *
from print_graphic import *
from tabu_algorithm import *
from grasp_algorithm import *
import numpy as np
import pandas as pd
import os


columns = ["Algoritmo","Instancia", "N","M", "Solucion","Solucion traducida","Tiempo","Distancia minima","Promedio solucion"]

def save_info(m_distance,m,size_problem,filename,coord_x,coord_y):
    print_solutions =[]
    solutions = []
    
    
#GREEDY
    start = time.time()
    solution_greedy = maxmin_greedy(m_distance, m)
    end = time.time()
    print_solutions.append(solution_greedy)
    execution_time=float(end-start)
    solution_greedy_str = json.dumps([str(element) for element in solution_greedy]) #para guardar la solución en bd
    array_solution_greedy = np.zeros(size_problem,dtype=int)
    for solution in solution_greedy:
        array_solution_greedy[solution]=1
    array_solution_greedy = ''.join(map(str, array_solution_greedy.tolist()))    
        
    solutions.append(['Greedy',filename,size_problem,m,array_solution_greedy,solution_greedy_str,execution_time,get_min_distance(solution_greedy,m_distance),get_average(solution_greedy,m_distance)])


    print("Generada solucion para la instancia: "+filename+ " - Algoritmo Greedy")
   

#TABU SEARCH
    start = time.time()
    solution_tabu = tabu_serach(m_distance,m,100,5)
    end = time.time()
    print_solutions.append(solution_tabu)
    execution_time=float(end-start)
    solution_tabu_str = json.dumps([str(element) for element in solution_tabu]) #para guardar la solución en bd
    array_solution_tabu = np.zeros(size_problem,dtype=int)
    for solution in solution_tabu:
        array_solution_tabu[solution]=1
    array_solution_tabu = ''.join(map(str, array_solution_tabu.tolist()))
        
    solutions.append(['TABU Search',
                      filename,size_problem,m,array_solution_tabu,solution_tabu_str,execution_time,
                      get_min_distance(solution_tabu,m_distance),get_average(solution_tabu,m_distance)])

    print("Generada solucion para la instancia: "+filename+ " - Tabu Search")

#GRASP
    start = time.time()
    solution_grasp= GRASP(m_distance,m,10) 
    end = time.time()
    execution_time=float(end-start)
    print_solutions.append(solution_grasp)
    solution_grasp_str = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd
    array_solution_grasp = np.zeros(size_problem,dtype=int)
    for solution in solution_grasp:
        array_solution_grasp[solution]=1
    array_solution_grasp = ''.join(map(str, array_solution_grasp.tolist()))
    
    solutions.append(['GRASP',
                      filename,size_problem,m,array_solution_grasp,solution_grasp_str,execution_time,
                      get_min_distance(solution_grasp,m_distance),get_average(solution_grasp,m_distance)])
    
    print("Generada solucion para la instancia: "+filename+ " - GRASP")

   
#HILL CLIMBING    
    start = time.time()
    solution_hill_climbing = hill_climbing(solution_greedy,m_distance,100,10)
    end = time.time()
    execution_time=float(end-start)
    print_solutions.append(solution_hill_climbing)
    solution_hill_climbing_str = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd
    array_solution_hill_climbing = np.zeros(size_problem,dtype=int)
    for solution in solution_hill_climbing:
        array_solution_hill_climbing[solution]=1
    array_solution_hill_climbing = ''.join(map(str, array_solution_hill_climbing.tolist()))
    
    solutions.append(['Hill Climbing',
                      filename,size_problem,m,array_solution_hill_climbing,solution_hill_climbing_str,execution_time,
                      get_min_distance(solution_hill_climbing,m_distance),get_average(solution_hill_climbing,m_distance)])
    
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
                    # Si la hoja no existe, simplemente creamos una nueva
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
    
# Función para convertir el tiempo en formato HH:MM:SS a segundos
def timer(time):
    time_str = time.strftime('%H:%M:%S', time.gmtime(time))
    horas, minutos, segundos = map(float, time_str.split(':'))
    resultado = horas * 3600 + minutos * 60 + segundos
    return resultado

def get_min_distance(solution, m_distance):
    min_distance = float('inf')

    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            distance = m_distance[solution[i]][solution[j]]
            min_distance = min(min_distance, distance)
    
    return min_distance
    
 
def get_average(solution, m_distance):
    num_elements = len(solution)
    total_distances = sum(m_distance[solution[i]][solution[j]] for i in range(num_elements) for j in range(i+1, num_elements))
    average_distance = total_distances / num_elements
    return average_distance
        
           