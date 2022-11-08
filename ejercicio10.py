import random
# Ejercicio 10 #
'''
Crear un programa que cree un matriz de 5 x 5 con números aleatorios
'''

def generaListaAleatoria(n):
    lst=[]
    for i in range(0,n):
             num_random=random.randint(0,10)
             lst.append(num_random)
    return lst
    
def generaMatrizAleatoria(n):
    lst=[]
    for i in range(0,n):
        lst.append(generaListaAleatoria(n))
    return lst



'''
Crear dos matrices y realize la suma
'''
def SumaMatrices(matriz,matriz2):
    print("Matriz A:")
    print(matriz)
    print("Matriz B:")
    print(matriz2)
    print("Suma de las matrices")
    matriz_suma=[]
    for i in range(0,len(matriz)):
        lst_suma=[]
        for x in range(0,len(matriz[i])):
            suma=(matriz[i][x] + matriz2[i][x])
            lst_suma.append(suma)
        matriz_suma.append(lst_suma)
    return matriz_suma

matriz=generaMatrizAleatoria(5)
matriz2=generaMatrizAleatoria(5)
print(SumaMatrices(matriz,matriz2))
'''
Crear dos matrices y realize la resta
'''
def RestaMatrices(matriz,matriz2):
    matriz_resta=[]
    for i in range(0,len(matriz)):
        lst_resta=[]
        for x in range(0,len(matriz[i])):
            resta=(matriz[i][x] - matriz2[i][x])
            lst_resta.append(resta)
        matriz_resta.append(lst_resta)
    return matriz_resta
print("Resta de matrices")
print(RestaMatrices(matriz,matriz2))
'''
producto de un número por una matriz
'''
def ProductonumeroMatriz(matriz):
    matriz_producto=[]
    producto=int(input("Dime el producto: "))
    for i in range(0,len(matriz)):
        lst_producto=[]
        for x in range(0,len(matriz[i])):
            total= producto*matriz[i][x]
            lst_producto.append(total)
        matriz_producto.append(lst_producto)
    return matriz_producto
print("Producto de un número por una matriz")
print(ProductonumeroMatriz(matriz))
'''
Multiplicación de dos matrices
'''
