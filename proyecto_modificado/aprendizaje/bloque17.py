import json


class AverageMixin:

    def calculate_average(self, grades):

        if not grades:
            raise ValueError(
                "Grades list cannot be empty."
            )

        return sum(grades) / len(grades)


class Student(AverageMixin):

    def show_average(self, grades):

        average = self.calculate_average(grades)

        return average


class ValidationMixin:

    def validate_email(self, email):

        return "@" in email and ".com" in email

    def validate_age(self, age):

        return age >= 18


class User(ValidationMixin):

    def register(self, email, age):

        if not self.validate_email(email):

            return "Invalid email."

        if not self.validate_age(age):

            return "User must be at least 18."

        return "User registered successfully."


class ExportMixin:

    def export_json(self, data):

        return json.dumps(data, indent=4)

    def export_csv(self, data):

        return ",".join(map(str, data))


class Report(ExportMixin):

    def export_data(self):

        sales = [100, 200, 300]

        return {
            "json": self.export_json(sales),
            "csv": self.export_csv(sales)
        }


class Block17:

    titulo = "Mixins en Python"

    concepto = """
    Un Mixin es una clase que NO se usa sola.
    Se diseña para agregar funcionalidad a otras clases mediante herencia,
    evitando duplicar código.
    Regla: si una clase es un Mixin, su nombre suele terminar en Mixin.

    Ejemplo:
    class ValidacionMixin:
        def validar_nombre(self, nombre):
            if not nombre: raise ValueError("Nombre vacío")

    class SistemaEstudiantes(ValidacionMixin):
        def registrar(self, nombre):
            self.validar_nombre(nombre)  # método del mixin

    MRO — Orden de Resolución de Métodos:
    Cuando una clase hereda de varias, Python busca métodos de izquierda a derecha.
    class C(A, B): → busca primero en A, luego en B, luego en C.
    C().metodo() imprime lo de A si A tiene el método.
    """

    def exercise1(self):

        return {
            "titulo": "AverageMixin",

            "explicacion":
            """
            Un Mixin puede reutilizar lógica para
            calcular promedios.
            """,

            "codigo":
            """
class AverageMixin:

    def calculate_average(self, grades):

        return sum(grades) / len(grades)


class Student(AverageMixin):

    pass


student = Student()

print(
    student.calculate_average(
        [80, 90, 100]
    )
)
            """,

            "resultado":
            """
90.0
            """
        }

    def exercise2(self):

        return {
            "titulo": "ValidationMixin",

            "explicacion":
            """
            Los Mixins también permiten reutilizar
            validaciones en diferentes clases.
            """,

            "codigo":
            """
class ValidationMixin:

    def validate_email(self, email):

        return "@" in email


class User(ValidationMixin):

    pass


user = User()

print(
    user.validate_email(
        "correo@gmail.com"
    )
)
            """,

            "resultado":
            """
True
            """
        }

    def exercise3(self):

        report = Report()

        exported = report.export_data()

        return {
            "titulo": "ExportMixin",

            "explicacion":
            """
            ExportMixin permite reutilizar funciones
            para exportar información.
            """,

            "codigo":
            """
class ExportMixin:

    def export_csv(self, data):

        return ",".join(map(str, data))


class Report(ExportMixin):

    pass


report = Report()

print(
    report.export_csv(
        [100, 200, 300]
    )
)
            """,

            "resultado":
            f"""
JSON:
{exported["json"]}

CSV:
{exported["csv"]}
            """
        }