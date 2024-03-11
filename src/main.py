from file_handler import *
from save_info import *
import matplotlib.pyplot as plt
import sqlite3

conexion = sqlite3.connect("MDP_results.sqlite")
cursor = conexion.cursor()
cursor.execute("""DROP TABLE IF EXISTS results""")
cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        algorithm TEXT NOT NULL,
        problem_size INTEGER,
        solution TEXT,
        execution_time REAL
    );
    ''')

allowed_size =[1000]

for file in range(2,3):
    for size in allowed_size:
        #lines = readFile('../ficheros/GKD_d_1_n2000_coor.txt')
        lines = readFile(f'C:/Users/Mer/Desktop/proyecto/mdp/ficheros/GKD_d_{file}_n{size}_coor.txt')

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
        if size < 500:
            m = round(size*8/100) 
        else:
            m = 10
        save_info(m_distance,m,size,coord_x,coord_y)

    
    