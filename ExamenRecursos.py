import os

class Recursos:
    def __init__(self):
        self.recursos = {}

    def agregar_recurso(self, nombre, codigo):
        if codigo not in self.recursos:
            self.recursos[codigo] = nombre
            print(f"Recurso '{nombre}' con código {codigo} agregado con éxito.")
        else:
            print(f"Error: El código {codigo} ya está en uso.")

    def mostrar_recursos(self):
        if self.recursos:
            print("Recursos:")
            for codigo, nombre in self.recursos.items():
                print(f"Código: {codigo}, Nombre: {nombre}")
        else:
            print("No hay recursos disponibles.")

class Usuario:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, nombre, id_usuario):
        if id_usuario not in self.usuarios:
            self.usuarios[id_usuario] = nombre
            print(f"Usuario '{nombre}' con identificación {id_usuario} agregado con éxito.")
        else:
            print(f"Error: La identificación {id_usuario} ya está en uso.")

    def mostrar_usuarios(self):
        if self.usuarios:
            print("Usuarios:")
            for id_usuario, nombre in self.usuarios.items():
                print(f"Identificación: {id_usuario}, Nombre: {nombre}")
        else:
            print("No hay usuarios disponibles.")

class Prestamos:
    def __init__(self):
        self.prestamos = {}

    def realizar_prestamo(self, usuario_id, recurso_codigo):
        if usuario_id in self.prestamos:
            print("El usuario ya tiene un préstamo pendiente.")
        else:
            self.prestamos[usuario_id] = recurso_codigo
            print(f"Prestamo realizado con éxito.")

    def devolver_recurso(self, usuario_id, recurso_codigo):
        if usuario_id in self.prestamos and self.prestamos[usuario_id] == recurso_codigo:
            del self.prestamos[usuario_id]
            print(f"Recurso devuelto con éxito.")
        else:
            print("Error: El usuario no tiene este recurso prestado.")

    def mostrar_prestamos_usuarios(self):
        if self.prestamos:
            print("Préstamos:")
            for usuario_id, recurso_codigo in self.prestamos.items():
                print(f"Usuario: {usuario_id}, Recurso: {recurso_codigo}")
        else:
            print("No hay préstamos realizados.")

def adicionar_recurso(gestor_recursos):
    nombre = input('Nombre: ')
    codigo = int(input('Codigo: '))
    gestor_recursos.agregar_recurso(nombre, codigo)

def consultar_recurso(gestor_recursos):
    gestor_recursos.mostrar_recursos()

def adicionar_usuario(gestor_usuarios):
    nombre = input('Nombre: ')
    identificacion = int(input('Identificación: '))
    gestor_usuarios.agregar_usuario(nombre, identificacion)

def consultar_usuario(gestor_usuarios):
    gestor_usuarios.mostrar_usuarios()

def realizar_prestamo(gestor_prestamos, gestor_usuarios, gestor_recursos):
    usuario_id = int(input('Identificación del usuario: '))
    recurso_codigo = int(input('Código del recurso: '))

    if usuario_id not in gestor_usuarios.usuarios:
        print("Error: El usuario no existe.")
    elif recurso_codigo not in gestor_recursos.recursos:
        print("Error: El recurso no existe.")
    else:
        gestor_prestamos.realizar_prestamo(usuario_id, recurso_codigo)

def devolver_recurso(gestor_prestamos, gestor_usuarios, gestor_recursos):
    usuario_id = int(input('Identificación del usuario: '))
    recurso_codigo = int(input('Código del recurso: '))
    
    gestor_prestamos.devolver_recurso(usuario_id, recurso_codigo)

def mostrar_prestamos_usuarios(gestor_prestamos):
    gestor_prestamos.mostrar_prestamos_usuarios()

def menuRecursos(gestor_recursos):
    os.system('cls')
    while True:    
        print('------Menu Recursos------')
        print(' 1. Adicionar recurso')
        print(' 2. Consultar recurso')
        print(' 3. Salir')
        print('---------------------------')    
        try:        
            opcion = int(input('Digite una opcion: '))       
            match opcion:
                case 1: 
                    adicionar_recurso(gestor_recursos)
                    os.system('pause')
                case 2:
                    consultar_recurso(gestor_recursos)
                case 3:
                    break
                case other:
                    print('Ha digitado una opción inválida')
                    os.system('pause')
        except ValueError:
            os.system('cls')
            print('ERROR: Digite un valor entero')
            os.system('pause')
            os.system('cls')

def menuUsuarios(gestor_usuarios):
    os.system('cls')
    while True:    
        print('------Menu Usuarios------')
        print(' 1. Adicionar usuario')
        print(' 2. Consultar usuario')
        print(' 3. Salir')
        print('---------------------------')    
        try:        
            opcion = int(input('Digite una opcion: '))       
            match opcion:
                case 1: 
                    adicionar_usuario(gestor_usuarios)
                    os.system('pause')
                case 2:
                    consultar_usuario(gestor_usuarios)
                    os.system('pause')
                case 3:
                    break
                case other:
                    print('Ha digitado una opción inválida')
                    os.system('pause')
        except ValueError:
            os.system('cls')
            print('ERROR: Digite un valor entero')
            os.system('pause')
            os.system('cls')

def menuPrestamosDevoluciones(gestor_prestamos, gestor_usuarios, gestor_recursos):
    os.system('cls')
    while True:    
        print('------Menu Prestamos y Devoluciones------')
        print(' 1. Prestamo de recurso')
        print(' 2. Devolucion de un recurso')
        print(' 3. Mostrar Prestamos usuarios')
        print(' 4. Salir')
        print('---------------------------')    
        try:        
            opcion = int(input('Digite una opcion: '))       
            match opcion:
                case 1: 
                    realizar_prestamo(gestor_prestamos, gestor_usuarios, gestor_recursos)
                    os.system('pause')
                case 2:
                    devolver_recurso(gestor_prestamos, gestor_usuarios, gestor_recursos)
                    os.system('pause')
                case 3:
                    mostrar_prestamos_usuarios(gestor_prestamos)
                    os.system('pause')
                case 4:
                    break
                case other:
                    print('Ha digitado una opción inválida')
                    os.system('pause')
        except ValueError:
            os.system('cls')
            print('ERROR: Digite un valor entero')
            os.system('pause')
            os.system('cls')

def menuPrincipal():
    os.system('cls')
    gestor_recursos = Recursos()
    gestor_usuarios = Usuario()
    gestor_prestamos = Prestamos()
    while True:    
        print('------Menu Principal------')
        print(' 1. Manejo de recursos')
        print(' 2. Manejo de usuarios')
        print(' 3. Manejo de prestamos y devoluciones')
        print(' 4. Salir')
        print('---------------------------')    
        try:        
            opcion = int(input('Digite una opcion: '))       
            match opcion:
                case 1: 
                    menuRecursos(gestor_recursos)
                case 2:
                    menuUsuarios(gestor_usuarios)
                case 3:
                    menuPrestamosDevoluciones(gestor_prestamos, gestor_usuarios, gestor_recursos)
                case 4:
                    break 
                case other:
                    print('Ha digitado una opción inválida')
                    os.system('pause')
        except ValueError:
            os.system('cls')
            print('ERROR: Digite un valor entero')
            os.system('pause')
            os.system('cls')

menuPrincipal()
