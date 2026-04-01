#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*



import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

def obtener_rango(entrada):
    try:
        partes = entrada.split("-")
        if len(partes) == 2:
            inicio = int(partes[0])
            fin = int(partes[1])
            return inicio, fin
        else:
            # Si solo se pasa un numero
            num = int(entrada)
            return num, num
    except ValueError:
        print("Entrada invalida. Debe ser un numero o un rango desde-hasta (ej. 4-8).")
        sys.exit()

# Pedir argumento 
if len(sys.argv) < 2:
    entrada = input("Ingrese un numero o un rango (ej. 4-8): ")
else:
    entrada = sys.argv[1]

inicio, fin = obtener_rango(entrada)

# Calcular factoriales en el rango
for n in range(inicio, fin + 1):
    resultado = factorial(n)
    if resultado is not None:
        print(f"Factorial {n}! es {resultado}")


#* codigo viejo
# if len(sys.argv) < 0: 
#    print("Debe informar un número!")
#    sys.exit()
# num=int(sys.argv[1])
