![Tec de Monterrey](../../images/logotecmty.png)
# Índice de masa corporal

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

Escribe un programa que calcule el **IMC** (Índice de Masa Corporal) de una persona, el cual se utiliza para determinar si la proporción de peso y altura es adecuada. El IMC se puede calcular utilizando la siguiente fórmula:

indice = peso / altura^2

Donde el peso debe darse en kilogramos y la altura en metros. La siguiente tabla muestra cómo se clasifican los diferentes rangos de índice:

| Rango de índice |  Descripción  |  
| :-------------: |:-------------:| 
|índice < 20      | PESO BAJO     |
|20 <= índice < 25| NORMAL        |
|25 <= índice < 30| SOBREPESO     |
|30 <= índice < 40| OBESIDAD      |
|índice >= 40     | OBESIDAD MORBIDA|

**Entradas**  
Dos números **flotantes** (peso y altura) uno en cada renglón y recibidos en este orden.  

**Salidas**  
Un **string** correspondiente a la descripción del índice de masa corporal, tal como se ve en la tabla, todo en mayúsculas.  
Debes de verificar que tanto el peso como la altura sean mayores a 0, en caso de que alguno sea 0 o menor, se debe mandar el siguiente mensaje de error: *Revisa tus datos, alguno de ellos es erróneo*.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Peso en kg: 53
Altura en m: 1.66
PESO BAJO
```
Ejemplo 2

```plaintext
Peso en kg: 65
Altura en m: 0
Revisa tus datos, alguno de ellos es erróneo.
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.