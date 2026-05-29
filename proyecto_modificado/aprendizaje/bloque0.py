# aprendizaje/bloque0.py

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Block0:

    titulo = "Introducción a la Programación Orientada a Objetos"

    concepto = """
    La Programación Orientada a Objetos (POO) es un paradigma que organiza el software alrededor de objetos, representando entidades del mundo real.
    En lugar de pensar solo en funciones y pasos, la POO propone modelar el sistema como un conjunto de clases y objetos que interactúan entre sí.

    Idea central: POO = Modelar la realidad en código

    CLASE vs OBJETO
    Clase: molde o plantilla que define atributos y métodos → es el plano de una casa.
    Objeto: instancia de una clase, elemento real creado a partir del molde → es la casa construida.

    ¿Por qué usar POO?
    • Organización: estructurar programas grandes de forma clara.
    • Reutilización: usar clases en múltiples partes del sistema.
    • Escalabilidad: el sistema puede crecer sin volverse caótico.
    • Mantenimiento: más fácil modificar una clase específica.
    • Modelado real: representar el mundo real en código.
    • Base para frameworks: Django, Flask, Spring, .NET usan POO intensivamente.

    Diferencia con Programación Estructurada:
    Estructurada → todo son funciones sueltas: def registrar_cliente(): pass
    POO → todo organizado en objetos: class Cliente: def registrar(self): pass
    """

    def exercise1(self):

        return {
            "titulo": "Identificar clases para un sistema de biblioteca",

            "explicacion":
            """
            Una clase representa un tipo de objeto.
            En una biblioteca podemos identificar libros,
            usuarios, préstamos y autores.
            """,

            "codigo":
            """
Book
User
Loan
Author
Category
            """
        }

    def exercise2(self):

        return {
            "titulo": "Crear objetos de la clase Person",

            "explicacion":
            """
            Un objeto es una instancia creada a partir de una clase.
            En este ejemplo se crean tres objetos Person.
            """,

            "codigo":
            """
person1 = Person("Damian", 20)
person2 = Person("Ricardo", 20)
person3 = Person("Luis", 25)
            """,

            "resultado":
            """
Damian - 20
Ricardo - 20
Luis - 25
            """
        }

    def exercise3(self):

        return {
            "titulo": "Diferencia entre clase y objeto",

            "explicacion":
            """
            Una clase funciona como una plantilla.
            Un objeto es una instancia creada a partir de esa plantilla.
            """
        }