class Block10:

    titulo = "Diccionarios en Python"

    concepto = """
    Los diccionarios almacenan pares clave:valor.
    Son la base de JSON, APIs y configuraciones.

    Acceso y modificación:
    dict["clave"]              → acceso directo (KeyError si no existe)
    dict.get("clave", default) → acceso seguro con valor por defecto
    dict["clave"] = valor      → modificar o agregar
    del dict["clave"]          → eliminar
    dict.pop("clave")          → eliminar y retornar

    Métodos útiles:
    .keys()   → lista de claves
    .values() → lista de valores
    .items()  → lista de tuplas (clave, valor)
    .update() → combinar con otro diccionario
    .copy()   → copia superficial

    Dict comprehension:
    cuadrados = {x: x**2 for x in range(5)}

    COPIA vs REFERENCIA:
    copia = datos        → misma referencia (copia["b"]=2 también cambia datos)
    copia = datos.copy() → objeto nuevo independiente
    """

    def exercise1(self):

        return {
            "titulo": "Acceso a valores",

            "explicacion":
            """
            Podemos acceder a los valores de un diccionario
            utilizando [] o el método get().
            """,

            "codigo":
            """
person = {
    "name": "Ricardo",
    "age": 20,
    "city": "Milagro"
}

print(person["name"])

print(person.get("age"))

print(
    person.get(
        "phone",
        "Not found"
    )
)
            """,

            "resultado":
            """
Ricardo

20

Not found
            """
        }

    def exercise2(self):

        return {
            "titulo": "Recorrer diccionarios",

            "explicacion":
            """
            El método items() permite recorrer
            las claves y valores del diccionario.
            """,

            "codigo":
            """
person = {
    "name": "Ricardo",
    "age": 20,
    "city": "Milagro"
}

for key, value in person.items():

    print(f"{key}: {value}")
            """,

            "resultado":
            """
name: Ricardo

age: 20

city: Milagro
            """
        }

    def exercise3(self):

        return {
            "titulo": "Referencia vs copia",

            "explicacion":
            """
            Cuando asignamos un diccionario a otra variable,
            ambas apuntan al mismo objeto en memoria.
            """,

            "codigo":
            """
person = {
    "name": "Ricardo",
    "age": 20
}

copy_ref = person

copy_ref["country"] = "Ecuador"

print(person)
            """,

            "resultado":
            """
{
    'name': 'Ricardo',
    'age': 20,
    'country': 'Ecuador'
}
            """
        }