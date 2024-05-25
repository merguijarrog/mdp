from save_info import *
import math
import os

def readFile(file):
    file = open(file,'r')
    with file as f:
        lines= f.readlines()
    file.close()
    return lines

if os.path.exists('resultados.xlsx'):
        os.remove('resultados.xlsx')
        
allowed_size =[25,50,100,250,500,1000]
    
for size in allowed_size:
    values=[math.ceil(size*0.1)] # si queremos añadir otra m: ,(math.ceil(size*0.1))*2 
    for m in values:
        for file in range(1,11):
            relative_path = os.path.join('../instances', f'GKD_d_{file}_n{size}_coor.txt')
            lines = readFile(relative_path)

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

            # Parámetro m: número de puntos a seleccionar
            save_info(m_distance,m,size,f'GKD_d_{file}_n{size}_coor.txt',coord_x,coord_y)