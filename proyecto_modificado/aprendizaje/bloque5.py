class Block5:
    
    titulo = "Estructuras Condicionales"

    concepto = """
    Estructura básica:
    if condicion:
        # se ejecuta si es verdadera
    elif otra_condicion:
        # si la anterior era falsa y esta verdadera
    else:
        # si ninguna fue verdadera

    Operador ternario:
    mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

    match-case (Python 3.10+):
    match dia:
        case "lunes": print("Inicio de semana")
        case "viernes": print("Fin laboral")
        case _: print("Otro día")

    Evaluación corta (short-circuit):
    Si la primera condición de un and es False, Python NO evalúa la segunda.
    Esto optimiza el rendimiento del programa.
    """

    def exercise1(self):

        return {
            "titulo": "Número par o impar",

            "explicacion":
            """
            El programa verifica si un número es par
            o impar utilizando el operador módulo %.
            """,

            "codigo":
            """
number = int(input("Ingrese un número: "))

if number % 2 == 0:
    print("Par")
else:
    print("Impar")
            """,

            "resultado":
            """
Ingrese un número: 10

Par
            """
        }

    def exercise2(self):

        return {
            "titulo": "Clasificación de notas",

            "explicacion":
            """
            El programa asigna una letra dependiendo
            de la calificación ingresada.
            """,

            "codigo":
            """
grade = int(input("Ingrese la nota: "))

if grade >= 90:
    print("A")

elif grade >= 80:
    print("B")

elif grade >= 70:
    print("C")

else:
    print("D")
            """,

            "resultado":
            """
Ingrese la nota: 85

B
            """
        }

    def exercise3(self):

        return {
            "titulo": "Sistema de login",

            "explicacion":
            """
            El programa valida usuario y contraseña
            utilizando estructuras condicionales.
            """,

            "codigo":
            """
username = input("Ingrese usuario: ")

password = input("Ingrese contraseña: ")

if username == "Ingeniero" and password == "2005":

    print("Bienvenido")

else:

    print("Acceso denegado")
            """,

            "resultado":
            """
Ingrese usuario: Ingeniero
Ingrese contraseña: 2005

Bienvenido
            """
        }