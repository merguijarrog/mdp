from file_handler import *
from print_graphic import *
from greedy import *
from tabu_search import *
from algorithms import *
from accuracy import *
import matplotlib.pyplot as plt
import sqlite3
import time
import json

conexion = sqlite3.connect("MDP_results.sqlite")
cursor = conexion.cursor()
cursor.execute("""DROP TABLE IF EXISTS results""")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        algorithm TEXT NOT NULL,
        problem_size INTEGER,
        solution TEXT,
        accuracy REAL,
        execution_time REAL
    );
    ''')

insert_db ='''INSERT INTO results (algorithm,problem_size,solution,accuracy,execution_time) VALUES (?, ?, ?, ?, ?)'''

allowed_size =[25,50,100,250,500,1000,2000]

for file in range(1,5):
    for size in allowed_size:
        #lines = readFile('../ficheros/GKD_d_1_n2000_coor.txt')
        lines = readFile(f'C:/Users/Mer/Desktop/DOCUMENTOS/proyecto/ficheros/GKD_d_{file}_n{size}_coor.txt')

        m_distance=[]
        coord_x=[]
        coord_y=[]
            
        for line in lines:
            line = line.rstrip()
            
            #en la primera línea tenemos el tamaño de nodos
            if(len(line.split(' ')) == 1):
                n=line.split(' ')
                n=int(n[0])
                for i in range(n): 
                    fila=[]
                    for j in range(n):
                        fila.append(0)
                    m_distance.append(fila) #añadimos tantas filas como pares de distancias entre elemenos hay
            
            if(len(line.split(' ')) == 2): # si en las líneas tenemos solo dos elementos indica las coordenadas del nodo
                row = line.split(' ')
                #guardamos la información en dos vectores para las coordenadas X y para las coordenadas y
                #de tal forma que para el nodo N sabremos que se encuentra en la coord_x[nodo_n] coord_y[nodo_n]
                coord_x.append(float(row[0]))
                coord_y.append(float(row[1]))
                
            if(len(line.split(' ')) == 3): #si en la línea tenemos tres elementos nos indica la distancia a la que se encuentran ese par de nodos
                row = line.split(' ')
                #guardamos info en la matriz de distancias como distancia[nodo_x][nodo_y] = distancia
                m_distance[int(row[0])][int(row[1])]= float(row[2]) 
                m_distance[int(row[1])][int(row[0])]= float(row[2]) 

        # Parámetro m: número de puntos a seleccionar - subconjunto
        m = 3
    
        start = time.time()
        solution_greedy = maxmin_greedy(m_distance, m)
        end = time.time()
        execution_time=float(end-start)
        accuracy_greedy = solution_accuracy(solution_greedy,m_distance)
        solution_greedy = json.dumps([str(element) for element in solution_greedy]) #para guardar la solución en bd

        cursor.execute(insert_db, ("Algoritmo Greedy", size, solution_greedy, accuracy_greedy, execution_time))
        conexion.commit()
        #print(solutionGreedy)
        #printGrap(coord_x,coord_y,solutionGreedy)

        start = time.time()
        solution_tabu = maxmin_greedy_tabu(m_distance,m,5) 
        end = time.time()
        execution_time=float(end-start)
        accuracy_tabu = solution_accuracy(solution_tabu,m_distance)
        solution_tabu = json.dumps([str(element) for element in solution_tabu]) #para guardar la solución en bd

        cursor.execute(insert_db, ("Algoritmo Tabu", size, solution_tabu,accuracy_tabu,execution_time))
        conexion.commit()
        #print(solutionTabu)
        #printGrap(coord_x,coord_y,solutionTabu)

        start = time.time()
        solution_grasp= grasp(m_distance,m,5) 
        end = time.time()
        execution_time=float(end-start)
        accuracy_grasp = solution_accuracy(solution_grasp,m_distance)
        solution_grasp = json.dumps([str(element) for element in solution_grasp]) #para guardar la solución en bd

        cursor.execute(insert_db, ("Algoritmo GRASP", size, solution_grasp,accuracy_grasp,execution_time))
        conexion.commit()
        #print(solutionGrasp)
        #printGrap(coord_x,coord_y,solutionGrasp)

    
    