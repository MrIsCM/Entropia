# ===============================
#
# 	Entropia de la informacion
#
# 			28/11/2022
#
# 			 Ismael CM
#
# ===============================

import numpy as np
import matplotlib.pyplot as plt
from random import randint

def flecha_temportal_noequiprobable(n, ciclos, k, l):
	# Inicio de las celdas en 0
	celdas = np.zeros(n)

	# Aleatoriamente se eligen celdas para ponerlas en 1
	for _ in range(n*8//10):
		p = randint(0,n-1)
		celdas[p]=1

	# Inicio de la suma de las celdas en 0 para cada iteracion
	suma = np.zeros(ciclos)

	# Variable auxiliar, numeros aleatorios para posteriormente compararlos con k y l
	dado = np.random.rand(ciclos)
	rand = np.random.randint(0, n-1, size=ciclos)
	for i in range(ciclos):
		
		if celdas[rand[i]]==0 and dado[i] <= k:
			celdas[rand[i]] = 1
		elif celdas[rand[i]]==1 and dado[i] <= l:
			celdas[rand[i]] = 0
		
		suma[i] = celdas.sum()

	
	return suma

def media(suma, lim_inf):
	med = 0
	med = sum(suma, lim_inf)/(len(suma)-lim_inf)
	return med

def graph(suma, n, k, l):
	
	plt.title(f"Macroestado con k={k}, l={l} y n={n}")
	plt.xlabel('Iteraciones')
	plt.ylabel('Macroestado: Suma')
	plt.ylim(0, n)
	plt.axhline(y=n*k/(k+l), color='r', linestyle='-')
	plt.plot(suma, linewidth=.8)
	plt.show()

def hist(suma, n):
	plt.title(f"Frecuencia de la suma para n={n}")
	plt.hist(suma, int(n/100))
	plt.show()

def write_data(suma, n, k, l):
	with open('Python/Results/Data.dat', 'w') as f:
		f.write(f"Dimension = {n}, Ciclos = {ciclos}, k = {k}, l = {l}\n")
		f.write(f"Valor teorico: {n*k/(k+l)}\n")
		f.write(f"Valor experimental total: {media(suma, 0)}\n")
		f.write(f"Valor experimental n/20: {media(suma, n/20)}\n")


# Numero de ciclos
# Un ciclo consiste en seleccionar una celda y cambiar el numero que hay dentro con probabilidad k, l (1, 0)
ciclos = int(1e7)

# Dimension del array de celdas
n = 10000

# Probabilidades de cambio de k: 0 --> 1, l: 1 --> 0
k = 0.5
l = 0.2

suma = flecha_temportal_noequiprobable(n, ciclos, k, l)

write_data(suma, n, k, l)
graph(suma, n, k, l)
hist(suma, n)