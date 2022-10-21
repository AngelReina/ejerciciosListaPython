# Ejercicio 4 #
'''
Programa que declare una lista y la vaya llenando
de núemros hasta que introducimos un número negativo.
Entonces se debe imprmir el vector (sólo los elementos introducidos)
'''
# número infinito
positive_infnity = float('inf')
# Lista de todas los números
def listaTotal():
    lst=[]
    while(positive_infnity>0):
        try:
            num= int(input("Dime un número: "))
            if(num>=0):
               lst.append(num)
            else:
                print("Has introducido un número negativo")
                break
        except:
            print("Tiene que ser un número")
    return lst
#Muestro la lista total de todos los números
print(listaTotal())
