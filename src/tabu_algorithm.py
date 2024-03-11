import random
import numpy as np

"""
    Calcula la distancia mínima entre los nodos seleccionados en el subconjunto.
"""
def calcular_distancia_minima(matriz_distancias, subconjunto):
    distancia_minima = float('inf')
    for i in range(len(subconjunto)):
        for j in range(i+1, len(subconjunto)):
            distancia = matriz_distancias[subconjunto[i]][subconjunto[j]]
            distancia_minima = min(distancia_minima, distancia)
    return distancia_minima

"""
    Implementación del algoritmo de búsqueda tabú para seleccionar un subconjunto de nodos
    que maximice la distancia mínima entre ellos.
"""
def buscar_subconjunto_optimo(matriz_distancias, n, max_iter=1000, tam_tabu=10):
    num_nodos = len(matriz_distancias)
    
    # Inicialización
    solucion_actual = random.sample(range(num_nodos), n)
    mejor_solucion = solucion_actual[:]
    mejor_distancia_minima = calcular_distancia_minima(matriz_distancias, mejor_solucion)
    lista_tabu = []

    # Bucle principal
    iteracion = 0
    while iteracion < max_iter:
        # Generar vecinos
        vecinos = []
        for i in range(num_nodos):
            if i not in solucion_actual:
                vecino = solucion_actual[:]
                vecino[random.randint(0, n-1)] = i
                vecinos.append(vecino)

        # Evaluar vecinos y seleccionar el mejor no tabú
        mejor_vecino = None
        mejor_distancia = 0
        for vecino in vecinos:
            distancia = calcular_distancia_minima(matriz_distancias, vecino)
            if distancia > mejor_distancia and vecino not in lista_tabu:
                mejor_vecino = vecino
                mejor_distancia = distancia

        # Actualizar solución actual y lista tabú
        if mejor_vecino is not None:
            solucion_actual = mejor_vecino[:]
            lista_tabu.append(mejor_vecino)
            if len(lista_tabu) > tam_tabu:
                lista_tabu.pop(0)

        # Actualizar mejor solución encontrada
        distancia_actual = calcular_distancia_minima(matriz_distancias, solucion_actual)
        if distancia_actual > mejor_distancia_minima:
            mejor_solucion = solucion_actual[:]
            mejor_distancia_minima = distancia_actual

        iteracion += 1

    return mejor_solucion