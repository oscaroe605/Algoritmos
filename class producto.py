class producto:
    def __init__ (self, nombre: str, precio: float, cantidad: int):
        if cantidad < 0:
            raise ValueError("la cantidad no puede ser negativa.")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: {self.precio}, Cantidad: {self.cantidad}"