# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test Case 1
    (
        ["2","3","9"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "NO ES TRIANGULO"],
        ["Revisa todas las opciones en las que se cumple que NO es un triangulo"]
    ),
    # Test Case 2
    (
        ["3", "3", "3"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO EQUILATERO"],
        ["Revisa todas las opciones en las que se cumple que es un Equilatero"]
    ),
    # Test Case 3
    (
        ["2", "3", "2"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ISOSCELES"],
        ["Revisa todas las opciones en las que se cumple que es un Isósceles"]
    ),
    # Test Case 4
    (
        ["2", "2", "3"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ISOSCELES"],
        ["Revisa todas las opciones en las que se cumple que es un Isósceles"]
    ),
    # Test Case 5
    (
        ["3", "2", "2"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ISOSCELES"],
        ["Revisa todas las opciones en las que se cumple que es un Isósceles"]
    ),
    # Test Case 6
    (
        ["2", "3", "4"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "ES UN TRIANGULO ESCALENO"],
        ["Revisa todas las opciones en las que se cumple que es un Escaleno"]
    ),
    # Test Case 7
    (
        ["3", "2", "-4"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "NO ES TRIANGULO"],  
        ["Revisa todas las opciones en las que se cumple que NO es un triangulo"]
    ),
    # Test Case 8
    (
        ["0", "3", "4"],
        ["Ingresa la medida del lado 1: ", "Ingresa la medida del lado 2: ", "Ingresa la medida del lado 3: ", "NO ES TRIANGULO"],
        ["Revisa todas las opciones en las que se cumple que NO es un triangulo"]
    )
    ]
