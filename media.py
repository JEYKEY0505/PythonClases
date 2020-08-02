import random
import math

def media(X):
    return sum(X)/len(X)

def varianza(X):
    mu=media(X)
    acumulador =0
    for x in X:
        acumulador+=(x-mu)**2

    return acumulador/len(X)

def desviacion(X):
    return math.sqrt(varianza(X))

if __name__=='__main__':
    X=[random.randint(9,12) for i in range(20)]
    mu = media(X)
    v=varianza(X)
    d=desviacion(X)
    print(X)
    print(mu)
    print(v)
    print(d)

