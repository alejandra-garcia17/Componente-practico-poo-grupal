class Block1:
    
    titulo = "Constructores y Métodos de Clase"

    concepto = """
    El constructor es un método especial que se ejecuta automáticamente cuando se crea un objeto.
    En Python se escribe __init__ (doble guion bajo).
    Su propósito es inicializar el objeto dejándolo preparado con sus datos iniciales.

    ¿Qué es self?
    self representa al objeto actual. Permite guardar atributos dentro de ese objeto específico,
    por eso cada instancia puede tener sus propios valores.

    Constructor con validación:
    El constructor puede validar datos, evitando crear objetos con valores inválidos.

    Parámetros por defecto:
    Los parámetros pueden tener valores por defecto: def __init__(self, nombre, estado="activo")

    Constructor alternativo con @classmethod:
    Permite crear objetos desde estructuras externas como diccionarios.

    Puntos clave:
    • __init__ inicializa objetos al momento de crearse.
    • Se ejecuta automáticamente; no hay que llamarlo.
    • Usa self para guardar atributos dentro del objeto.
    • No retorna valores.
    • Puede recibir parámetros y definir valores por defecto.
    • Puede validar datos antes de guardarlos.
    • Si no se define, Python crea uno vacío internamente.
    """

    def exercise1(self):

        return {
            "titulo": "Creación de objetos Product",

            "explicacion":
            """
            Se crean dos objetos de la clase Product utilizando
            su constructor.
            """,

            "codigo":
            """
product1 = Product("P001", "Laptop", 900)
product2 = Product("P002", "Mouse", 25)
            """,

            "resultado":
            """
P001 - Laptop - 900
P002 - Mouse - 25
            """
        }

    def exercise2(self):

        return {
            "titulo": "Validación de precio negativo",

            "explicacion":
            """
            El constructor valida que el precio no sea negativo.
            Si el valor es incorrecto se genera una excepción.
            """,

            "codigo":
            """
product = Product("P003", "Keyboard", -50)
            """,

            "resultado":
            """
Error: El precio no puede ser negativo.
            """
        }

    def exercise3(self):

        return {
            "titulo": "Atributos opcionales en clases",

            "explicacion":
            """
            Un atributo puede ser opcional utilizando un valor
            por defecto en el constructor.
            """,

            "codigo":
            """
student1 = Student("Daniel")
student2 = Student("Maria", [90, 85, 100])
            """,

            "resultado":
            """
Daniel - []
Maria - [90, 85, 100]
            """
        }

    def exercise4(self):

        return {
            "titulo": "Crear objeto desde un diccionario",

            "explicacion":
            """
            Un método de clase permite crear objetos a partir
            de estructuras de datos como diccionarios.
            """,

            "codigo":
            """
data = {
    "name": "Carlos",
    "grades": [80, 90, 100]
}

student = Student.from_dictionary(data)
            """,

            "resultado":
            """
Carlos - [80, 90, 100]
            """
        }