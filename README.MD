# Descripción

Este repositorio contiene todos los ficheros utilizados y generados para la realización del TFG, cuyo fichero está incluido en el mismo. 

# Contenido

El proyecto consta de los siguientes directorios y archivos principales:
- instances/: directorio que contiene los conjuntos de datos utilizados para evaluar los algoritmos. Están en formato txt.
- src/: directorio que contiene todos los archivos fuente de los diferentes algoritmos, los archivos para procesar los ficheros txt y un fichero para poder mostrar gráficas para representar el conjunto de datos.
    - main.py: fichero principal que procesa cada uno de los ficheros.
    - save_info.py: fichero que guarda la solución que devuelve cada uno de los algoritmos.
    - greedy.py: implementación del algoritmo Greedy.
    - tabu_algorithm.py: implementación del algoritmo Tabu Search.
    - hill_climbing.py: implementación de la búsqueda local.
    - grasp_algorithm.py: implementación del algoritmo GRASP.
    - print_graphic.py: permite representar el conjunto de datos y la solución obtenida para un algoritmo.
    - resultados.xlsx: excel que contiene todos los resultados obtenidos para cada uno de los algoritmos.
    - maxmin_v2.xlsx: Excel que contiene los resultados obtenidos con métodos exactos.
    - Comparación_resultados.xlsx: comparación de resultados entre los algoritmos Tabu y GRASP con los métodos exactos junto con el error relativo.
    - TFGMercedesGuijarro.pdf: contiene la memoria del trabajo.


# Instalación

Este proyecto ha sido desarrollado en Python 3.10, por lo que se recomienda tener instalada dicha versión en el equipo que ejecutará los algoritmos del repositorio. Para la instalación de dependencias se puede utilizar el fichero "requirements.txt":

```
pip install -r requirements.txt
```

También es posible realizar la instalación en un entorno virtual:
```python -m venv nombre_del_entorno 
.\nombre_del_entorno\Scripts\activate
pip install -r requirements.txt
```

Podemos listar las librerías instaladas de la siguiente manera:

```
pip list
```

# Ejecución

Para ejecutar el proyecto basta con situarnos en el directorio src y utilizar el comando: “python .\main.py”, con eso se ejecutarán cada uno de los algoritmos para las instancias que tenemos en la carpeta instances y se almacenará toda la información en el fichero resultados.