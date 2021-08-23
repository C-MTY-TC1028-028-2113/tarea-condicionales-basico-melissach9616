![Tec de Monterrey](../../images/logotecmty.png)
# Tipo de Triángulo

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe el código adecuado para completar el programa
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))


if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  
Realiza un programa que sea útil para determinar si los números enteros X, Y y Z, proporcionados por el usuario, son medidas correctas para los lados de un triángulo y si lo son, debe decir si se trata de un triángulo Equilátero, Isósceles o Escaleno.

**NOTA:** X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:
Todos los números son mayores que cero
  * X + Y > Z   
  * X + Z > Y   
  * Y + Z > X  

es decir, la suma de dos de las medidas debe ser estrictamente mayor que la tercera.

El triángulo equilátero tiene 3 lados iguales, el isósceles tiene 2 lados iguales y el escaleno tiene los 3 lados diferentes.

**Entradas**  
El programa va a preguntar por tres **números enteros** uno en cada renglón.

**Salidas**  
Alguna de las siguientes palabras, según sea el tipo de triángulo para los valores dados: 
  * ES UN TRIANGULO EQUILATERO
  * ES UN TRIANGULO ISOSCELES  
  * ES UN TRIANGULO ESCALENO   
 
O bien, la frase: NO ES TRIANGULO si los valores introducidos por el usuario no corresponden a los lados de un triángulo, es decir no cumplen con alguna de las condiciones mencionadas arriba.

Escribe solamente uno de los 4 mensajes permitidos usando letras mayúsculas, no les pongas acentos en esta ocasión, escribe el mensaje exactamente como se describe.

## Ejemplos    
Ejemplo 1

```plaintext
Ingresa la medida del lado 1: 3
Ingresa la medida del lado 2: 3
Ingresa la medida del lado 3: 3
ES UN TRIANGULO EQUILATERO
```
Ejemplo 2

```plaintext
Ingresa la medida del lado 1: 4
Ingresa la medida del lado 2: 5
Ingresa la medida del lado 3: 6
ES UN TRIANGULO ESCALENO
```

Ejemplo 3
```plaintext
Ingresa la medida del lado 1: 3
Ingresa la medida del lado 2: 2
Ingresa la medida del lado 3: 3
ES UN TRIANGULO ISOSCELES
```

Ejemplo 4
```plaintext
Ingresa la medida del lado 1: 12
Ingresa la medida del lado 2: 3
Ingresa la medida del lado 3: 23
NO ES TRIANGULO
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.