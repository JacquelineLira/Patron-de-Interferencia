import numpy as np
from matplotlib import pyplot as plt

# inicialización de variables
D = 1 # distancia entre la pared y la pantalla
a = 4 # intensidad
d = 1 # distancia entre las dos rendijas
k = 0.5 # numero real

# puntos en la pantalla
x = np.linspace(-25, 20,10001)

# intensidad de la onda en los puntos de x
a_1 = a / pow(pow(D, 2) + pow(x - d, 2), 1 / 4)
a_2 = a / pow(pow(D, 2) + pow(x + d, 2), 1 / 4)

# valor de phi para las ondas
phi_1 = k * pow(pow(D, 2) + pow(x - d, 2), 1 / 2)
phi_2 = k * pow(pow(D, 2) + pow(x + d, 2), 1 / 2)

# elevación de las ondas
elv_1 = a_1 * np.cos(phi_1)
elv_2 = a_2 * np.cos(phi_2)

# amplitud de la onda
amp = pow(pow(elv_1, 2) + pow(elv_2, 2) + 2 * elv_1 * elv_2 * np.cos(phi_1 - phi_2), 1 / 2)
 
plt.plot(x, elv_1, 'r', label = "Fuente 1")
plt.plot(x, elv_2, 'b', label = "Fuente 2")
plt.title("Experimento de las rendijas")
plt.xlabel("Distancia del centro")
plt.ylabel("Amplitud de las ondas individuales")
plt.legend(loc = 'best')
plt.show()

plt.plot(x, amp, 'g', label = "Conjunta")
plt.title("Patrón de Interferencia")
plt.xlabel("Distancia del centro")
plt.ylabel("Amplitud de la onda conjunta")
plt.legend(loc = 'best')
plt.show()