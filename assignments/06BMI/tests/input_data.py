# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test Case 1
    (
        ["50", "1.7"],
        ["Peso en kg: ", "Altura en m: ", "PESO BAJO"],
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"]
    ),
    # Test Case 2
    (
        ["65", "1.7"],
        ["Peso en kg: ", "Altura en m: ", "NORMAL"],
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"]
    ),
    # Test Case 3
    (
        ["66", "1.54"],
        ["Peso en kg: ", "Altura en m: ", "SOBREPESO"], 
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"]
    ),
    # Test Case 4
    (
        ["95", "1.7"],
        ["Peso en kg: ", "Altura en m: ", "OBESIDAD"],
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"]
    ),
    # Test Case 5
    (
        ["120", "1.7"],
        ["Peso en kg: ", "Altura en m: ", "OBESIDAD MORBIDA"],
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos que genera el problema"]
    ),
    # Test Case 6
    (
        ["0", "1.54"],
        ["Peso en kg: ", "Altura en m: ", "Revisa tus datos, alguno de ellos es erróneo."],
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos limite o de error que genera el problema"]
    ),
    # Test Case 7
    (
        ["66", "-2"],
        ["Peso en kg: ", "Altura en m: ", "Revisa tus datos, alguno de ellos es erróneo."],
        ["No se cumple con el caso de prueba\nRevisa todos los posibles casos limite o de error que genera el problema"]
    )
]
