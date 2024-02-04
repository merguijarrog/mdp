import sqlite3
import time
import json
from greedy import *
from tabu_search import *
from algorithms import *
from hill_climbing import *
from accuracy import *
from print_graphic import *

conexion = sqlite3.connect("MDP_results.sqlite")
cursor = conexion.cursor()
insert_db ='''INSERT INTO results (algorithm,problem_size,solution,accuracy,execution_time) VALUES (?, ?, ?, ?, ?)'''

def save_info(m_distance,m,size_problem,coord_x,coord_y):
    solutions = []
    
    start = time.time()
    solution_greedy = maxmin_greedy(m_distance, m)
    end = time.time()
    solutions.append(solution_greedy)
    execution_time=float(end-start)
    accuracy_greedy = solution_accuracy(solution_greedy,m_distance)
    solution_greedy_str = json.dumps([str(element) for element in solution_greedy]) #para guardar la solución en bd

    cursor.execute(insert_db, ("Algoritmo Greedy", size_problem, solution_greedy_str, accuracy_greedy, execution_time))
    conexion.commit()
    #print(solutionGreedy)
    #printGrap(coord_x,coord_y,solutionGreedy)

    start = time.time()
    solution_tabu = maxmin_greedy_tabu(m_distance,m,5) 
    end = time.time()
    execution_time=float(end-start)
    solutions.append(solution_tabu)
    accuracy_tabu = solution_accuracy(solution_tabu,m_distance)
    solution_tabu_str = json.dumps([str(element) for element in solution_tabu]) #para guardar la solución en bd

    cursor.execute(insert_db, ("Algoritmo Tabu", size_problem, solution_tabu_str,accuracy_tabu,execution_time))
    conexion.commit()
    #print(solutionTabu)
    #printGrap(coord_x,coord_y,solutionTabu)

    start = time.time()
    solution_grasp= grasp(m_distance,m,5) 
    end = time.time()
    solutions.append(solution_grasp)
    execution_time=float(end-start)
    accuracy_grasp = solution_accuracy(solution_grasp,m_distance)
    solution_grasp_str = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd

    cursor.execute(insert_db, ("Algoritmo GRASP", size_problem, solution_grasp_str,accuracy_grasp,execution_time))
    conexion.commit()
    
    solution_greedy_upgrade = hill_climbing(solution_greedy,m_distance)
    solutions.append(solution_greedy_upgrade)
    
    print_all_solutions(coord_x,coord_y,solutions)
    #print(solutionGrasp)
    #printGrap(coord_x,coord_y,solutionGrasp)