![Tec de Monterrey](../../images/logotecmty.png)
# Licencia

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python

def main():
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "



if __name__ == '__main__':
    main()
```

Recuerda, la línea `# Escribe el código adecuado para completar el programa` es un comentario, el programa la va a ignorar al ejecutarse.

## Definición del problema
Una persona puede obtener su licencia de manejo si es mayor de edad y tiene identificación oficial.

Escribe un programa en Python que lea la edad de una persona y si tiene (s/n) identificación oficial.

De salida debe mostrar Si  puede obtener su licencia o No la puede obtener.

**Entradas**
El programa va a preguntar por:
- la edad de la persona, debe ser un entero positivo.
- si tiene identificación o no. Debe ser un string, que contenga las letras "s" o "n". Puede contestar con mayúsculas.

**Salidas**
Añade el código necesario para que el programa imprima:
- **Trámite de licencia concedido** si la edad es mayor o igual a 18 y tiene identificación oficial
- **No cumples requisitos** si no cumple con los requisitos para la licencia
- Si la edad es negativa o el usuario ingresó cualquier otro caracter que no sea s o n cuando pides la identificación, debe mostrar el mensaje **Respuesta incorrecta**

La salida del programa debe de ser exactamente de la siguiente forma:

## Ejemplos
Ejemplo 1

```plaintext
Ingresa tu edad: 19
¿Tienes identificación oficial? (s/n): s
Trámite de licencia concedido
```
Ejemplo 2

```plaintext
Ingresa tu edad: 19
¿Tienes identificación oficial? (s/n): n
No cumples requisitos
```

Ejemplo 3
```plaintext
Ingresa tu edad: 12
No cumples requisitos
```

Ejemplo 4
```plaintext
Ingresa tu edad: 20
¿Tienes identificación oficial? (s/n): g
Respuesta incorrecta
```

**Nota:** No te preocupes por esta parte del código
`if __name__ == '__main__':` por el momento. No la vamos a necesitar para
este programa, pero es una buena práctica incluirla y quedará más
claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `python -m pytest --tb=short -v`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
