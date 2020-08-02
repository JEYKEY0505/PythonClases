import random
from bokeh.plotting import figure, show
def tirar_dados(dados):
    suma_de_dados=[]
    for i in range(dados):
        d1=random.choice([1,2,3,4,5,6])
        d2=random.choice([1,2,3,4,5,6])
        suma_de_dados.append(d1+d2)
    return suma_de_dados

def main(dados, repeticiones):
    suma=[]
    for i in range(repeticiones):
        secuencia= tirar_dados(dados)
        suma.append(secuencia)
    
    tiros_12=0
    for tiro in suma:
        if 12 in tiro:
            tiros_12+=1
        probabilidad= tiros_12/repeticiones
    
    print(f'La probabilidad de que ambos dados sumen 12 es {probabilidad}')

if __name__=='__main__':
    dados=int(input('Cuantos veces va a tirar los dos dados: '))
    repeticiones= int(input('Cuantas veces vas a repetir:'))

    main(dados, repeticiones)


   