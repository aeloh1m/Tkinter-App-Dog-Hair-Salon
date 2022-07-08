from DB.DBactions import *

class Perro():

    def __init__(self, nombre=0, dueño=0, direccion=0, telefono=0):
        self.conexionDB = DBConexion()
        self.nombre = nombre
        self.dueño = dueño
        self.direccion = direccion
        self.telefono = telefono

    def mostrarPerros(self):
        cursor = self.conexionDB.obtener_muchos("select * from perro")
        return cursor

    def guardar(self, value1, value2, comportamiento):
        query = 'INSERT INTO perro VALUES(NULL,"{}","{}", "{}", "{}", "{}", "{}", "{}")'.format(
            self.nombre, self.dueño, self.direccion, self.telefono, value1, value2, comportamiento)
        self.conexionDB.ejecutar_query(query)

    def __str__(self):
        return ('{} {} {} {}'.format(self.nombre, self.dueño, self.direccion, self.telefono))

    def modificarPerro(self, baño, corte, comportamiento, id):
        query = 'UPDATE perro SET nombre="{}", dueño="{}", direccion="{}", telefono="{}", baño= baño, corte=corte, comportamiento="{}" WHERE id={}'.format(

            self.nombre, self.dueño, self.direccion, self.telefono, comportamiento, id)

        if baño:
            query = 'UPDATE perro SET nombre="{}", dueño="{}", direccion="{}", telefono="{}", baño= baño+1, corte=corte, comportamiento="{}" WHERE id={}'.format(

                self.nombre, self.dueño, self.direccion, self.telefono, comportamiento, id)

        elif corte:
            query = 'UPDATE perro SET nombre="{}", dueño="{}", direccion="{}", telefono="{}", baño= baño, corte=corte+1, comportamiento="{}" WHERE id={}'.format(

                self.nombre, self.dueño, self.direccion, self.telefono, comportamiento, id)

        if corte and baño:
            query = 'UPDATE perro SET nombre="{}", dueño="{}", direccion="{}", telefono="{}", baño= baño+1, corte=corte+1, comportamiento="{}" WHERE id={}'.format(

                self.nombre, self.dueño, self.direccion, self.telefono, comportamiento, id)

        self.conexionDB.ejecutar_query(query)

    def borrarPerro(self, id):
        query3 = f'DELETE FROM perro WHERE id="{id}"'
        self.conexionDB.ejecutar_query(query3)


class Personal():

    def __init__(self, nombre=0, apellido=0, dni=0, direccion=0, telefono=0, email=0, sueldo=0):
        self.conexionDB = DBConexion()
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.sueldo = sueldo
        self.direccion = direccion

    def mostrarPersonal(self):
        cursor = self.conexionDB.obtener_muchos("select * from personal")
        return cursor

    def mostrarPeluqueros(self):
        cursor = self.conexionDB.obtener_muchos(
            "select * from personal where anios_experiencia != '' ")
        return cursor

    def mostrarRecepcionistas(self):
        cursor = self.conexionDB.obtener_muchos(
            "select * from personal where anios_experiencia == '' ")
        return cursor

    def mostrarPorSueldo(self, cantSueldo):
        cursor = self.conexionDB.obtener_muchos(
            "select * from personal where sueldo >= {}".format(cantSueldo))
        return cursor


class Recepcionista(Personal):

    def __init__(self, nombre, apellido, dni, direccion, telefono, email, sueldo, añosDeExp):
        self.conexionDB = DBConexion()
        super().__init__(nombre, apellido, dni, direccion, telefono, email, sueldo)
        self.añosDeExp = añosDeExp

    def crearCodigo(self):
        doc = str(self.dni)
        return "RC_" + doc[-3:]

    def modificarRecepcionista(self, codigo):
        query3 = f'UPDATE personal SET nombre="{self.nombre}", apellido="{self.apellido}", dni="{self.dni}", telefono="{self.telefono}", anios_experiencia="{""}", email="{self.email}" , direccion="{self.direccion}", sueldo="{self.sueldo}" WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)

    def guardarRecepcionista(self):
        codigo = self.crearCodigo()
        query2 = 'INSERT INTO personal (id, nombre, apellido, dni, direccion, telefono, email, sueldo, anios_experiencia) VALUES (\"{}\", \"{}\", \"{}\",\"{}\",\"{}\", \"{}\", \"{}\",\"{}\",\"{}\")'.format(
            codigo, self.nombre, self.apellido, self.dni, self.direccion, self.telefono, self.email, self.sueldo, self.añosDeExp)
        self.conexionDB.ejecutar_query(query2)

    def eliminarRecepcionista(self, codigo):
        query3 = f'DELETE FROM personal WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)


class Peluquero(Personal):
    _sueldo = 0
    _codigo = 0

    def __init__(self, nombre, apellido, dni, direccion, telefono, email, sueldo, añosDeExpe=""):
        self.conexionDB = DBConexion()
        super().__init__(nombre, apellido, dni, direccion, telefono, email, sueldo)
        self.añosDeExp = añosDeExpe

    def crearCodigo(self):
        doc = str(self.dni)
        _codigo = "PQ_" + doc[-3:]
        return _codigo

    def consularPorsueldo(self, _sueldo):
        cursor = self.conexionDB.obtener_muchos(
            "select * from personal where sueldo > {}".format(_sueldo))
        return cursor

    def guardarPeluquero(self):
        codigo = self.crearCodigo()
        query2 = 'INSERT INTO personal (id, nombre, apellido, dni, direccion, telefono, email, sueldo, anios_experiencia) VALUES (\"{}\", \"{}\", \"{}\",\"{}\",\"{}\", \"{}\", \"{}\",\"{}\",\"{}\")'.format(
            codigo, self.nombre, self.apellido, self.dni, self.direccion, self.telefono, self.email, self.sueldo, self.añosDeExp)
        self.conexionDB.ejecutar_query(query2)

    def eliminarPeluquero(self, codigo):
        query3 = f'DELETE FROM personal WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)

    def modificarPeluquero(self, codigo):
        query3 = f'UPDATE personal SET nombre="{self.nombre}", apellido="{self.apellido}", dni="{self.dni}", telefono="{self.telefono}", anios_experiencia="{self.añosDeExp}", email="{self.email}" , direccion="{self.direccion}", sueldo="{self.sueldo}" WHERE id="{codigo}"'
        self.conexionDB.ejecutar_query(query3)
