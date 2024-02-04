import matplotlib.pyplot as plt
def printGrap(coord_x,coord_y,solution):
    coord_solution_x=[]
    coord_solution_y=[]
    #creamos una lista con con las coordenadas de la solución
    for i in solution:
        coord_solution_x.append(coord_x[i])
        coord_solution_y.append(coord_y[i])

    plt.plot(coord_x,coord_y, "o",color="b")
    plt.plot(coord_solution_x,coord_solution_y, "o",color="r")
    
    print(coord_solution_x)
    print(coord_solution_y)
    plt.show()