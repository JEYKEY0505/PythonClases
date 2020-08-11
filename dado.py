import random
import collections
from bokeh.plotting import figure, show
from bokeh.layouts import row
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
    temporal=[]
    for indice in suma:
        temporal.append(indice[0])
    counter1=dict(collections.Counter(temporal))
    x=[key for key in counter1.keys()]
    y=[value for value in counter1.values()]
    print(x)
    print(y)
    # fig.line(x, y, line_width=2)
   

if __name__=='__main__':
    dados=int(input('Cuantos veces va a tirar los dos dados: '))
    repeticiones= int(input('Cuantas veces vas a repetir:'))

    main(dados, repeticiones)


   