class inventario:
    def __init__ (self):
        self.productos = []
    def agregar_productos(self, producto: producto):
        self.productos.append(producto)
    def eliminar_producto(self, nombre: str):
        self.productos = [p for p in self.productos if p.nombre not in nombre]
    def buscar_producto(self, nombre: str):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None
    def lista_productos(self):
        return self.productos
    def actualizar_cantidad(self, nombre: str, cantidad_vendida: int):
        producto = self.buscar_producto(nombre)
        if producto:
            producto.cantidad -= cantidad_vendida
            if producto.cantidad < 0:
                print (f"El producto {producto.nombre} esta agotado")
    def ordenar_productos(self, criterio: str):
        if criterio == 'nombre':
            self.productos.sort(key = lambda p: p.nombre)
        elif criterio == 'precio':
            self.productos.sort(key = lambda P: p.precio)
        elif criterio == 'cantidad':
            self.productos.sort(key = lambda p: p.cantidad)
        else:
            raise ValueError("Ese criterio de evaluacion no es posible")
    def valor_total(self):
        return self.calculo_valor_total(self, producto)
    def calculo_valor_total(self, producto):
        if not producto:
            return 0
        return producto[0].precio * producto[0].cantidad - producto[0] + self.calculo_valor_total