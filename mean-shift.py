import matplotlib
import matplotlib.pyplot as plt
import math

class Punto():
    def __init__(self,la,al,La,Al):
        self.x=random.randint(la,La)
        self.y=random.randint(al,Al)

class Centro():
    def __init__(self,k,j):
        self.x=5*(k+1)
        self.y=5*(j+1)

def distancia(xc, yc, xp, yp):
    return math.sqrt((xc -xp)**2 + (yc - yp)**2)

def media(grupo):
    xm=0
    ym=0
    for i in grupo:
        xm+=i[0]
        ym+=i[1]
    if len(grupo)==0:
        return 0, 0
    else:
        return xm/len(grupo), ym/len(grupo)
    
if __name__=='__main__':
    universo=[]
    centros=[]
    for i in range(40):
        punto=Punto(0,0,30,30)
        universo.append([punto.x, punto.y])
    for i in range(40):
        punto=Punto(0,80,20,100)
        universo.append([punto.x, punto.y])
    for i in range(40):
        punto=Punto(80,0,100,20)
        universo.append([punto.x, punto.y])
    for i in range(40):
        punto=Punto(60,60,100,100)
        universo.append([punto.x, punto.y])
    
    x=[p[0] for p in universo]
    y=[p[1] for p in universo]
    plt.scatter(x,y)
    plt.show()
    
    for i in range(4):
        for j in range(4):
            centro=Centro(i,j)
            centros.append([centro.x, centro.y])
    
    xc=[p[0] for p in centros]
    yc=[p[1] for p in centros]
    plt.scatter(xc, yc)
    plt.show()
    centros_m=[]
    for centro in centros:
        grupo=[]
        for punto in universo:
            if punto[0]<=centro[0] and punto[1]<=centro[1]:
                rango= distancia(centro[0], centro[1], punto[0], punto[1])
                if rango<=20:
                    grupo.append([punto[0], punto[1]])
        xm, ym=media(grupo)
        centros_m.append([xm, ym])

get_order()




