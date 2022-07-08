import sqlite3

class DBConexion():

    def __init__(self, path='Peluqueria'):
        self.__path = path
        self.__miConexion = sqlite3.connect(self.__path)
        self.__miCursor = self.__miConexion.cursor()

        self.__crear_tablas()

    def __del__(self):
        self.__miConexion.close()

    def __crear_tablas(self):
        query = '''CREATE TABLE IF NOT EXISTS perro(id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                    nombre text unique,
                                                    dueno text,
                                                    direccion text,
                                                    telefono text,
                                                    banio INTEGER,
                                                    corte INTEGER,
                                                    comportamiento text)'''
        query2 = '''CREATE TABLE IF NOT EXISTS personal(id TEXT,
                                                    nombre text,
                                                    apellido text,
                                                    dni INTEGER,
                                                    telefono INTEGER,
                                                    anios_experiencia INTEGER,
                                                    email text,
                                                    direccion text,
                                                    sueldo int)'''
        self.ejecutar_query(query)
        self.ejecutar_query(query2)

    def ejecutar_query(self, query):
        self.__miCursor.execute(query)
        self.__miConexion.commit()

    def obtener_uno(self, query):
        self.ejecutar_query(query)
        return self.__miCursor.fetchone()

    def obtener_muchos(self, query):
        self.ejecutar_query(query)
        return self.__miCursor.fetchall()
