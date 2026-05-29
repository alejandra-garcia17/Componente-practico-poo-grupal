from abc import ABC, abstractmethod


class Figura(ABC):

    @abstractmethod
    def area(self):
        pass


class Triangulo(Figura):

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def area(self):

        return (self.base * self.altura) / 2


class Producto:

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self):

        return self._precio

    @precio.setter
    def precio(self, valor):

        if valor < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        self._precio = valor


class Animal:

    def sonido(self):

        return "Sonido genérico"


class Perro(Animal):

    def sonido(self):

        return "Guau"


class Gato(Animal):

    def sonido(self):

        return "Miau"


class Vaca(Animal):

    def sonido(self):

        return "Muu"


class Block18:

    titulo = "Principios de POO y Conceptos Avanzados"

    concepto = """
    1. Abstracción: Mostrar lo esencial y ocultar lo innecesario.
       El usuario usa el objeto sin saber cómo funciona internamente.

    2. Encapsulamiento: Proteger los datos controlando el acceso.
       Atributos privados con doble guion bajo: self.__saldo
       Acceso solo a través de métodos públicos.

    3. Herencia: Una clase hija reutiliza atributos y métodos de la clase padre.
       super().__init__() llama al constructor del padre.

    4. Polimorfismo: Mismo método, distinto comportamiento según la clase.
       Perro.sonido() → "Ladra"   |   Gato.sonido() → "Maulla"

    5. Property (getters y setters):
       @property  → getter: controla la lectura de un atributo.
       @attr.setter → setter: valida el valor antes de asignarlo.

    6. Clases Abstractas e Interfaces (ABC):
       from abc import ABC, abstractmethod
       Los métodos @abstractmethod obligan a las subclases a implementarlos.
       No se puede instanciar una clase abstracta directamente.

    Resumen:
    Abstracción     → ocultar complejidad
    Encapsulamiento → proteger datos
    Herencia        → reutilizar código
    Polimorfismo    → mismo método, distinto comportamiento
    Property        → control de acceso a atributos
    Abstractas      → obligan a implementar métodos
    """

    def exercise1(self):

        triangulo = Triangulo(10, 5)

        return {
            "titulo": "Clase abstracta Figura",

            "explicacion":
            """
            Las clases abstractas sirven como plantilla
            para otras clases.

            Triangulo implementa el método area().
            """,

            "codigo":
            """
from abc import ABC, abstractmethod


class Figura(ABC):

    @abstractmethod
    def area(self):
        pass


class Triangulo(Figura):

    def __init__(self, base, altura):

        self.base = base
        self.altura = altura

    def area(self):

        return (
            self.base * self.altura
        ) / 2


triangulo = Triangulo(10, 5)

print(triangulo.area())
            """,

            "resultado":
            f"""
Área: {triangulo.area()}
            """
        }

    def exercise2(self):

        producto = Producto(
            "Laptop",
            900
        )

        return {
            "titulo": "@property y setter",

            "explicacion":
            """
            @property permite controlar el acceso
            a atributos privados.

            El setter valida que el precio
            no sea negativo.
            """,

            "codigo":
            """
class Producto:

    def __init__(self, nombre, precio):

        self.nombre = nombre
        self.precio = precio

    @property
    def precio(self):

        return self._precio

    @precio.setter
    def precio(self, valor):

        if valor < 0:

            raise ValueError(
                "Precio inválido"
            )

        self._precio = valor


producto = Producto(
    "Laptop",
    900
)

print(producto.precio)
            """,

            "resultado":
            f"""
900
            """
        }

    def exercise3(self):

        animales = [
            Perro(),
            Gato(),
            Vaca()
        ]

        sonidos = [
            animal.sonido()
            for animal in animales
        ]

        return {
            "titulo": "Polimorfismo con animales",

            "explicacion":
            """
            El polimorfismo permite que diferentes
            clases tengan métodos con el mismo nombre
            pero distinto comportamiento.
            """,

            "codigo":
            """
class Animal:

    def sonido(self):

        pass


class Perro(Animal):

    def sonido(self):

        return "Guau"


class Gato(Animal):

    def sonido(self):

        return "Miau"


class Vaca(Animal):

    def sonido(self):

        return "Muu"


animales = [
    Perro(),
    Gato(),
    Vaca()
]

for animal in animales:

    print(
        animal.sonido()
    )
            """,

            "resultado":
            f"""
{sonidos[0]}
{sonidos[1]}
{sonidos[2]}
            """
        }