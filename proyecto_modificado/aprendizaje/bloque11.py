class Block11:

    titulo = "Conjuntos en Python"

    concepto = """
    Los conjuntos (set) tienen dos características clave:
    • Sin duplicados: elimina automáticamente los repetidos.
    • Sin orden garantizado: no se puede acceder por índice.

    Operaciones matemáticas:
    Unión            | ó .union()
    Intersección     & ó .intersection()
    Diferencia       - ó .difference()
    Dif. simétrica   ^ ó .symmetric_difference()

    Métodos:
    add(x)     → agregar elemento
    remove(x)  → eliminar; lanza KeyError si no existe
    discard(x) → eliminar; sin error si no existe
    pop()      → eliminar y retornar un elemento aleatorio
    issubset() / issuperset() / isdisjoint()

    Uso práctico — eliminar duplicados de una lista:
    lista = [1, 2, 2, 3, 3, 3]
    sin_dup = list(set(lista))  → [1, 2, 3]
    """

    def exercise1(self):

        return {
            "titulo": "Operaciones entre conjuntos",

            "explicacion":
            """
            Python permite realizar operaciones matemáticas
            entre conjuntos utilizando operadores especiales.
            """,

            "codigo":
            """
set_a = {1, 2, 3, 4}

set_b = {3, 4, 5, 6}

print(set_a | set_b)

print(set_a & set_b)

print(set_a - set_b)
            """,

            "resultado":
            """
Union:
{1, 2, 3, 4, 5, 6}

Intersection:
{3, 4}

Difference:
{1, 2}
            """
        }

    def exercise2(self):

        return {
            "titulo": "Eliminar duplicados",

            "explicacion":
            """
            Los conjuntos eliminan automáticamente
            elementos repetidos.
            """,

            "codigo":
            """
numbers = [
    1,
    2,
    2,
    3,
    3,
    3,
    4
]

unique_numbers = list(set(numbers))

print(unique_numbers)
            """,

            "resultado":
            """
[1, 2, 3, 4]
            """
        }

    def exercise3(self):

        return {
            "titulo": "Diferencia simétrica",

            "explicacion":
            """
            La diferencia simétrica devuelve
            los elementos que no se repiten
            en ambos conjuntos.
            """,

            "codigo":
            """
set_a = {1, 2, 3, 4}

set_b = {3, 4, 5, 6}

result = (
    set_a | set_b
) - (
    set_a & set_b
)

print(result)
            """,

            "resultado":
            """
{1, 2, 5, 6}
            """
        }