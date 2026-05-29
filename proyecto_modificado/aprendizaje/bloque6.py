class Block6:
    
    titulo = "Bucles y List Comprehension"

    concepto = """
    while: repite mientras la condición sea verdadera.

    for con range(): itera sobre un rango de números.
    range(5) → 0,1,2,3,4
    range(0, 10, 2) → 0,2,4,6,8 (paso 2)

    for sobre colecciones: itera listas, diccionarios, etc.
    enumerate() → devuelve índice y valor en cada iteración.
    .items() → itera claves y valores de un diccionario.

    break y continue:
    break    → termina el bucle completamente.
    continue → salta la iteración actual y continúa.

    List Comprehension:
    cuadrados = [x**2 for x in range(5)]        → [0, 1, 4, 9, 16]
    pares     = [x for x in range(10) if x % 2 == 0]  → [0, 2, 4, 6, 8]
    cubos     = {x: x**3 for x in range(4)}     → dict comprehension
    """

    def exercise1(self):

        return {
            "titulo": "Imprimir números del 1 al 10 con while",

            "explicacion":
            """
            El ciclo while ejecuta instrucciones mientras
            una condición sea verdadera.
            """,

            "codigo":
            """
counter = 1

while counter <= 10:

    print(counter)

    counter += 1
            """,

            "resultado":
            """
1
2
3
4
5
6
7
8
9
10
            """
        }

    def exercise2(self):

        return {
            "titulo": "Recorrer listas con enumerate",

            "explicacion":
            """
            enumerate() permite obtener el índice
            y el valor de cada elemento de una lista.
            """,

            "codigo":
            """
fruits = [
    "Manzana",
    "Pera",
    "Uva"
]

for index, fruit in enumerate(fruits):

    print(f"{index} - {fruit}")
            """,

            "resultado":
            """
0 - Manzana
1 - Pera
2 - Uva
            """
        }

    def exercise3(self):

        return {
            "titulo": "List comprehension",

            "explicacion":
            """
            Las list comprehensions permiten crear listas
            de forma rápida y elegante.
            """,

            "codigo":
            """
even_squares = [

    x ** 2

    for x in range(1, 11)

    if x % 2 == 0
]

print(even_squares)
            """,

            "resultado":
            """
[4, 16, 36, 64, 100]
            """
        }