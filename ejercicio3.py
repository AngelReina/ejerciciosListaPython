# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas
obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media,
la nota más alta que ha sacado y la menor
'''
# número infinito
positive_infnity = float('inf')
# Número menos infinito
negative_infnity = float('-inf')
# Lista de todas las notas
def listaDeNotas():
    lst=[]
    cont=0
    while(cont<5):
        try:
            nota= int(input("Dime tu nota: "))
            if(0<=nota<=10):
               lst.append(nota)
               cont=cont+1
            else:
                print("La nota debe ser un número entre el 0 y 10")
        except:
            print("Tiene que ser un número")
    return lst
# Funcion para la nota media
def NotaMedia(lst):
    media=0
    for i in lst:
        media= media+i
    media=media/len(lst)
    return media
# Funcion para el numero menor
def notamayor(lst):
    cont=negative_infnity
    for i in lst:
        if(cont>i):
            cont=cont
        else:
           cont=i
    return cont
# Funcion para el numero menor
def notamenor(lst):
    cont= positive_infnity
    for i in lst:
        if(cont<i):
            cont=cont
        else:
           cont=i
    return cont
#Muestro la lista total de notas
lista = listaDeNotas()
print(lista)
#Muestro la nota media de notas
print("La nota media es: ",NotaMedia(lista))
#Muestro el número mayor de las notas
print(notamayor(lista),"Es el número mayor")
#Muestro el número menor de las notas
print(notamenor(lista),"Es el número menor")
