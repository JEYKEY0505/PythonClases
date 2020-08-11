import numpy as np
import random 
import matplotlib.pyplot as plt
import math
def main():
    posx=np.array([random.randint(1,11) for i in range(4)])
    posy=np.array([random.randint(1,11) for i in range(4)])
    print(posx)
    print(posy)
    plt.scatter(posx, posy)
    plt.show()
    while len(posx)>1:
        posx=list(posx)
        posy=list(posy)
        i=random.randint(0,(len(posx)-1))
        posx, posy=minimo(posx,posy,i)
        posx=np.array(posx)
        posy=np.array(posy)
        plt.scatter(posx, posy, color="red")
        plt.show()
        
    
    print(f'El punto se encuentra en la posicion x= {posx} y y= {posy}')
    

def distancia(x_a, y_a, x_s, y_s):
    return math.sqrt((x_a-x_s)**2 + (y_a-y_s)**2)
def nuevo(pos_x,pos_y,ahora, pos):
    x=(pos_x[ahora]+pos_x[pos])/2
    y=(pos_y[ahora]+pos_y[pos])/2
    return x, y
def minimo(pos_x,pos_y, ahora):
    d2=100
    for j in range(len(pos_x)):
        d=distancia(pos_x[ahora], pos_y[ahora], pos_x[j],pos_y[j])
        if j==ahora:
            continue
        if d<d2:
            d2=d
            pos=j
    nuevoX, nuevoY= nuevo(pos_x,pos_y,ahora, pos)
    if pos<ahora:
        pos_y.pop(ahora)
        pos_x.pop(ahora)
        pos_x.pop(pos)
        pos_y.pop(pos)
    else:
        pos_x.pop(pos)
        pos_y.pop(pos)
        pos_y.pop(ahora)
        pos_x.pop(ahora)
    
    pos_x.append(nuevoX)
    pos_y.append(nuevoY)
    return pos_x, pos_y


   
    
if __name__=='__main__':
    main()
    
