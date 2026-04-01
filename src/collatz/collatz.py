import matplotlib.pyplot as plt

def collatz_iterations(n):
    """Devuelve la cantidad de pasos que tarda en llegar a 1 según la conjetura de Collatz."""
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

# Calcular para números entre 1 y 10000
numeros = list(range(1, 10001))
iteraciones = [collatz_iterations(n) for n in numeros]

# Crear gráfico
plt.figure(figsize=(12, 6))
plt.scatter(iteraciones, numeros, s=5, color="blue")
plt.title("Conjetura de Collatz (3n+1) entre 1 y 10000")
plt.xlabel("Número de iteraciones hasta converger")
plt.ylabel("Número inicial n")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
