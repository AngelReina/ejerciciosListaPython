# Ejercicio 7 #
'''
Programa que declare tres listas 'lista1', 'lista2' de cinco enteros cada uno. 
Calcule lista3 = lista1 + lista2, por ejemplo 
           lista1 = [1, 2, 3, 4, 5]
        +  lista2 = [3, 2, 4, 5, 1]
           --------------------------
           lista3 = [4, 4, 7, 9, 6]
           
'''
#Importo el random
import random
# Creo una funcion de listas randoms
def listasRandom(n):
    lst=[]
    for i in range(0,n):
        num_random=random.randint(0,10)
        lst.append(num_random)
    return lst
# Lista 3
def lista_3(lst,lst2):
    lst_3=[]
    for i in range (len(lst)):
        lst_3.append(lst[i]+lst2[i])
    return lst_3
# Hago la lista 1
lista=listasRandom(5)
# Muestro la lista 1
print("  ",lista)
# Hago la lista 2
lista2=listasRandom(5)
# Muestro la lista 2
print("+ ",lista2)
# Decoración
print("--------------------")
# Muestro la lista 3
print("  ",lista_3(lista,lista2))
