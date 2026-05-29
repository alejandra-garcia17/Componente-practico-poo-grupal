class Block2:
    
    titulo = "Tipos de Datos y Estructuras de Datos"

    concepto = """
    Tipos simples:
    • int: 19, -5, 0
    • float: 3.14, -2.5
    • str: "Hola", "Python"
    • bool: True, False
    • None: ausencia de valor

    Tipos complejos:
    • list — colección ordenada y mutable: [1, 2, 3, "python"]
    • tuple — colección inmutable: (1, "hello", 3.14)
    • dict — pares clave-valor: {"nombre": "Juan", "edad": 25}
    • set — elementos únicos sin orden: {1, 2, 3}

    Acceso por índice:
    Python cuenta desde 0: posición 0 = primer elemento, -1 = último elemento.

    Slicing (rebanado):
    Sintaxis: [inicio:fin] → incluye inicio, NO incluye fin.
    lista[1:4] → elementos en posiciones 1, 2 y 3
    lista[:3]  → primeros tres elementos
    lista[-2:] → últimos dos elementos
    """

    def exercise1(self):

        return {
            "titulo": "Tipos de datos simples y complejos",

            "explicacion":
            """
            Python permite almacenar información utilizando
            distintos tipos de datos según la necesidad.
            """,

            "codigo":
            """
integer_number = 19
float_number = 3.14
text = "Hello Python"
boolean_value = True
null_value = None

number_list = [1, 2, 3, "Python", True]

data_tuple = (
    1,
    "Hello",
    3.14
)

data_dictionary = {
    "name": "Juan",
    "age": 25
}

unique_numbers = {1, 2, 3, 4, 5}
            """,

            "resultado":
            """
19
3.14
Hello Python
True
None

[1, 2, 3, 'Python', True]

(1, 'Hello', 3.14)

{'name': 'Juan', 'age': 25}

{1, 2, 3, 4, 5}
            """
        }

    def exercise2(self):

        return {
            "titulo": "Manipulación de listas",

            "explicacion":
            """
            Las listas permiten acceder a elementos
            utilizando índices y cortes.
            """,

            "codigo":
            """
number_list = [10, 20, 30, 40, 50]

number_list[0]

number_list[-1]

number_list[1:4]
            """,

            "resultado":
            """
10

50

[20, 30, 40]
            """
        }

    def exercise3(self):

        return {
            "titulo": "Acceso a estructuras de datos",

            "explicacion":
            """
            Podemos acceder a cadenas, listas y diccionarios
            utilizando índices o claves.
            """,

            "codigo":
            """
text = "Python"

number_list = [1, 2, 3, 4, 5]

data_dictionary = {
    "country": "Ecuador",
    "city": "Guayaquil"
}

text[0]

number_list[-1]

data_dictionary["country"]
            """,

            "resultado":
            """
P

5

Ecuador
            """
        }