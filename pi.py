import random
import math
def tirar_agujas(n_agujas):
    circulo_inside= 0

    for i in range(n_agujas):
        x=random.random()*random.choice([1,-1])
        y=random.random()*random.choice([1,-1])
        distancia=math.sqrt(x**2 + y**2)

        if distancia <=1:
            circulo_inside+=1
        
    
    return 4*circulo_inside/n_agujas

if __name__=='__main__':
    n_agujas=int(input('Cuantas agujas vas a lanzar: '))
    pi=tirar_agujas(n_agujas)
    print(pi)