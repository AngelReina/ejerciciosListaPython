# Ejercicio 2
'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso,
y muestra sus elementos por la pantalla.
'''
# Función de La lista de Caracteres

def listaDeCaracter():
    lst=[]
    for i in range(0,5):
       caracter= str(input("Dime un caracter: "))
       lst.append(caracter)
    return lst

# Función de La lista de Caracteres Inversa

def listaDeCaracterInversa(lst):
    lst.reverse()
    return lst

# Muestro el resultado

lista=listaDeCaracter()
print(lista)
print(listaDeCaracterInversa(lista))
