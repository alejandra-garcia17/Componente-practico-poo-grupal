class Block7:

    titulo = "Funciones en Python"

    concepto = """
    Estructura básica:
    def sumar(a, b):
        return a + b

    Parámetros por defecto y retorno múltiple:
    def presentarse(nombre, edad=25):  → parámetro opcional
    def dividir(a, b): return a // b, a % b  → retorna tupla

    *args y **kwargs:
    *args   → múltiples parámetros posicionales → def sumar_varios(*numeros)
    **kwargs → múltiples parámetros con nombre → def mostrar_datos(**datos)

    Funciones lambda:
    cuadrado = lambda x: x**2  → función anónima en una línea

    Recursividad:
    Una función que se llama a sí misma. Requiere un caso base para terminar.
    def factorial(n):
        if n == 0: return 1  # caso base
        return n * factorial(n - 1)  # llamada recursiva
    """

    def exercise1(self):

        return {
            "titulo": "Función para calcular el doble",

            "explicacion":
            """
            Se crea una función llamada double()
            que recibe un número y retorna su doble.
            """,

            "codigo":
            """
def double(number):

    return number * 2


number = int(input("Ingrese un número: "))

print(double(number))
            """,

            "resultado":
            """
Ingrese un número: 5

10
            """
        }

    def exercise2(self):

        return {
            "titulo": "Función usando *args",

            "explicacion":
            """
            *args permite recibir múltiples valores
            dentro de una función.
            """,

            "codigo":
            """
def add_numbers(*numbers):

    return sum(numbers)


result = add_numbers(
    10,
    20,
    30,
    40
)

print(result)
            """,

            "resultado":
            """
100
            """
        }

    def exercise3(self):

        return {
            "titulo": "Función recursiva factorial",

            "explicacion":
            """
            Una función recursiva es aquella
            que se llama a sí misma.

            En este ejemplo se calcula el factorial.
            """,

            "codigo":
            """
def factorial(number):

    if number == 0:

        return 1

    return number * factorial(number - 1)


number = int(input("Ingrese un número: "))

print(factorial(number))
            """,

            "resultado":
            """
Ingrese un número: 5

120
            """
        }