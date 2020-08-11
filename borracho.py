import random
from bokeh.plotting import figure, output_file, show

class Borracho:
    def __init__(self, name):
        self.name= name

class Borracho_tradicional(Borracho):
    def __init__(self, name):
        super().__init__(name)
    def camina(self):
        return random.choice([(0,1), (0,-1), (1,0), (-1,0)])

class Coordenada:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    
    def caminar(self, delta_x, delta_y):
        self.x+=delta_x
        self.y+=delta_y
        return self.x, self.y


if __name__=='__main__':
    fig=figure()
    origen_x=0
    origen_y=0
    pasos=int(input('Cuantos pasos quiere dar: '))
    memo_x=[]
    memo_y=[]
    ebrio= Borracho_tradicional('Edwin')
    coordenada= Coordenada(origen_x,origen_y)
    for i in range(pasos):
        memo_x.append(origen_x)
        memo_y.append(origen_y)
        delta_x, delta_y=ebrio.camina()
        origen_x, origen_y= coordenada.caminar(delta_x, delta_y)

    Max_x=max(memo_x)
    Max_y=max(memo_y)
    distancia= (Max_x**2 + Max_y**2)**0.5
    print(f'La distancia mas alejada a la que llego fue {distancia}')
    fig.line(memo_x, memo_y, line_width=1)
    show(fig)
    

