#ejercicio con metodo abstracto_
#es como una pnantilla que nos sirve para 
#para definir una regla o "contrato": establece el nombre y 
# los parámetros de un método, pero no contiene código ni lógica.
#  Obliga a todas las subclases (clases hijas) a implementar su propia
#  versión de ese método para poder funcionar
from abc import ABC, abstractmethod

class Block20:
   titulo='clase abstracta'
   def exercise1(self):
        return{

'titulo':'clase abstracta',
    'codigo':'''
from abc import ABC, abstractmethod
class vehiculo(ABC):
     @abstractmethod
     def acelerar(self):
         pass
            
Class coche(vehiculo):
       def acelerar(self):
            print('el coche acelera')

mi_coche=coche()
mi_coche.acelerar()           
                ''',
'resultado':'el coche acelera'                
        }

# =========================================================
# ENUNCIADO — SISTEMA DE BIBLIOTECA 
# =========================================================
#
# Una biblioteca necesita registrar información de:
#
# - Libros
# - Revistas
#
# El administrador quiere que ambos objetos puedan:
#
# - mostrar toda su información
# - indicar si están disponibles o no
#
# Como las dos clases necesitan las mismas funcionalidades,
# debes utilizar mixins para evitar repetir código.
#
#
# =========================================================
# MIXINS QUE DEBES CREAR
# =========================================================
#
# MostrarMixin
#
# Método:
#
# mostrar()
#
# Debe imprimir:
#
# - nombre de la clase
# - todos los atributos y sus valores
#
#
# ---------------------------------------------------------
#
# DisponibilidadMixin
#
# Método:
#
# disponible_estado()
#
# Debe imprimir:
#
# "Disponible"
#
# o:
#
# "No disponible"
#
# dependiendo del valor del atributo:
#
# disponible
#
#
# =========================================================
# CLASES DEL DOMINIO
# =========================================================
#
# Libro
#
# Atributos:
#
# - titulo
# - autor
# - disponible
#
# Debe heredar ambos mixins.
#
#
# ---------------------------------------------------------
#
# Revista
#
# Atributos:
#
# - nombre
# - edicion
# - disponible
#
# Debe heredar ambos mixins.
#
#
# =========================================================
# LO QUE DEBES HACER
# =========================================================
#
# 1. Crear los mixins.
# 2. Crear las clases Libro y Revista.
# 3. Crear un libro disponible.
# 4. Crear una revista no disponible.
# 5. Mostrar la información de ambos objetos.
# 6. Mostrar el estado de disponibilidad.
#
#
# =========================================================
# CÓDIGO
# =========================================================


# class MostrarMixin:
#
#     def mostrar(self):
#
#         print(f"\n--- {self.__class__.__name__} ---")
#
#         for atributo, valor in self.__dict__.items():
#
#             print(f"{atributo}: {valor}")


# class DisponibilidadMixin:
#
#     def disponible_estado(self):
#
#         if self.disponible:
#
#             print("\nDisponible")
#
#         else:
#
#             print("\nNo disponible")


# class Libro(
#
#     MostrarMixin,
#     DisponibilidadMixin
#
# ):
#
#     def __init__(
#
#         self,
#         titulo,
#         autor,
#         disponible
#
#     ):
#
#         self.titulo = titulo
#         self.autor = autor
#         self.disponible = disponible


# class Revista(
#
#     MostrarMixin,
#     DisponibilidadMixin
#
# ):
#
#     def __init__(
#
#         self,
#         nombre,
#         edicion,
#         disponible
#
#     ):
#
#         self.nombre = nombre
#         self.edicion = edicion
#         self.disponible = disponible


# libro = Libro(
#
#     "Python",
#     "Guido",
#     True
#
# )


# revista = Revista(
#
#     "Ciencia Hoy",
#     15,
#     False
#
# )


# libro.mostrar()

# libro.disponible_estado()

# revista.mostrar()

# revista.disponible_estado()