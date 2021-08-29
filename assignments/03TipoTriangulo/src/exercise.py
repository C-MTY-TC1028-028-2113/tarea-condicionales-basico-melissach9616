import math
def validartriangulo (x, y):
    '''función validará que sea un triángulo'''
    mayor = x + y 
    return mayor 

def main():   
#ola
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...
    
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        sino = validartriangulo(lado1, lado2)
        if sino > lado3:
            if lado1 == lado2 and lado2 == lado3: 
                print('ES UN TRIANGULO EQUILATERO')
            elif lado1 == lado3 and lado3 != lado2: 
                print ('ES UN TRIANGULO ISOSCELES')
            elif lado2 == lado3 and lado3 != lado1: 
                print ('ES UN TRIANGULO ISOSCELES')
            elif lado1 == lado2 and lado2 != lado3: 
                print ('ES UN TRIANGULO ISOSCELES')
            elif lado1 != lado2 and lado2 != lado3: 
                print ('ES UN TRIANGULO ESCALENO')
        else: 
            print('NO ES TRIANGULO')
    else: 
        print('NO ES TRIANGULO')

if __name__=='__main__': 
    main()
