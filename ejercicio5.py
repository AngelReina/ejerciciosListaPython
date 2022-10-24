# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con
valores aleatorios (10 valores), y 
posterior ordene los elementos de menor a mayor
'''
#Importo el random
import random
# Lista de valores aleatorios
def lista_numeros():
    lst=[]
    for i in range(0,10):
        num_random=random.randint(0,100)
        lst.append(num_random)
    return lst
# Muestro la lista de todos los números
lista=lista_numeros()
print(lista)
# Pongo la lista de menor a mayor
lista.sort()
# Mustro la lista ordenada de menor a mayor
print(lista)
