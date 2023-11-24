class Tienda: 
    dinero_caja=0
    def __init__(self,producto1,producto2,producto3,producto4):
        self.producto1=producto1
        self.producto2=producto2
        self.producto3=producto3
        self.producto4=producto4
    
    def mostrar_productos(self):
        print(self.producto1)
        print(self.producto2)
        print(self.producto3)
        print(self.producto4)

    def consultar_producto(self,producto):
        if self.producto1.nombre==producto:
            return self.producto1
        elif self.producto2.nombre==producto:
                    return self.producto2
        elif self.producto3.nombre==producto:
                    return self.producto3
        elif self.producto4.nombre==producto:
                    return self.producto4
        else:
               return None
    
    def mostrar_producto(self,producto):
        if self.producto1.nombre==producto:
           print(self.producto1)
        elif self.producto2.nombre==producto:
           print(self.producto2)
        elif self.producto3.nombre==producto:
           print(self.producto3)
        elif self.producto4.nombre==producto:
           print(self.producto4)   

    def realizar_venta(self,producto,cantidad):
        if self.producto1.nombre==producto:
            self.producto1.cant_bodega=self.producto1.cant_bodega-cantidad
            self.producto1.cant_vendida+=cantidad
            venta=self.producto1.v_unitario*cantidad
        elif self.producto2.nombre==producto:
             self.producto2.cant_bodega=self.producto1.cant_bodega-cantidad
             venta=self.producto2.v_unitario*cantidad
             self.producto2.cant_vendida+=cantidad
        elif self.producto3.nombre==producto:
             self.producto3.cant_bodega=self.producto3.cant_bodega-cantidad
             self.producto3.cant_vendida+=cantidad
             venta=self.producto3.v_unitario*cantidad
        elif self.producto4.nombre==producto:
             self.producto4.cant_bodega=self.producto4.cant_bodega-cantidad
             self.producto4.cant_vendida+=cantidad
             venta=self.producto4.v_unitario*cantidad
        Tienda.dinero_caja+=venta
        
    def productoMasVendido(self):
        if self.producto1.cant_vendida>may:
              may=self.producto1.cant_vendida
              productomay=self.producto1.nombre
        elif self.producto2.cant_vendida>may:
              may=self.producto2.cant_vendida
              productomay=self.producto2.nombre
        elif self.producto3.cant_vendida>may:
              may=self.producto3.cant_vendida
              productomay=self.producto3.nombre
        elif self.producto4.cant_vendida>may:
              may=self.producto4.cant_vendida
              productomay=self.producto4.nombre
        
        print(f"Producto: {productomay}\nCantidad{may}")
