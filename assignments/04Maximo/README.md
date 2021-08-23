
![Tec de Monterrey](../../images/logotecmty.png)
# El mayor de 3 números

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    # Escribe el código adecuado para completar el programa
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))


if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema  

Realiza un programa que muestre el mayor de 3 números enteros x, y, z proporcionados por el usuario.

**NOTA:** NO puedes utilizar la función incorporada de Python: max(), debes hacerlo con condicionales.

**Entradas**  
El programa va a preguntar por tres **números enteros** uno en cada renglón.

**Salidas**  
El mayor de los tres números dados por el usuario.
 
## Ejemplos  

Ejemplo 1    

```plaintext
Ingresa el primer número: 5
Ingresa el segundo número: 8
Ingresa el tercer número: -3
8
```
Ejemplo 2

```plaintext
Ingresa el primer número: 5
Ingresa el segundo número: 1
Ingresa el tercer número: 12
12
```
**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest --tb=short`,
subela a tu repositorio en GitHub, con el proceso de commit + push.