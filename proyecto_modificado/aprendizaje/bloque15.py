class Block15:
    
    titulo = "Funciones de Orden Superior"

    concepto = """
    Una función de orden superior recibe otra función como parámetro o devuelve una función.

    map(): Aplica una función a cada elemento de una colección.
    numeros = [1, 2, 3, 4]
    cuadrados = list(map(lambda x: x**2, numeros))  → [1, 4, 9, 16]

    filter(): Filtra elementos según condición (True/False).
    pares = list(filter(lambda x: x % 2 == 0, numeros))  → [2, 4]

    reduce(): Reduce la colección a un único valor acumulado.
    from functools import reduce
    suma = reduce(lambda x, y: x + y, numeros)  → 10
    Proceso: 1+2=3, 3+3=6, 6+4=10

    Combinación de map() + filter():
    resultado = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numeros)))
    → Cuadrado de los pares: [4, 16]
    """

    def exercise1(self):

        return {
            "titulo": "Uso de map()",

            "explicacion":
            """
            map() aplica una función a cada elemento
            de una lista.
            """,

            "codigo":
            """
numbers = [2, 4, 6]

result = list(
    map(
        lambda x: x + 1,
        numbers
    )
)

print(result)
            """,

            "resultado":
            """
[3, 5, 7]
            """
        }

    def exercise2(self):

        return {
            "titulo": "Uso de filter()",

            "explicacion":
            """
            filter() permite filtrar elementos
            que cumplen una condición.
            """,

            "codigo":
            """
numbers = [1, 2, 3, 4, 5]

result = list(
    filter(
        lambda x: x > 3,
        numbers
    )
)

print(result)
            """,

            "resultado":
            """
[4, 5]
            """
        }

    def exercise3(self):

        return {
            "titulo": "Uso de reduce()",

            "explicacion":
            """
            reduce() combina todos los elementos
            de una lista en un solo resultado.
            """,

            "codigo":
            """
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(
    lambda x, y: x * y,
    numbers
)

print(result)
            """,

            "resultado":
            """
24
            """
        }

    def exercise4(self):

        return {
            "titulo": "Combinar filter() y map()",

            "explicacion":
            """
            Podemos combinar funciones para realizar
            transformaciones más avanzadas.
            """,

            "codigo":
            """
numbers = [1, 2, 3, 4, 5, 6]

result = list(

    map(

        lambda x: x ** 2,

        filter(
            lambda x: x % 2 == 0,
            numbers
        )
    )
)

print(result)
            """,

            "resultado":
            """
[4, 16, 36]
            """
        }