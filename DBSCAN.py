import random
import math
import matplotlib
import matplotlib.pyplot as plt
angulo=math.pi*random.random()
5*math.cos(angulo)
class Punto():
    def __init__(self, radio,angulo):
        self.x=round(radio*math.cos(angulo),1)
        self.y=round(radio*math.sin(angulo),1)

def rango(punto, indice, epsilon,grupos,universo):
    elementos_cerca=1
    grupo=[]
    universo.pop(indice)
    grupo.append([punto[0], punto[1]])
    for punto in grupo:
        elementos_cerca=0
        i=0
        while i<len(universo):
            if abs(punto[0]-universo[i][0])<=epsilon or abs(punto[1]-universo[i][1])<=epsilon:
                d=round(distancia(universo[i][0], punto[0], universo[i][1], punto[1]),1)
                if d<=epsilon:
                    grupo.append([universo[i][0],universo[i][1]])
                    universo.pop(i)
                    elementos_cerca+=1
                    i-=1
            i+=1
    grupos.append(grupo)
    return grupo

def distancia(xc, xp, yc, yp):
    return math.sqrt((xc -xp)**2 + (yc - yp)**2)

def run():
    universo=[]
    grupos=[]
    for i in range(200):
        radio= 40 + random.randint(0,5)
        angulo=2*math.pi*random.random()
        punto=Punto(radio,angulo)
        universo.append([punto.x, punto.y])
    xp1=[p[0] for p in universo]
    yp1=[p[1] for p in universo] 
    
    for i in range(100):
        radio= 20 + random.randint(0,5)
        angulo=2*math.pi*random.random()
        punto=Punto(radio,angulo)
        universo.append([punto.x, punto.y])
    xp2=[p[0] for p in universo]
    yp2=[p[1] for p in universo] 
    xp=xp1+xp2
    yp=yp1+yp2
    plt.scatter(xp, yp)
    plt.show()
    while len(universo)>=1:
        indice=random.randint(0, len(universo)-1)
        punto=universo[indice]
        epsilon=10
        grupo=rango(punto, indice, epsilon,grupos,universo)
        xg=[p[0] for p in grupo]
        yg=[p[1] for p in grupo]
        plt.scatter(xg, yg)
    plt.show()
    
if __name__=='__main__':
    run()