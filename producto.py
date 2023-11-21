class producto:
    def __init__(self,nombre,tipo,v_unitario,cant_bodega,cant_vendida,cant_min):
        self.nombre=nombre
        self.tipo=tipo
        self.v_unitario=v_unitario
        self.cant_bodega=cant_bodega
        self.cant_min=cant_min
        self.cant_vendida=cant_vendida
        
    def __str__(self):
        return(f"Nombre {self.nombre} Tipo: {self.tipo} Valor unitario: {self.v_unitario} Cantidad bodega: {self.cant_bodega}")
    
