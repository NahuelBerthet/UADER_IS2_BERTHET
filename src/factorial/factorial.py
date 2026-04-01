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
        # -hasta
        if entrada.startswith("-"):
            fin = int(entrada[1:])
            return 1, fin
        
        # desde-
        if entrada.endswith("-"):
            inicio = int(entrada[:-1])
            return inicio, 60
        
        # desde-hasta
        if "-" in entrada:
            partes = entrada.split("-")
            inicio = int(partes[0])
            fin = int(partes[1])
            return inicio, fin
        
        # Caso número unico
        num = int(entrada)
        return num, num
    
    except ValueError:
        print("Entrada inválida. Debe ser un número o un rango válido (ej. 4-8, -10, 20-).")
        sys.exit()

# Pedir argumento
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 20-): ")
else:
    entrada = sys.argv[1]

inicio, fin = obtener_rango(entrada)

# Validar
if inicio > fin:
    print("El rango es inválido: el inicio no puede ser mayor que el fin.")
    sys.exit()

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
