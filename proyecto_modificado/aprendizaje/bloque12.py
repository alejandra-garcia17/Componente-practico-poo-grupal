class Block12:

    titulo = "Manejo de Excepciones"

    concepto = """
    Estructura completa:
    try:
        # código que puede fallar
    except TipoError as e:
        # manejar el error
    else:
        # se ejecuta si NO hubo error
    finally:
        # se ejecuta SIEMPRE

    Tipos de error comunes:
    ValueError        → valor inválido (ej. int("abc"))
    TypeError         → tipo incorrecto (str + int)
    IndexError        → índice fuera de rango
    KeyError          → clave no existe en dict/set
    ZeroDivisionError → división por cero
    FileNotFoundError → archivo no encontrado

    Técnicas avanzadas:
    raise → lanzar una excepción manualmente.
    Excepción personalizada → class MiError(Exception): pass
    assert x > 0, "Debe ser positivo"  → verificar condición
    """

    def exercise1(self):

        return {
            "titulo": "Capturar ValueError",

            "explicacion":
            """
            ValueError ocurre cuando un valor
            no tiene el formato esperado.
            """,

            "codigo":
            """
try:

    value = int(
        input("Enter a number: ")
    )

    print(value)

except ValueError:

    print("Invalid input.")
            """,

            "resultado":
            """
Enter a number: hola

Invalid input.
            """
        }

    def exercise2(self):

        return {
            "titulo": "Capturar IndexError",

            "explicacion":
            """
            IndexError ocurre cuando intentamos
            acceder a una posición inexistente
            en una lista.
            """,

            "codigo":
            """
try:

    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:

    print("Index out of range.")
            """,

            "resultado":
            """
Index out of range.
            """
        }

    def exercise3(self):

        return {
            "titulo": "Capturar múltiples errores",

            "explicacion":
            """
            Un bloque try puede manejar
            diferentes tipos de errores
            utilizando varios except.
            """,

            "codigo":
            """
try:

    number = int(
        input("Enter a number: ")
    )

    result = 10 / number

    print(result)

except ValueError:

    print("Input must be numeric.")

except ZeroDivisionError:

    print("Cannot divide by zero.")
            """,

            "resultado":
            """
Enter a number: 0

Cannot divide by zero.
            """
        }