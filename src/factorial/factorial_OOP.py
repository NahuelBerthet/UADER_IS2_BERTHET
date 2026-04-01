import sys

class Factorial:
    def __init__(self):
        pass

    def calcular(self, num):
        """Método auxiliar para calcular el factorial de un número"""
        if num < 0:
            print(f"Factorial de {num} no existe (número negativo)")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, minimo, maximo):
        """Calcula factoriales entre minimo y maximo"""
        resultados = {}
        for n in range(minimo, maximo + 1):
            resultados[n] = self.calcular(n)
        return resultados


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

        # Caso numero único
        num = int(entrada)
        return num, num

    except ValueError:
        print("Entrada inválida. Debe ser un número o un rango válido (ej. 4-8, -10, 20-).")
        sys.exit()


if __name__ == "__main__":
    # Pedir Argumento
    if len(sys.argv) < 2:
        entrada = input("Ingrese un número o un rango (ej. 4-8, -10, 20-): ")
    else:
        entrada = sys.argv[1]

    minimo, maximo = obtener_rango(entrada)

    if minimo > maximo:
        print("El rango es inválido: el inicio no puede ser mayor que el fin.")
        sys.exit()

    # Crear y ejecutar
    f = Factorial()
    resultados = f.run(minimo, maximo)

    # Resultado
    for n, valor in resultados.items():
        if valor is not None:
            print(f"Factorial {n}! es {valor}")
