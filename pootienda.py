import os
from producto import producto
from tienda import Tienda

def menu_ventas():
    while True:
        os.system("cls")
        print("   MENU VENTAS   ")
        print("   --------------------")
        print("   1.Realizar venta")
        print("   2.Mostrar venta")
        print("   3.Venta por producto")
        print("   4.Salir")
        o=int(input("Ingrese una opcion"))
        match o:
            case 1:
                realizar_venta(Tienda)
            case 2:
                mostrar_venta()
            case 3:
                venta_por_producto()              
            case 4:
                break
            case other:
                print("La opcion es invalida")
                os.system("pause")

#DEFS OPCIONES MENU VENTAS

def realizar_venta(tienda):
    tienda.mostrar_producto()
    producto=input("Digitar producto: ")
    productoal=tienda.consultar_producto(producto)
    if productoal!=None:
        tienda.mostrar_producto(producto)
        cantidad=int(input("Digitar cantidad: "))
        if productoal.cantidad_bodega>cantidad:
            cantidadv=cantidad
        elif productoal.cantidad_bodega>0:
            cantidadv=productoal.cantidad_bodega
        else:
            print("No hay productos a la venta")
            return
        tienda.realizar_venta(producto,cantidadv)
        valor_venta=productoal.v_unitario*cantidadv
        print(f"Cantidad{cantidadv} \n Valor unitario es: {productoal.v_unitario} \n valor venta: {valor_venta}")
        tienda.dinero_caja=tienda.dinero_caja+valor_venta
    else:
        print("El producto no existe")
        return
    
def mostrar_venta():
    print

def venta_por_producto():
    print

def menu_pedidos():
    while True:
        os.system("cls")
        print("   MENU VENTAS   ")
        print("   --------------------")
        print("   1.Determinar pedido")         #con pedir se refiere a llenar inventario de nuevo
        print("   2.Realizar pedido")
        print("   3.Salir")
        o=int(input("Ingrese una opcion"))
        match o:
            case 1:
                print
            case 2:
                print
            case 3:
                break
            case other:
                print("La opcion es invalida")
                os.system("pause")


def menu_estadisticas():
    while True:
        os.system("cls")
        print("   MENU ESTADISTICAS   ")
        print("   --------------------")
        print("   1.Ventas totales")
        print("   2.Ventas por producto")
        print("   3.promedio ventas")
        print("   4.Producto mas vendido")
        print("   5.Salir")
        o=int(input("Ingrese una opcion"))
        match o:
            case 1:
                print
            case 2:
                print
            case 3:
                print
            case 4: 
                print
            case 5:
                break
            case other:
                print("La opcion es invalida")
                os.system("pause")



def main():
    creado=False
    while True:
        os.system("cls")
        print("   MENU TIENDA   ")
        print("   --------------------")
        print("   1.Crear tienda")
        print("   2.Mostar productos")
        print("   3.Realizar ventas")
        print("   4.Realizar pedidos")
        print("   5.Estadisticas")
        print("   6.Salir")
        a=int(input("ingrese una opcion: "))
        match a:
            case 1:
                if creado==False:
                    tienda=crear_tienda()
                    os.system("pause")
                    creado=True
                else:
                    print("ya hay productos en la tienda")
                    os.system("pause")
            case 2:
                if creado==True:
                    tienda.mostrar_productos()
                    os.system("pause")
                else: 
                    print("No hay productos")
                    os.system("pause")
            case 3:
                    if creado==1:
                        menu_ventas()
                        os.system("pause")
                    else:
                        print("ingrese primero la opcion 1")
                        os.system("pause")
            case 4:
                    if creado==1:
                        menu_pedidos()
                        os.system("pause")
                    else: 
                        print("ingrese primero la opcion 1")
                        os.system("pause")
            case 5:
                    if creado==1:
                        menu_estadisticas()
                        os.system("pause")
                    else: 
                        print("ingrese primero la opcion 1")
                        os.system("pause")
            case 6:
                print("gracias por usa nuestro sistema")
                break
            case _:
                print("ingrese un numero valido")

def crear_tienda():
    producto1=producto("Lapiz",1,2000,50,5,0)
    producto2=producto("Cuaderno",1,3000,50,5,0)
    producto3=producto("Aspirina",2,1000,50,3,0)
    producto4=producto("Arroz",3,5000,50,2,0)
    tienda=Tienda(producto1,producto2,producto3,producto4)
    return tienda #retorna direccion, ya que es un objeto
    print("se ha creado tienda con 4 productos")

main()
