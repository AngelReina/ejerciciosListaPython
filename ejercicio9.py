import random
# Ejercicio 9 #

'''
Implementar la siguientes funciones 
        - sumaVector(<Lista>) devuelve <Entero>.
        - sumaVectorDeVector(<Lista>) devuelve <Entero>.
        
      
              
'''
# Listas random
def listasRandom(n):
    lst=[]
    for i in range(0,n):
        num_random=random.randint(0,10)
        lst.append(num_random)
    return lst
# Dado una lista con números enteros devolver la suma de todos ellos por ejemplo:
              # sumaVector([1,2,3]) -->  6
              # sumaVector([3,4]) --> 7
def sumaVector(lst):
    sumatotal=0
    for i in range(0,len(lst)):
        sumatotal= sumatotal+lst[i]
    return sumatotal
# Inicializo la lista random
lista= listasRandom(4)
# Muestro la lista random
print(lista)
# Muestro la lista de la suma de todos los valores
print("La suma de todos los valores de la lista es:", sumaVector(lista))

# Dado una lista con listas de números enteros devolver la suma de todos
# ellos por ejemplo:
              # sumaVectorDeVector([[1,2],[3,4],[5,6,7]]) --> 28
lst_lst=[[1,2],[3,4],[5,6,7]]
def sumaVectorDeVector(lst):
    resultado=0
    for i in lst:
        resultado= resultado+sumaVector(i)
    return resultado
# Mustro todos los vectores
print(lst_lst)
# Mustro la suma de todos los vectores
print("La suma de todos los vectores es", sumaVectorDeVector(lst_lst))
