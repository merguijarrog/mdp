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

conexion = sqlite3.connect("MDP_results.sqlite")
cursor = conexion.cursor()
insert_db ='''INSERT INTO results (algorithm,problem_size,solution,execution_time) VALUES (?, ?, ?, ?)'''

def save_info(m_distance,m,size_problem,coord_x,coord_y):
    solutions = []
    
    start = time.time()
    solution_greedy = maxmin_greedy(m_distance, m)
    end = time.time()
    solutions.append(solution_greedy)
    execution_time=float(end-start)
    solution_greedy_str = json.dumps([str(element) for element in solution_greedy]) #para guardar la solución en bd
    cursor.execute(insert_db, ("Algoritmo Greedy", size_problem, solution_greedy_str, execution_time))
    conexion.commit()
    #print(solutionGreedy)
    #printGrap(coord_x,coord_y,solutionGreedy)

    start = time.time()
    solution_tabu = maxmin_greedy_tabu(m_distance,m,5) 
    end = time.time()
    execution_time=float(end-start)
    solutions.append(solution_tabu)
    solution_tabu_str = json.dumps([str(element) for element in solution_tabu]) #para guardar la solución en bd
    cursor.execute(insert_db, ("Algoritmo Tabu", size_problem, solution_tabu_str,execution_time))
    conexion.commit()
    #print(solutionTabu)
    #printGrap(coord_x,coord_y,solutionTabu)

    start = time.time()
    solution_grasp= grasp(m_distance,m,5) 
    end = time.time()
    solutions.append(solution_grasp)
    execution_time=float(end-start)
    solution_grasp_str = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd

    cursor.execute(insert_db, ("Algoritmo GRASP", size_problem, solution_grasp_str,execution_time))
    conexion.commit()
    
    solution_greedy_upgrade = hill_climbing(solution_greedy,1000,m_distance)
    solutions.append(solution_greedy_upgrade)
    
    tabuAlgSolution = buscar_subconjunto_optimo(m_distance,m)
    #solutions.append(tabuAlgSolution)
    
    graspAlgSolution = GRASP(m_distance,m,1000)
    #solutions.append(graspAlgSolution)
    
    print_all_solutions(coord_x,coord_y,solutions)
    #print(tabuAlgSolution)
    #printGrap(coord_x,coord_y,tabuAlgSolution)