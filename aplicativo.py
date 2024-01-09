from clases import *
def consultarRecurso(central):
    codigo=leerInt("Digite codigo a buscar:")
    recurso,b = central.buscarRecurso(codigo)
    if b ==True:
        print(f"{recurso}")

    else: 
        print(f"El recurso no existe en la central")

def consultarUsuario(central):
    codigo=leerInt("Digite codigo a buscar:")
    usuario, b= central.buscarUsuario(codigo)
    if b==True:
        print (f"{usuario}")
    else:
        print (f"el usuario no existe en la central")
def prestar(central,usuario):
    print("usuario valido")
    codigo=leerInt(input("digite codigo del recurso:"))
    recurso,b=central.buscarRecurso(codigo)
    if b==True:
        prestamo=Prestamo(usuario,recurso)
        central.prestamos.append(prestamo)
        central.recursos.remove(recurso)
    else:
        print("el recurso no existe en la central")
def prestamo(central):
    codigo=leerInt(input("Digite codigo del usuario:"))
    usuario,b= central.buscarUsuario(codigo)
    if b==True:
        central.mostrarrecursos()
        c=central.conteo(usuario)
        if usuario.tipo==2:
            if c<2:
                prestar(central,usuario)
            else:
                print("el docente ya tiene 2 prestamos, no puede mas")
        elif usuario.tipo==3:
            if c<1:
                prestar(central,usuario)
            else:
                print("el trabajador ya tiene 1 prestamo, no puede mas")
        elif usuario.tipo==1:
            prestar(central,usuario)
    else:
        print("el usuario no esta registrado")
def devolucion(central):
    codigo=leerInt(input("digite codigo del usuario"))
    usuario,b=central.buscarUsuario(codigo)
    if b==True:
        central.mostrarprestamos(usuario)
        codigo2=leerInt(input("digite codigo del recurso:"))
        prestamo,b2=central.buscarPrestamo(codigo2)
        if b2==True:
            central.recursos.append(prestamo.recurso)
            central.prestamos.remove(prestamo)
        else:
            print("el recurso no ha sido prestado")
def menu():
    central=Central()
    while True:
        #os.system("cls")
        print("menu")
        print("1.Manejo recursos")
        print("2.Manejo usuarios")
        print("3.Manejo prestamos y devoluciones")
        print("4.salir")
        opcion=leerInt(input("digite opcion:"))
        match opcion:
            case 1:
                manejorecursos(central)
                os.system("pause")
            case 2:
                manejousuarios(central)
                os.system("pause")
            case 3:
                if len(central.usuarios)>0 and len(central.usuarios)>0:                           
                    manejopresdev(central)
                else:
                    print("no hay recursos o usuarios")
                os.system("pause")
def manejorecursos(central):
    while True:
        #os.system("cls")
        print("manejo recursos")
        print("1.adicionar recurso")
        print("2.consultar recurso")
        print("3.regresar")
        opcion=leerInt(input("digite opcion:"))
        match opcion:
            case 1:
                central.adicionarRecurso()
                os.system("pause")
            case 2:
                consultarRecurso(central)
                os.system("pause")
            case 3:
                break
            case other:
                print("opcion invalida")
def manejousuarios(central):
    while True:
        #os.system("cls")
        print("manejo usuarios")
        print("1.adicionar usuario")
        print("2.consultar usuario")
        print("3.regresar")
        opcion=leerInt(input("digite opcion:"))
        match opcion:
            case 1:
                central.adicionarUsuario()
                os.system("pause")
            case 2:
                consultarUsuario(central)
                os.system("pause")
            case 3:
                break
            case other:
                print("opcion invalida")
                os.system("pause")
def manejopresdev(central):
    while True:
        #os.system("cls")
        print("manejo de prestamos y devoluciones")
        print("1.prestamo de recurso")
        print("2.devolucion de un recurso")
        print("3.mostrar prestamo usuario")
        print("4.mostrar prestamos usuarios")
        opcion=leerInt(input("digite opcion:"))
        match opcion:
            case 1:
                prestamo(central)
                os.system("pause")
            case 2:
                devolucion(central)
                os.system("pause")
            case 3:
                codigo=leerInt(input("Digite codigo del usuario:"))
                usuario,b= central.buscarUsuario(codigo)
                central.mostrarprestamosusuario(usuario)
                os.system("pause")
            case 4:
                central.mostrarprestamos()
                os.system("pause")
            case 5:
                break
            case other:
                print("opcion invalida")
                os.system("pause")
menu()
