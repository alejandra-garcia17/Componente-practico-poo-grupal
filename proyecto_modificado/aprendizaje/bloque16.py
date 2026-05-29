class Block16:
    
    titulo = "Archivos y JSON"

    concepto = """
    Modos de apertura de archivos:
    "r"  → lectura
    "w"  → escritura (sobrescribe el contenido)
    "a"  → append — agrega al final
    "x"  → crear; error si el archivo ya existe

    Lectura y escritura (siempre usar with para cerrar automáticamente):
    with open("archivo.txt", "w") as f:
        f.write("Hola mundo\\n")

    with open("archivo.txt", "r") as f:
        contenido = f.read()       # leer todo
    for linea in f: linea.strip()  # leer línea a línea

    JSON:
    import json
    json.dump(datos, f, indent=2)  → guardar objeto como JSON
    json.load(f)                   → cargar JSON como objeto Python

    JSON admite: strings, números, listas, diccionarios, booleanos y null.
    """

    def exercise1(self):

        return {
            "titulo": "Escribir y leer archivos",

            "explicacion":
            """
            El programa crea un archivo de texto,
            escribe información y luego la lee.
            """,

            "codigo":
            """
with open("example.txt", "w") as file:

    file.write("Python\\n")


with open("example.txt", "r") as file:

    content = file.read()


print(content)
            """,

            "resultado":
            """
Python
            """
        }

    def exercise2(self):

        return {
            "titulo": "Guardar y cargar JSON",

            "explicacion":
            """
            json.dump() guarda información
            en formato JSON y json.load()
            permite leerla.
            """,

            "codigo":
            """
import json

data = {
    "x": 10,
    "y": 20
}

with open("data.json", "w") as file:

    json.dump(data, file, indent=4)


with open("data.json", "r") as file:

    loaded = json.load(file)


print(loaded)
            """,

            "resultado":
            """
{
    'x': 10,
    'y': 20
}
            """
        }

    def exercise3(self):

        return {
            "titulo": "Guardar usuarios en JSON",

            "explicacion":
            """
            Podemos guardar listas de usuarios
            y recorrer la información almacenada.
            """,

            "codigo":
            """
users = [

    {"name": "Ana", "age": 20},

    {"name": "Luis", "age": 30}
]

with open("users.json", "w") as file:

    json.dump(users, file, indent=4)


with open("users.json", "r") as file:

    loaded_users = json.load(file)


for user in loaded_users:

    print(user["name"])
            """,

            "resultado":
            """
Ana
Luis
            """
        }