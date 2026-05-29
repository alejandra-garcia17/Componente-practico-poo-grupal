class Block13:

    titulo = "Decoradores en Python"

    concepto = """
    Un decorador es una función que recibe otra función,
    modifica su comportamiento y retorna una nueva función.
    Se aplica con @nombre_decorador antes de la función.

    Estructura básica:
    def mi_decorador(funcion_original):
        def wrapper(*args, **kwargs):
            print("Antes de ejecutar")
            resultado = funcion_original(*args, **kwargs)
            print("Después de ejecutar")
            return resultado
        return wrapper

    @mi_decorador
    def saludar():
        print("Hola mundo")

    Usos reales de los decoradores:
    • Validar datos antes de ejecutar.
    • Controlar acceso (autenticación en Django/Flask).
    • Registrar logs de ejecución.
    • Medir tiempo de ejecución.
    """

    def exercise1(self):

        return {
            "titulo": "Decorador básico",

            "explicacion":
            """
            Un decorador puede ejecutar código
            antes o después de una función.
            """,

            "codigo":
            """
def start_message(func):

    def wrapper():

        print("Starting...")

        func()

    return wrapper


@start_message
def hello():

    print("Hello world")


hello()
            """,

            "resultado":
            """
Starting...

Hello world
            """
        }

    def exercise2(self):

        return {
            "titulo": "Decorador para validar números",

            "explicacion":
            """
            Este decorador verifica
            que el número sea positivo
            antes de ejecutar la función.
            """,

            "codigo":
            """
def positive_validator(func):

    def wrapper(number):

        if number < 0:

            print(
                "Number must be positive."
            )

            return

        return func(number)

    return wrapper


@positive_validator
def square(number):

    print(number ** 2)


square(5)
            """,

            "resultado":
            """
25
            """
        }

    def exercise3(self):

        return {
            "titulo": "Validación con número negativo",

            "explicacion":
            """
            Si el número es negativo,
            el decorador evita que
            la función se ejecute.
            """,

            "codigo":
            """
square(-5)
            """,

            "resultado":
            """
Number must be positive.
            """
        }