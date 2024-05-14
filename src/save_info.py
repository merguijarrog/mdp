import sqlite3
import time
import json
from greedy import *
from tabu_search import *
from algorithms import *
from hill_climbing import *
from accuracy import *
from print_graphic import *
from tabu_algorithm import *
from grasp_algorithm import *
import numpy as np

conexion = sqlite3.connect("MDP_results.sqlite")
cursor = conexion.cursor()
insert_db ='''INSERT INTO results (algorithm,problem_size,solution,execution_time,filename) VALUES (?, ?, ?, ?, ?)'''

def save_info(m_distance,m,size_problem,coord_x,coord_y,filename):
    solutions = []
    
#GREEDY
    start = time.time()
    solution_greedy = maxmin_greedy(m_distance, m)
    end = time.time()
    solutions.append(solution_greedy)
    execution_time=float(end-start)
    solution_greedy_str = json.dumps([str(element) for element in solution_greedy]) #para guardar la solución en bd
    array_solution_greedy = np.zeros(size_problem,dtype=int)
    for solution in solution_greedy:
        array_solution_greedy[solution]=1

    cursor.execute(insert_db, ("Algoritmo Greedy", size_problem, solution_greedy_str,execution_time,filename))
    conexion.commit()
    array_solution_greedy_str = ''.join(map(str, array_solution_greedy.tolist()))
    print("GREEDY")
    print(solution_greedy)
    print(array_solution_greedy_str)

#TABU SEARCH
    start = time.time()
    solution_tabu = tabu_serach(m_distance,m,1000,5)
    end = time.time()
    execution_time=float(end-start)
    solutions.append(solution_tabu)
    solution_tabu_str = json.dumps([str(element) for element in solution_tabu]) #para guardar la solución en bd
    cursor.execute(insert_db, ("Algoritmo Tabu", size_problem, solution_tabu_str,execution_time,filename))
    conexion.commit()
    print("TABU")
    print(solution_tabu)

#GRASP
    start = time.time()
    solution_grasp= GRASP(m_distance,m,10) 
    end = time.time()
    solutions.append(solution_grasp)
    execution_time=float(end-start)
    solution_grasp_str = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd
    cursor.execute(insert_db, ("Algoritmo GRASP", size_problem, solution_grasp_str,execution_time,filename))
    conexion.commit()
    print("GRASP")
    print(solution_grasp)
   
#HILL CLIMBING    
    solution_greedy_upgrade = hill_climbing(solution_greedy,m_distance,1000,10)
    solutions.append(solution_greedy_upgrade)
    execution_time=float(end-start)
    solution_greedy_upgrade_str = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd
    cursor.execute(insert_db, ("Hill Climbing", size_problem, solution_greedy_upgrade_str,execution_time,filename))
    conexion.commit()
    
    array_solution_greedy_upgrade = np.zeros(size_problem,dtype=int)
    for solution in solution_greedy_upgrade:
        array_solution_greedy_upgrade[solution]=1
        
    solution_greedy_upgrade_str = ''.join(map(str, array_solution_greedy_upgrade.tolist()))
    print("hill climbing")
    print(solution_greedy_upgrade)
    print(solution_greedy_upgrade_str)
    
    #suma = sum(m_distance[solution_greedy_upgrade[i]][solution_greedy_upgrade[j]] for i in range(len(solution_greedy_upgrade)) for j in range(i+1, len(solution_greedy_upgrade)))

    
    #tabuAlgSolution = search_local(m_distance,m,1000,5)
    #solutions.append(tabuAlgSolution)
    
    #graspAlgSolution = GRASP(m_distance,m,1000)
    #solutions.append(graspAlgSolution)
    
    print_all_solutions(coord_x,coord_y,solutions)
    #print(tabuAlgSolution)
    #printGrap(coord_x,coord_y,tabuAlgSolution)