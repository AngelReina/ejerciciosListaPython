# Ejercicio 6 #
'''
Crea un programa que pida un número al usuario,
un número de mes ( por ejemplo, el 4). 
El programa dirá cuántos días tiene (por ejemplo 30) y
el nombre del mes. Debes usar listas. Nota: En una lista
podemos guardar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días
'''
# Lista de los meses
lst_meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
# Lista de los días
lst_dias=[31,28,31,30,31,30,31,31,30,31,30,31]
# Pido el numero del mes
mes = int(input("Introduce un mes (1-12):"))
if(1>mes or mes>12):
    print("Tienes que introducir un número entre el 1 y 12")
else:
    # Muestro el resultado
    print("El mes de",lst_meses[mes-1],"tiene",lst_dias[mes-1],"días.")
