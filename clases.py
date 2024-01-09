import os
from leer import leerInt
class Central:
    def __init__(self):
        self.usuarios = []
        self.recursos = []
        self.prestamos = []

    def adicionarUsuario(self):
        b=False
        codigo = leerInt(input("digite codigo:"))
        for usuario in self.usuarios:
            if codigo==usuario.codigo:
                b=True

        if b==False:
            nombre=input("Digite nombre")
            tipo=leerInt(input("Digite tipo: (1-3)"))
            usuario=Usuario(codigo,tipo,nombre)
            self.usuarios.append(usuario)
        else: 
            print("Ese codigo ya esta en uso")

    def buscarUsuario(self,codigo):
        b=False
        usuario1=None
        for usuario in self.usuarios:
            if codigo == usuario.codigo:
                usuario1=usuario
                b= True
            else:
                print("No hay")

        return usuario1, b
    def adicionarRecurso(self):
        b=False
        codigo=leerInt(input("Digite codigo del recurso:"))
        for recurso in self.recursos:
            if codigo ==recurso.codigo:
                b= True
        if b!=True:
            nombre=input("Digite nombre del recurso:")
            recurso=Recurso(codigo,nombre)
            self.recursos.append(recurso)
        else:
            print("ese codigo ya esta en uso")
    def buscarRecurso(self,codigo):
        b=False
        recurso1=None
        for recurso in self.recursos:
            if recurso.codigo == codigo:
                recurso1 = recurso
                b=True
        return recurso1, b
    def buscarPrestamo(self,codigo):
        b=False
        Prestamo=None
        for prestamo in self.prestamos:
            if prestamo.recurso.codigo == codigo:
                Prestamo=prestamo
                b=True
        return Prestamo,b
    def mostrarrecursos(self):
        for recurso in self.recursos:
            print(recurso)
    def mostrarprestamos(self,usuario):
        for prestamo in self.prestamos:
            if prestamo.usuario.nombre==usuario.nombre:
                print(prestamo)
    def conteo(self,usuario):
        c=0
        for prestamo in self.prestamos:
            if prestamo.usuario.nombre == usuario.nombre:
                c+=1
        return c
    def mostrarprestamosusuario(self,usuario):
        for prestamo in self.prestamos:
            if prestamo.usuario.nombre==usuario.nombre:
                print(prestamo)
class Usuario:
    def __init__(self,codigo,tipo,nombre):
        self.codigo = codigo
        self.tipo = tipo
        self.nombre = nombre
    def __str__(self):
        return(f"codigo:{self.codigo}   nombre:{self.nombre}    tipo:{self.tipo}")
class Recurso:
    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre
    def __str__(self):
        return(f"codigo:{self.codigo}    nombre:{self.nombre}")
class Prestamo:
    def __init__ (self,usuario,recurso):
        self.usuario= usuario
        self.recurso=recurso
    def __str__(self):
        return(f"usuario:{self.usuario}\nrecurso:{self.recurso}")