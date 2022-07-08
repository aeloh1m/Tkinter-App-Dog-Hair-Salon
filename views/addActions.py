from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB.base import Perro, Peluquero, Recepcionista
import __init__

# ========================================================================
# ======== ## DOG CRUD ACTIONS ## ========================================
# ========================================================================


class dogActions(__init__):
    def __init__(self, parent):
        super().__init__(parent)

    def addDog(self):
        newDog = Perro(self.nombre.get(), self.dueño.get(),
                       self.direccion.get(), self.telefono.get())
        if self.corte.get() and self.baño.get():
            newDog.guardar(1, 1, self.comportamiento.get())
        elif self.baño.get() and self.corte.get() == False:
            newDog.guardar(1, 0, self.comportamiento.get())
        elif self.corte.get() and self.baño.get() == False:
            newDog.guardar(0, 1, self.comportamiento.get())
        else:
            newDog.guardar(0, 0, self.comportamiento.get())
        self.showDogs()
        self.clearSets()

    def updateDog(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea modificar el perro: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                self.newDog = Perro(nombre=self.nombre.get(), dueño=self.dueño.get(
                ), direccion=self.direccion.get(), telefono=self.telefono.get())
                if self.baño.get():
                    self.newDog = self.updateDog(
                        1, 0, self.comportamiento.get(), self.ID.get())
                elif self.corte.get():
                    self.newDog = self.updateDog(
                        0, 1, self.comportamiento.get(), self.ID.get())
                if self.corte.get() and self.baño.get():
                    self.newDog = self.updateDog(
                        1, 1, self.comportamiento.get(), self.ID.get())
                else:
                    self.newDog = self.updateDog(
                        0, 0, self.comportamiento.get(), self.ID.get())
                self.showDogs()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo modificar el registro")

    def deleteDog(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el perro: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                self.newDog = Perro(self.nombre.get(), self.dueño.get(
                ), self.direccion.get(), self.telefono.get())
                self.newDog = self.deleteDog(self.ID.get())
                self.showDogs()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro")


# ========================================================================
# ======== ## STAFF CRUD ACTIONS ## ======================================
# ========================================================================


class staffActions(__init__):
    def __init__(self, parent):
        super().__init__(parent)

    # Añadir Personal

    def addStaff(self):

        try:
            if self.puesto.get() == 1:
                self.personalPeluquero = Peluquero(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get(), direccion=self.direccion.get(
                ), telefono=self.telefono.get(), email=self.email.get(), sueldo=self.sueldo.get(), añosDeExpe=self.años_experiencia.get())
                self.personalPeluquero.guardarPeluquero()
                messagebox.showinfo(message="Se agrego correctamente el personal con ID: " +
                                    self.personalPeluquero.crearCodigo(), title="Título")
            else:
                self.personalRecepcionista = Recepcionista(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get(
                ), direccion=self.direccion.get(), telefono=self.telefono.get(), email=self.email.get(), sueldo=self.sueldo.get())
                self.personalRecepcionista.guardarRecepcionista()
                messagebox.showinfo(message="Se agrego correctamente el personal con ID: " +
                                    self.personalRecepcionista.crearCodigo(), title="Título")
            self.showStaff()
            self.clearSets()
        except:
            messagebox.showerror(
                "Error", "No se pudo agregar el nuevo registro a la base de datos")

    # Modificar Personal

    def updateStaff(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea modificar el personal: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                if self.ID.get()[:2] == "PQ":
                    self.personalPeluquero = Peluquero(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get(), direccion=self.direccion.get(
                    ), telefono=self.telefono.get(), email=self.email.get(), sueldo=self.sueldo.get(), añosDeExpe=self.años_experiencia.get())
                    self.personalPeluquero.modificarPeluquero(self.ID.get())
                elif self.ID.get()[:2] == "RC":
                    self.personalRecepcionista = Recepcionista(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get(
                    ), direccion=self.direccion.get(), telefono=self.telefono.get(), email=self.email.get(), sueldo=self.sueldo.get())
                    self.personalRecepcionista.modificarRecepcionista(
                        self.ID.get())
                self.showStaff()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo modificar el registro.")

    
    # Mostrar Personal

    def deleteStaff(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el personal: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):

                if self.ID.get()[:2] == "PQ":
                    self.personalPeluquero = Peluquero(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get(), direccion=self.direccion.get(
                    ), telefono=self.telefono.get(), email=self.email.get(), sueldo=self.sueldo.get(), añosDeExpe=self.años_experiencia.get())
                    self.personalPeluquero.eliminarPeluquero(self.ID.get())
                elif self.ID.get()[:2] == "RC":
                    self.personalRecepcionista = Recepcionista(nombre=self.nombre.get(), apellido=self.apellido.get(), dni=self.dni.get(
                    ), direccion=self.direccion.get(), telefono=self.telefono.get(), email=self.email.get(), sueldo=self.sueldo.get())
                    self.personalRecepcionista.eliminarRecepcionista(
                        self.ID.get())
                self.showStaff()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro.")
