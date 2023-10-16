import random
import time
import matplotlib.pyplot as plt

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivotardo = arr[random.randint(0, len(arr) - 1)]
    menor = [n for n in arr if n < pivotardo]
    igual = [n for n in arr if n == pivotardo]
    grandote = [n for n in arr if n > pivotardo]

    return quick(menor) + igual + quick(grandote)

arreglos = []
for _ in range(100):
    tam = random.randint(1, 1000)
    array = [random.randint(1, 10000) for _ in range(tam)]
    print(array)
    print()
    print("Omaga")
    arreglos.append(array)

xd = []
for arr in arreglos:
    initiem = time.time()
    sorted_array = quick(arr.copy())  
    fintiem = time.time()
    xd.append(fintiem - initiem)

plt.plot(range(1, 101), xd, marker='o')
plt.xlabel('Número del arreglos')
plt.ylabel('El timepo de ejecución en segundos')
plt.title('Tiempo de ejecución del algoritmo de Quicksort')
plt.show()
