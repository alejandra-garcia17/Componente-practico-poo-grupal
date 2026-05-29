class Block8:

    titulo = "Listas y Métodos"

    concepto = """
    Métodos principales de listas:
    append(x)  → agregar al final
    extend(L)  → agregar múltiples elementos
    insert(i,x)→ insertar en posición i
    pop()      → eliminar y retornar el último
    remove(x)  → eliminar primera ocurrencia de x
    sort()     → ordenar in-place (modifica la lista original)
    reverse()  → invertir in-place
    clear()    → vaciar la lista
    copy()     → copia superficial
    count(x)   → contar ocurrencias de x
    index(x)   → posición de x

    Funciones integradas: len(), sum(), max(), min()
    sorted() → devuelve lista ordenada SIN modificar la original.

    CONCEPTO CLAVE — referencia vs copia:
    copia_ref  = lista        → misma referencia (ambas apuntan al mismo objeto)
    copia_real = lista.copy() → objeto nuevo (cambios no afectan al original)
    """

    def exercise1(self):

        return {
            "titulo": "Agregar y ordenar elementos en una lista",

            "explicacion":
            """
            Se crea una lista vacía, se agregan elementos
            utilizando append() y luego se ordenan con sort().
            """,

            "codigo":
            """
numbers = []

numbers.append(8)

numbers.append(3)

numbers.append(15)

numbers.sort()

print(numbers)
            """,

            "resultado":
            """
[3, 8, 15]
            """
        }