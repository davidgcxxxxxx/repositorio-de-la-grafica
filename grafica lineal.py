#en esta parte del código se añaden las librerias necesarias para poder realizar la gráfica lineal, en este caso se utiliza la librería matplotlib.pyplot que es una de las más utilizadas para la creación de gráficos en Python.
import matplotlib.pyplot as plt
#aqui se añden los valos en X para la gráfica lineal, en este caso se añaden los valores del 1 al 6.
x = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
y = [10, 15, 13, 18, 22, 25,30,35,40,45,50,55,60,65,70,75,80, 85,90,95]


plt.plot(x, y, color="red", marker="o", linestyle="-", linewidth=2)


plt.title("Gráfica lineal de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")


plt.grid(True)


plt.show()