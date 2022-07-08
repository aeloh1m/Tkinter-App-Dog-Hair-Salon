from ast import Import
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import __init__
from DB.base import Perro, Personal

#========================================================================
#======== ## DOG SHOW ACTIONS ## ========================================
#========================================================================

class showDogActions(__init__):
    def __init__(self, parent):
        super().__init__(parent)

    def showDogTable(self):
        # Table for dogs

        self.dogTitle = Label(self.parent, text="Lista de perros:")
        self.dogTitle.place(x=10, y=90)
        self.dogTitle.config(width=107, height=120)

        self.dogTree = ttk.Treeview(self.dogTitle, height=16, columns=(
            '#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7',))
        self.dogTree.place(x=0, y=0)
        self.dogTree.column('#0', width=40)
        self.dogTree.heading('#0', text="ID", anchor=CENTER)
        self.dogTree.column('#1', width=105)
        self.dogTree.heading('#1', text="Nombre", anchor=CENTER)
        self.dogTree.column('#2', width=105)
        self.dogTree.heading('#2', text="Dueño", anchor=CENTER)
        self.dogTree.column('#3', width=100)
        self.dogTree.heading('#3', text="Dirección", anchor=CENTER)
        self.dogTree.column('#4', width=110)
        self.dogTree.heading('#4', text="Telefono", anchor=CENTER)
        self.dogTree.column('#5', width=100)
        self.dogTree.heading('#5', text="Baño", anchor=CENTER)
        self.dogTree.column('#6', width=80)
        self.dogTree.heading('#6', text="Corte", anchor=CENTER)
        self.dogTree.column('#7', width=110)
        self.dogTree.heading('#7', text="Comportamiento", anchor=CENTER)

        Comportamiento = ttk.Combobox(self.parent, values=[
                                      "(null)", "Bien", "Mal", "Muy bien", "Muy mal"], state="readonly")
        Comportamiento.place(x=570, y=540)
        Comportamiento.current(0)

        labelmiComportamiento = Label(self.parent, text="Comportamiento:")
        labelmiComportamiento.place(x=445, y=540)
        labelmiComportamiento.config(font=("David", 9))

        self.button = ttk.Button(self.parent, text='Mostrar Datos')
        self.button['command'] = self.showDogs
        self.button.pack()
        self.button.place(x=790, y=180)

        self.button = ttk.Button(self.parent, text='Agregar')
        self.button['command'] = self.addDog
        self.button.pack()
        self.button.place(x=790, y=240)

        self.dogTree.bind("<Double-1>", self.selectOnClick)

    def showDogs(self):
        registros = self.dogTree.get_children()
        for elemento in registros:
            self.dogTree.delete(elemento)
        try:

            miCursor = Perro().mostrarPerros()
            for row in miCursor:
                self.dogTree.insert("", 0, text=row[0], values=(
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        except:
            messagebox.showerror("Error", "No se pudo acceder a la BBDD")


#========================================================================
#======== ## STAFF SHOW ACTIONS ## ======================================
#========================================================================

class showStaffActions(__init__):
    def __init__(self, parent):
        super().__init__(parent)

    def showStaffTable(self):

        # Table for staff
        self.showInputs
        self.staffTitle = Label(self.parent, text="Lista de personal:")
        self.staffTitle.place(x=10, y=90)
        self.staffTitle.config(width=107, height=120)

        self.staffTree = ttk.Treeview(self.staffTitle, height=16,
                                      columns=('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8',))
        self.staffTree.place(x=0, y=0)
        self.staffTree.column('#0', width=40)
        self.staffTree.heading('#0', text="ID", anchor=CENTER)
        self.staffTree.column('#1', width=105)
        self.staffTree.heading('#1', text="Nombre", anchor=CENTER)
        self.staffTree.column('#2', width=100)
        self.staffTree.heading('#2', text="Apellido", anchor=CENTER)
        self.staffTree.column('#3', width=90)
        self.staffTree.heading('#3', text="Dni", anchor=CENTER)
        self.staffTree.column('#4', width=95)
        self.staffTree.heading('#4', text="Telefono", anchor=CENTER)
        self.staffTree.column('#5', width=70)
        self.staffTree.heading('#5', text="Exp", anchor=CENTER)
        self.staffTree.column('#6', width=110)
        self.staffTree.heading('#6', text="Email", anchor=CENTER)
        self.staffTree.column('#7', width=70)
        self.staffTree.heading('#7', text="Dirección", anchor=CENTER)
        self.staffTree.column('#8', width=70)
        self.staffTree.heading('#8', text="Sueldo", anchor=CENTER)

        labelPuesto = Label(self.parent, text="Puesto:")
        labelPuesto.config(font=("David", 9))
        labelPuesto.place(x=520, y=515)
        Peluquero = Radiobutton(
            self.parent, text="Peluquero", value=1, variable=self.puesto, tristatevalue=0)
        Peluquero.deselect()
        Peluquero.place(x=570, y=515)
        Recepcionista = Radiobutton(
            self.parent, text="Recepcionista", value=2, variable=self.puesto, tristatevalue=0)
        Recepcionista.deselect()
        Recepcionista.place(x=655, y=515)
        self.puesto.set(0)

        self.button = ttk.Button(self.parent, text='Mostrar Datos')
        self.button['command'] = self.showStaff
        self.button.pack()
        self.button.place(x=790, y=180)

        self.button = ttk.Button(self.parent, text='Agregar')
        self.button['command'] = self.addStaff
        self.button.pack()
        self.button.place(x=790, y=240)

        self.staffTree.bind("<Double-1>", self.selectOnClick)

    def showStaff(self):
        registrosPers = self.staffTree.get_children()
        for elemento in registrosPers:
            self.staffTree.delete(elemento)
        try:
            miCursor = Personal().mostrarPersonal()
            for row in miCursor:
                self.staffTree.insert("", 0, text=row[0], values=(
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
            messagebox.showerror("Error", "No se pudo acceder a la BBDD.")
