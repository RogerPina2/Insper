# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:05:09 2018

@author: Roger Pina
"""

import matplotlib.pyplot as plt

import numpy as np

from scipy.integrate import odeint





#Coeficiente de transferência convectiva entre a parede e o ar [W/m**2](para um isopor de 50mm)

hp=0.64

#Coeficiente de transferência convectiva entre o gelo e o ar interno

hg=2.25
  
#Área da superfície da parede em contato com o ar externo [m**2]

Ap=251.15


#Temperatura ambiente [°C]

Ta=27


#Temperatura da parede do isopor

Tp= -20

#Condutividade térmica do isopor [W/((m**2)*°C)]

Kp=0.033


#Área da superfície interna em contato com o gelo

Apg=874

#Área da superfície interna em contato com o ar

Apa=436.5

#Área da superfície do gelo em contato com o ar interno

Aga=185

#Espessura da parede de isopor [m]

dp=0.035


#Temperatura do gelo

Tg = -20

#Temperatura do ar (dentro do isopor)

Tar= -20

#Massa de gelo

mg=2


#Calor epecífico do gelo [cal/(g*°C)]

cg=0.550


#Massa de ar dentro do isopor

ma=1


#Calor específico do ar interno

ca=0.24




#Implementação das funções

def EqDif1(listaSolucoes1, tempo1):

    To1=listaSolucoes1[0]

    Qt1=((Ta-Tg)/((1/(hp*Ap))+(dp/(Kp*Apg))))

    Qar=hg*Aga*(Tar-Tg)

    dTdt=(Qt1+Qar)/(mg*cg)
    return dTdt

    

lisTempo = np.arange(0, 10000, 0.01)



#condição inicial: temperatura inicial = temperatura ambiente
ci=[Ta]



#executando o odeint

Solucao1=odeint(EqDif1, ci, lisTempo)



#conversão de unidades
lisTempoH=[t/3600 for t in lisTempo]


#plotando o gráfico como pedido
plt.plot(lisTempo, Solucao1)

plt.ylabel("Temperatura do gelo - graus Celsius")

plt.xlabel("Tempo (h)")

plt.grid(True)

plt.show()







def EqDif2(listaSolucoes2, tempo2):

    To2=listaSolucoes2[0]

    Qt2=((Ta-Tar)/((1/(hp*Ap))+(1/(hp*Apa))))

    Qar=hg*Aga*(Tar-Tg)

    dTdt=(Qt2+Qar)/(mg*cg)

    return dTdt





#executando o odeint

Solucao2=odeint(EqDif2, ci, lisTempo)



#conversão de unidades
lisTempoH=[t/3600 for t in lisTempo]



#plotando o gráfico como pedido

plt.plot(lisTempo, Solucao2)

plt.ylabel("Temperatura do ar - graus Celsius")

plt.xlabel("Tempo (h)")

plt.grid(True)

plt.show()