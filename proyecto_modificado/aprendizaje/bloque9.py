class Block9:

    titulo = "Tuplas en Python"

    concepto = """
    Las tuplas son INMUTABLES: no se pueden modificar tras crearse.
    Son más rápidas que las listas y se usan cuando los datos no deben cambiar.

    Métodos disponibles (solo 2):
    count(x) → contar ocurrencias de x
    index(x) → posición de x

    Unpacking (desempaquetado):
    a, b, c = (1, 2, 3)
    primero, *resto, ultimo = (1, 2, 3, 4, 5)
    → primero=1, resto=[2,3,4], ultimo=5

    Iteración con tuplas:
    coordenadas = [(1,2), (3,4)]
    for x, y in coordenadas:
        print(f"x={x}, y={y}")

    Conversión:
    Para modificar una tupla → convertir a lista, modificar y volver a tupla.
    lista_temp = list(tupla)
    lista_temp.append(6)
    nueva_tupla = tuple(lista_temp)
    """

    def exercise1(self):

        return {
            "titulo": "Inmutabilidad de las tuplas",

            "explicacion":
            """
            Las tuplas no permiten modificar
            sus elementos después de ser creadas.
            """,

            "codigo":
            """
numbers = (10, 20, 30, 40)

numbers[0] = 99
            """,

            "resultado":
            """
Error:
'tuple' object does not support item assignment
            """
        }

    def exercise2(self):

        return {
            "titulo": "Desempaquetado de tuplas",

            "explicacion":
            """
            Python permite asignar los valores
            de una tupla directamente a variables.
            """,

            "codigo":
            """
a, b, *rest = (
    100,
    200,
    300,
    400
)

print(a)

print(b)

print(rest)
            """,

            "resultado":
            """
100

200

[300, 400]
            """
        }

    def exercise3(self):

        return {
            "titulo": "Recorrer coordenadas",

            "explicacion":
            """
            Podemos recorrer listas de tuplas
            utilizando un ciclo for.
            """,

            "codigo":
            """
coordinates = [
    (1, 2),
    (3, 4),
    (5, 6)
]

for x, y in coordinates:

    print(f"x = {x}, y = {y}")
            """,

            "resultado":
            """
x = 1, y = 2

x = 3, y = 4

x = 5, y = 6
            """
        }