class Block4:
    
    titulo = "Entrada de Datos y Conversión de Tipos"

    concepto = """
    print(): Muestra información en pantalla. Admite f-strings, sep y end.
    Ejemplo: print(f"Nombre: {nombre}, Edad: {edad}")

    input(): Lee datos del usuario. ⚠ SIEMPRE devuelve str (texto).
    Ejemplo: edad = int(input("Ingrese su edad: "))

    Casting (conversión de tipos):
    int()   → convierte a entero
    float() → convierte a decimal
    str()   → convierte a texto

    Error común:
    edad = input("Edad: ")
    print(edad + 5)  ❌ ERROR: str + int
    → Siempre convertir con int() o float() antes de operar con números.

    Si NO se convierte el input, los números se concatenan como texto:
    "10" + "5" = "105"  (no suma, concatena)
    """

    def exercise1(self):

        return {
            "titulo": "Solicitar nombre y edad",

            "explicacion":
            """
            El programa solicita el nombre y la edad del usuario
            y luego muestra un mensaje personalizado utilizando f-strings.
            """,

            "codigo":
            """
name = input("Ingrese su nombre: ")

age = int(input("Ingrese su edad: "))

print(f"Nombre: {name}, Edad: {age}")
            """,

            "resultado":
            """
Ingrese su nombre: Damian
Ingrese su edad: 20

Nombre: Damian, Edad: 20
            """
        }

    def exercise2(self):

        return {
            "titulo": "Calcular suma y promedio",

            "explicacion":
            """
            El programa solicita dos números, calcula
            la suma y luego obtiene el promedio.
            """,

            "codigo":
            """
number1 = int(input("Ingrese el primer número: "))

number2 = int(input("Ingrese el segundo número: "))

total = number1 + number2

average = total / 2

print("Suma:", total)

print("Promedio:", average)
            """,

            "resultado":
            """
Ingrese el primer número: 10
Ingrese el segundo número: 20

Suma: 30
Promedio: 15.0
            """
        }

    def exercise3(self):

        return {
            "titulo": "Concatenación de cadenas",

            "explicacion":
            """
            Cuando no se convierte el valor ingresado,
            Python lo trata como texto y realiza concatenación.
            """,

            "codigo":
            """
number = input("Ingrese un número: ")

result = number + "5"

print(result)
            """,

            "resultado":
            """
Ingrese un número: 10

105

Los valores se concatenan como texto.
            """
        }