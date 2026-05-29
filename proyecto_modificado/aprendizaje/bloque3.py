class Block3:
    
    titulo = "Operadores en Python"

    concepto = """
    Operadores Aritméticos:
    +  → suma        -  → resta       *  → multiplicación
    /  → división decimal              // → división entera
    %  → módulo / residuo              ** → potencia

    Operadores de Comparación:
    == → igual        != → diferente
    >  → mayor        <  → menor
    >= → mayor o igual  <= → menor o igual

    Operadores Lógicos:
    and → ambas condiciones verdaderas
    or  → al menos una condición verdadera
    not → invierte el resultado

    CONCEPTO CLAVE: == vs is
    == compara el VALOR (contenido).
    is compara la REFERENCIA en memoria (¿es el mismo objeto?).

    Precedencia de operadores (de mayor a menor):
    1° → **
    2° → *, /, //, %
    3° → +, -
    4° → ==, !=, >, <, >=, <=
    5° → not
    6° → and
    7° → or
    """

    def exercise1(self):

        return {
            "titulo": "Operadores aritméticos",

            "explicacion":
            """
            Los operadores aritméticos permiten realizar
            operaciones matemáticas básicas.
            """,

            "codigo":
            """
a = 20
b = 4

a + b
a - b
a * b
a / b
a // b
a % b
a ** b
            """,

            "resultado":
            """
Suma: 24
Resta: 16
Multiplicación: 80
División: 5.0
División entera: 5
Módulo: 0
Potencia: 160000
            """
        }

    def exercise2(self):

        return {
            "titulo": "Comparación de listas y memoria",

            "explicacion":
            """
            El operador == compara valores.

            El operador is compara si dos variables
            apuntan al mismo objeto en memoria.
            """,

            "codigo":
            """
a = [1, 2]
b = [1, 2]

a == b

a is b
            """,

            "resultado":
            """
True

False

== compara valores.

is compara referencias de memoria.
            """
        }

    def exercise3(self):

        return {
            "titulo": "Orden de evaluación de operadores",

            "explicacion":
            """
            Python sigue reglas de precedencia
            para decidir qué operación ejecutar primero.
            """,

            "codigo":
            """
x = 2 + 1 * 2 % 2 + (2 ** 1) // 2
            """,

            "resultado":
            """
Resultado final: 3

Orden de evaluación:

1. (2 ** 1) = 2

2. 1 * 2 = 2

3. 2 % 2 = 0

4. 2 // 2 = 1

5. 2 + 0 + 1 = 3
            """
        }