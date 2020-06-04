import numpy as np
import matplotlib.pyplot as plt

L = 0.6

dX = 0.1
dY = dX

nX = 7
nY = nX

t = 1000000
dT = 52
nT = int(t/dT) + 1  

T = np.zeros(shape=(nT,nY,nX))

for e in range(nY):
    T[0][e][0] = 10
    T[0][e][-1] = 50

T[0][0] = 100

k = 230
c = 897
p = 2700

alpha = k/(c*p)

#=====================================

F0 = alpha*(dT/dX**2)

print(F0)

final = -1

lista_erro = []

for p in range(1,nT):

    erro = 0
    tol = 1e-8

    for j in range(nY):
        for i in range(nX):

            if i == 0 or j == 0 or i == (nX-1):
                T[p][j][i] = T[p-1][j][i]

            elif j == (nY-1):
                T[p][j][i] = F0 * (T[p-1][j][i+1] + T[p-1][j][i-1] + 2*T[p-1][j-1][i]) + (1 - 4*F0)*T[p-1][j][i]

            else:
                T[p][j][i] = F0 * (T[p-1][j][i+1] + T[p-1][j][i-1] + T[p-1][j+1][i] + T[p-1][j-1][i]) + (1 - 4*F0)*T[p-1][j][i]

            if T[p][j][i] != 0:
                aux = abs((T[p][j][i] - T[p-1][j][i])/(T[p][j][i]))
                
                lista_erro.append(aux)
                if aux > erro:
                    erro = aux

    if erro < tol:
        final = p
        break

print(erro)

'''
for e in T[final]:
    lista = []
    for f in e:
        lista.append(float("{:.4f}".format(f)))
    print(lista)

'''
print('')

print('\n'.join([' '.join(['{:8.4f}'.format(item) for item in row]) for row in T[final]]))

print(final)

#print(lista_erro)