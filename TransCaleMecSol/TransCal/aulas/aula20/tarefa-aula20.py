import numpy as np
import matplotlib.pyplot as plt

L = 0.4

nX = 10
nY = 10

dX = L/(nX-1)
dY = dX

t = 10
dT = 1e-3
nT = int(t/dT) + 1  

T = np.zeros(shape=(nT,nY,nX))

T[0][0] = 150
for e in range(nY):
    T[0][e][-1] = 50

T[0][0][-1] = 0
T[0][-1] = 0

k = 0.23
c = 897
p = 2.7 * 1e-6

alpha = k/(c*p) * 1e-6

#=====================================

F0 = alpha*(dT/dX**2)
final = -1

for p in range(1,nT):

    erro = 0
    tol = 1e-8

    for j in range(nY):
        for i in range(nX):

            if j == 0 or j == (nY-1) or i == (nX-1):
                T[p][j][i] = T[p-1][j][i]

            elif i==0:
                T[p][j][i] = F0 * (2*T[p-1][j][i+1]+ T[p-1][j+1][i] + T[p-1][j-1][i]) + (1 - 4*F0)*T[p-1][j][i]

            else:
                T[p][j][i] = F0 * (T[p-1][j][i+1] + T[p-1][j][i-1] + T[p-1][j+1][i] + T[p-1][j-1][i]) + (1 - 4*F0)*T[p-1][j][i]

            if T[p][j][i] != 0:
                aux = abs((T[p][j][i] - T[p-1][j][i])/(T[p][j][i]))
                    
                if aux > erro:
                    erro = aux

print(erro)

for e in T[final]:
    lista = []
    for f in e:
        lista.append(float("{:.4f}".format(f)))
    print(lista)