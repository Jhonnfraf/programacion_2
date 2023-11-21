class Tienda: 
    dinero_caja=0
    def __init__(self,producto1,producto2,producto3,producto4):
        self.producto1=producto1
        self.producto2=producto2
        self.producto3=producto3
        self.producto4=producto4
    
    def mostrar_producto(self):
        print(self.producto1)
        print(self.producto2)
        print(self.producto3)
        print(self.producto4)