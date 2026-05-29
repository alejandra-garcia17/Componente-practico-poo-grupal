class Block14:

    titulo = "Unpacking en Python"

    concepto = """
    Unpacking = extraer valores de una estructura y asignarlos a variables individuales.

    Básico:
    a, b = [1, 2]
    a, b, c = (1, 2, 3)

    Con operador * (rest):
    primero, *resto, ultimo = [1, 2, 3, 4, 5]
    → primero=1, resto=[2,3,4], ultimo=5

    En funciones:
    numeros = [1, 2, 3]
    suma(*numeros)  → equivale a suma(1, 2, 3)

    Combinar diccionarios con **:
    dict1 = {"a": 1}
    dict2 = {"b": 2}
    combinado = {**dict1, **dict2}  → {"a":1, "b":2}

    En bucles:
    coordenadas = [(1,2), (3,4), (5,6)]
    for x, y in coordenadas:
        print(f"x={x}, y={y}")
    """

    def exercise1(self):

        return {
            "titulo": "Desempaquetar valores",

            "explicacion":
            """
            Podemos extraer valores de una tupla
            utilizando variables y el operador *.
            """,

            "codigo":
            """
first, *middle, last = (
    10,
    20,
    30,
    40
)

print(first)

print(middle)

print(last)
            """,

            "resultado":
            """
10

[20, 30]

40
            """
        }

    def exercise2(self):

        return {
            "titulo": "Pasar lista como argumentos",

            "explicacion":
            """
            El operador * permite enviar
            elementos de una lista
            como argumentos individuales.
            """,

            "codigo":
            """
def multiply(a, b, c):

    return a * b * c


numbers = [2, 3, 4]

result = multiply(*numbers)

print(result)
            """,

            "resultado":
            """
24
            """
        }

    def exercise3(self):

        return {
            "titulo": "Combinar diccionarios",

            "explicacion":
            """
            El operador ** permite combinar
            múltiples diccionarios.
            """,

            "codigo":
            """
dict1 = {
    "a": 1
}

dict2 = {
    "b": 2
}

merged = {
    **dict1,
    **dict2
}

print(merged)
            """,

            "resultado":
            """
{'a': 1, 'b': 2}
            """
        }