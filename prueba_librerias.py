import numpy as np
import matplotlib.pyplot as plt

# Crear un arreglo de NumPy
numeros = np.array([1, 2, 3, 4, 5])

print("Arreglo:", numeros)
print("Promedio:", np.mean(numeros))

# Crear un gráfico con Matplotlib
plt.plot(numeros, marker="o")
plt.title("Mi primer gráfico")
plt.xlabel("Posición")
plt.ylabel("Valor")
plt.grid(True)
plt.show()