import random

def construir_solucion(matriz_distancias, tamano_subconjunto):
    nodos = list(range(len(matriz_distancias)))
    solucion_parcial = []
    for _ in range(tamano_subconjunto):
        # Selecciona un nodo aleatorio que no esté en la solución parcial actual
        nodo = random.choice(list(set(nodos) - set(solucion_parcial)))
        solucion_parcial.append(nodo)
    return solucion_parcial

def distancia_minima(matriz_distancias, subconjunto_nodos):
    min_distancia = float('inf')
    for i in range(len(subconjunto_nodos)):
        for j in range(i + 1, len(subconjunto_nodos)):
            distancia = matriz_distancias[subconjunto_nodos[i]][subconjunto_nodos[j]]
            min_distancia = min(min_distancia, distancia)
    return min_distancia

def busqueda_local(matriz_distancias, solucion_parcial):
    mejor_solucion = solucion_parcial[:]
    mejor_distancia = distancia_minima(matriz_distancias, solucion_parcial)

    for i in range(len(solucion_parcial)):
        for j in range(i + 1, len(solucion_parcial)):
            # Intercambia los nodos i y j
            nueva_solucion = solucion_parcial[:]
            nueva_solucion[i], nueva_solucion[j] = nueva_solucion[j], nueva_solucion[i]
            nueva_distancia = distancia_minima(matriz_distancias, nueva_solucion)
            if nueva_distancia > mejor_distancia:
                mejor_solucion = nueva_solucion[:]
                mejor_distancia = nueva_distancia

    return mejor_solucion

def GRASP(matriz_distancias, tamano_subconjunto, iteraciones):
    mejor_solucion = []
    mejor_distancia = 0

    for _ in range(iteraciones):
        solucion_parcial = construir_solucion(matriz_distancias, tamano_subconjunto)
        solucion_mejorada = busqueda_local(matriz_distancias, solucion_parcial)
        distancia_actual = distancia_minima(matriz_distancias, solucion_mejorada)
        if distancia_actual > mejor_distancia:
            mejor_solucion = solucion_mejorada[:]
            mejor_distancia = distancia_actual

    return mejor_solucion