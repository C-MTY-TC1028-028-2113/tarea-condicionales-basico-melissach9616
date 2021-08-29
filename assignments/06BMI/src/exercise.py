import math 
def imc (pe, al): 
    indi = (pe / (al * al))
    return indi

def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    if altura > 0 and peso > 0:
        indice = imc(peso, altura)
        if indice < 20: 
            print('PESO BAJO')
        elif indice >= 20 and indice < 25: 
            print ('NORMAL')
        elif indice >= 25 and indice < 30: 
            print ('SOBREPESO')
        elif indice >= 30 and indice < 40: 
            print ('OBESIDAD')
        elif indice >= 40: 
            print ('OBESIDAD MORBIDA')
    else: 
        print('Revisa tus datos, alguno de ellos es erróneo.')

if __name__=='__main__':
    main()