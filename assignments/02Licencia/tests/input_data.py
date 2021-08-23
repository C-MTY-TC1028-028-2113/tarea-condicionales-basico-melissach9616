# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
        (
            ["19", "n"],
            ["Ingresa tu edad: ","¿Tienes identificación oficial? (s/n): ", "No cumples requisitos" ],
            ["Revisa que pasa si cumples edad, pero no con credencial"]
        ),
    # Test case 2
        ( 
            ["20", "s"],
            ["Ingresa tu edad: ","¿Tienes identificación oficial? (s/n): ", "Trámite de licencia concedido"],
            ["Revisa qué debe pasar si cumples con los dos requisitos"]
        ),
    # Test case 3
        (
            ["18", "r"],
            ["Ingresa tu edad: ","¿Tienes identificación oficial? (s/n): ", "Respuesta incorrecta"],
            ["Revisa qué debes pasar si tecleas de manera incorrecta la respuesta de s/n"]
        ),
    # Test case 4
        (
            ["0"],
            ["Ingresa tu edad: ", "Respuesta incorrecta"],
            ["Revisa qué debe pasar si te mandan un dato inválido para la edad"]
        ),
    # Test case 5
        (
            ["12"],
            ["Ingresa tu edad: ", "No cumples requisitos"],
            ["Revisa qué deb pasar si es un menor de edad"]
        )
    ]
