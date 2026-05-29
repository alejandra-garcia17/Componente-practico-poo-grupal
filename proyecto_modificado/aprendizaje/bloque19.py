class Persona:
    
    def __init__(self, nombre):

        self.nombre = nombre


class Empleado(Persona):

    def __init__(self, nombre, salario):

        super().__init__(nombre)

        self.salario = salario


class DetalleFactura:

    def __init__(self, producto, precio):

        self.producto = producto
        self.precio = precio


class Factura:

    def __init__(self):

        self.detalles = []

    def agregar_detalle(self, detalle):

        self.detalles.append(detalle)


class Block19:

    titulo = "Relaciones UML en Código"

    concepto = """
    Resumen de Relaciones UML en código:

    Asociación  → una clase USA otra (como parámetro o referencia temporal)
                  Código típico: Venta(cliente)  |  emp es parámetro en crear()

    Agregación  → una clase CONTIENE objetos externos (existen independientemente)
                  Código típico: carrito.agregar(producto)  |  self.cliente = cliente

    Composición → una clase CREA objetos internamente (el objeto hijo no existe sin el padre)
                  Código típico: self.detalles.append(DetalleVenta(...))

    Herencia    → una clase ES una especialización de otra
                  Código típico: class Cliente(Persona)

    Interfaz    → una clase CUMPLE un contrato (implementa métodos obligatorios)
                  Código típico: class Venta(ICrud)  con @abstractmethod

    Regla de identificación:
    "ES un..."      → Herencia
    "TIENE un..."   → Composición o Agregación
    "USA un..."     → Asociación
    "CUMPLE con..." → Interfaz
    """

    def exercise1(self):

        return {
            "titulo": "Relaciones UML",

            "explicacion":
            """
            Las relaciones UML describen cómo
            interactúan las clases entre sí.
            """,

            "codigo":
            """
Persona <--- Empleado

Factura *--- DetalleFactura
            """,

            "resultado":
            """
Herencia:
Empleado ES una Persona.

Composición:
Factura contiene DetalleFactura.
            """
        }

    def exercise2(self):

        empleado = Empleado(
            "Carlos",
            1200
        )

        return {
            "titulo": "Herencia con Empleado",

            "explicacion":
            """
            La herencia ocurre cuando una clase
            reutiliza atributos y métodos
            de otra clase.
            """,

            "codigo":
            """
class Persona:

    def __init__(self, nombre):

        self.nombre = nombre


class Empleado(Persona):

    def __init__(
        self,
        nombre,
        salario
    ):

        super().__init__(nombre)

        self.salario = salario
            """,

            "resultado":
            f"""
Nombre: {empleado.nombre}

Salario: {empleado.salario}
            """
        }

    def exercise3(self):

        factura = Factura()

        detalle1 = DetalleFactura(
            "Laptop",
            900
        )

        detalle2 = DetalleFactura(
            "Mouse",
            25
        )

        factura.agregar_detalle(detalle1)
        factura.agregar_detalle(detalle2)

        detalles = "\n".join(
            [
                f"{d.producto} - ${d.precio}"
                for d in factura.detalles
            ]
        )

        return {
            "titulo": "Composición con Factura",

            "explicacion":
            """
            La composición ocurre cuando una clase
            contiene completamente a otra.

            Si Factura desaparece,
            sus detalles también.
            """,

            "codigo":
            """
class DetalleFactura:

    def __init__(
        self,
        producto,
        precio
    ):

        self.producto = producto
        self.precio = precio


class Factura:

    def __init__(self):

        self.detalles = []


factura = Factura()
            """,

            "resultado":
            f"""
{detalles}
            """
        }