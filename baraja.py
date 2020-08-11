import random
import collections
PALOS= ['espada', 'corazon ', 'diamante', 'trebol']
VALORES= ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    barajas=[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))
    
    return barajas

def obtener_mano(barajas, tamano):

    mano=random.sample(barajas, tamano)
    return mano

def main(tamano, intentos):
    barajas=crear_baraja()
    manos=[]
    for i in range(intentos):
        mano=obtener_mano(barajas,tamano)
        manos.append(mano)
    
    pares=0
    for mano in manos:
        valores=[]
        for carta in mano:
            valores.append(carta[1])
        
        counter=dict(collections.Counter(valores))
        
        for val in counter.values():
            if val==3:
                pares+=1
                break

    probabilidad_par=pares/intentos  
    print(f'La probabilidad de obtener un par en una baraja de {tamano} es {probabilidad_par}')  


if __name__=='__main__':
    tamano=int(input('Cual es cartas quieres: '))
    intentos=int(input('Cuantas repeticiones quieres: '))
    main(tamano, intentos)