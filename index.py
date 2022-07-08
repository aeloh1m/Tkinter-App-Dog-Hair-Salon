import tkinter as tk
from tkinter import CENTER, Button, Entry, IntVar, Label, Radiobutton, StringVar, ttk
from tkinter.messagebox import showinfo

from setuptools import Command
from DB.base import Perro, Personal, Peluquero, Recepcionista
from tkinter import messagebox

class App(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_interface()

        self.ID = tk.StringVar()
        self.nombre = tk.StringVar()
        self.dueño = tk.StringVar()
        self.direccion = tk.StringVar()
        self.telefono = tk.StringVar()
        self.baño = tk.BooleanVar()
        self.corte = tk.BooleanVar()
        self.comportamiento = tk.StringVar()

        self.codigo_identificatorio = tk.StringVar()
        self.apellido = tk.StringVar()
        self.dni = tk.StringVar()
        self.email = tk.StringVar()
        self.años_experiencia = tk.StringVar()
        self.sueldo = tk.StringVar()
        self.puesto = IntVar() #Basically Links Any Radiobutton With The Variable=i.
        
    def init_interface(self):
            
        # configure the root window
        self.parent.title('Paws Grooming and Haircuts')
        self.parent.geometry('900x850')

        # Titulos
        header = ttk.Label(self.parent, text="Paws Grooming and Haircuts")
        header.place(x=265, y=15)
        header.config(font=("Verdana", 20))

        # buttons
    
        self.button = ttk.Button(self.parent, width=14, text='Tabla Perros')
        self.button['command'] = lambda: [self.showDogTable(),self.showInputDog()]
        self.button.pack()
        self.button.place(x=790, y=90)

        self.button = ttk.Button(self.parent, width=14,text='Tabla Personal')
        self.button['command'] = lambda: [self.showStaffTable(),self.showInputStaff()]
        self.button.pack()
        self.button.place(x=790, y=120)

        self.button = ttk.Button(self.parent, width=14, text='Mostrar Datos')
        self.button['command'] = self.showStaff
        self.button.pack()
        self.button.place(x=790, y=150)

        self.button = ttk.Button(self.parent, width=14, text='Filtar por salario')
        self.button['command'] = self.filterSalary
        self.button.pack()
        self.button.place(x=790, y=180)

        self.button = ttk.Button(self.parent, width=14, text='Agregar')
        self.button['command'] = self.addStaff
        self.button.pack()
        self.button.place(x=790, y=240)

        self.button = ttk.Button(self.parent, width=14, text='Limpiar')
        self.button['command'] = self.clearSets
        self.button.pack()
        self.button.place(x=790, y=270)

        self.button = ttk.Button(self.parent, width=14, text='Modificar')
        self.button['command'] = self.updateStaff
        self.button.pack()
        self.button.place(x=790, y=300)

        self.button = ttk.Button(self.parent, width=14, text='Borrar')
        self.button['command'] = self.deleteStaff
        self.button.pack()
        self.button.place(x=790, y=330)


    
    def showDogTable(self):
        # Table for dogs

        self.dogTitle = Label(self.parent, text="Lista de perros:")
        self.dogTitle.place(x=10, y=90)
        self.dogTitle.config(width=107, height=120)

        self.dogTree=ttk.Treeview(self.dogTitle, height=16, columns=('#0','#1','#2','#3','#4','#5','#6','#7',))
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


        # labelName = Label(self.parent, text="Nombre:")
        # labelName.config(font=("Verdana", 9))
        # labelName.place(x=20, y=455)
        # entryName = Entry(self.parent, width=25, textvariable=self.nombre)
        # entryName.place(x=90, y=455)
        Comportamiento=ttk.Combobox(self.parent, values=["S/D", "Bien","Mal","Muy bien", "Muy mal"], state="readonly", width=13)
        Comportamiento.place(x=648, y=515)
        Comportamiento.current(0)

        labelmiComportamiento=Label(self.parent, text="Comportamiento:")
        labelmiComportamiento.place(x=520, y=515)
        labelmiComportamiento.config(font=("David", 9))


        self.button = ttk.Button(self.parent, width=14, text='Mostrar Datos')
        self.button['command'] = self.showDogs
        self.button.pack()
        self.button.place(x=790, y=150)

        self.button = ttk.Button(self.parent, width=14, text='Agregar')
        self.button['command'] = self.addDog
        self.button.pack()
        self.button.place(x=790, y=240)

        self.dogTree.bind("<Double-1>", self.selectOnClick)


    
    def showStaffTable(self):

        # Table for staff
        self.showInputStaff
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
        Peluquero = Radiobutton(self.parent, text="Peluquero", value=1, variable=self.puesto, tristatevalue=0)
        Peluquero.deselect()
        Peluquero.place(x=570, y=515)
        Recepcionista = Radiobutton(self.parent, text="Recepcionista", value=2, variable=self.puesto, tristatevalue=0)
        Recepcionista.deselect()
        Recepcionista.place(x=655, y=515)
        self.puesto.set(0)


        self.button = ttk.Button(self.parent, width=14, text='Mostrar Datos')
        self.button['command'] = self.showStaff
        self.button.pack()
        self.button.place(x=790, y=150)

        self.button = ttk.Button(self.parent, width=14, text='Agregar')
        self.button['command'] = self.addStaff
        self.button.pack()
        self.button.place(x=790, y=240)

        self.staffTree.bind("<Double-1>", self.selectOnClick)

    
    def showInputStaff(self):
        labelNombre = Label(self.parent, text="Nombre:")
        labelNombre.config(font=("David", 9))
        labelNombre.place(x=20, y=455)
        entryNombre = Entry(self.parent, width=25, textvariable=self.nombre)
        entryNombre.place(x=90, y=455)

        labelApellido = Label(self.parent, text="Apellido:")
        labelApellido.config(font=("David", 9))
        labelApellido.place(x=20, y=485)
        entryApellido = Entry(self.parent, width=25, textvariable=self.apellido)
        entryApellido.place(x=90, y=485)

        labelDNI = Label(self.parent, text="DNI:")
        labelDNI.config(font=("David", 9))
        labelDNI.place(x=20, y=515)
        entryDNI = Entry(self.parent, width=25, textvariable=self.dni)
        entryDNI.place(x=90, y=515)

        labelTelPers = Label(self.parent, text="Telefono:")
        labelTelPers.config(font=("David", 9))
        labelTelPers.place(x=260, y=455)
        entryTelPers = Entry(self.parent, width=25, textvariable=self.telefono)
        entryTelPers.place(x=350, y=455)

        labelEmail = Label(self.parent, text="Email:")
        labelEmail.config(font=("David", 9))
        labelEmail.place(x=260, y=485)
        entryEmail = Entry(self.parent, width=25, textvariable=self.email)
        entryEmail.place(x=350, y=485)

        labelExperiencia = Label(self.parent, text="Experiencia:")
        labelExperiencia.config(font=("David", 9))
        labelExperiencia.place(x=260, y=515)
        self.entryExperiencia = Entry(self.parent, width=25, textvariable=self.años_experiencia)
        self.entryExperiencia.place(x=350, y=515)

        labelSueldo = Label(self.parent, text="Sueldo:")
        labelSueldo.config(font=("David", 9))
        labelSueldo.place(x=520, y=485)
        entrySueldo = Entry(self.parent, width=25, textvariable=self.sueldo)
        entrySueldo.place(x=595, y=485)

        labelDireccion = Label(self.parent, text="Dirección:")
        labelDireccion.config(font=("David", 9))
        labelDireccion.place(x=520, y=455)
        entryDireccion = Entry(self.parent, width=25, textvariable=self.direccion)
        entryDireccion.place(x=595, y=455)

    def showInputDog(self):
        labelNombre = Label(self.parent, text="Nombre:")
        labelNombre.config(font=("David", 9))
        labelNombre.place(x=20, y=455)
        entryNombre = Entry(self.parent, width=25, textvariable=self.nombre)
        entryNombre.place(x=90, y=455)

        labelTelPers = Label(self.parent, text="Dueño:")
        labelTelPers.config(font=("David", 9))
        labelTelPers.place(x=20, y=485)
        entryTelPers = Entry(self.parent, width=25, textvariable=self.telefono)
        entryTelPers.place(x=90, y=485)

        labelTelPers = Label(self.parent, text="Direccion:")
        labelTelPers.config(font=("David", 9))
        labelTelPers.place(x=260, y=455)
        entryTelPers = Entry(self.parent, width=25, textvariable=self.telefono)
        entryTelPers.place(x=350, y=455)

        labelEmail = Label(self.parent, text="Telefono:")
        labelEmail.config(font=("David", 9))
        labelEmail.place(x=260, y=485)
        entryEmail = Entry(self.parent, width=25, textvariable=self.email)
        entryEmail.place(x=350, y=485)

        labelSueldo = Label(self.parent, text="Baño:")
        labelSueldo.config(font=("David", 9))
        labelSueldo.place(x=520, y=485)
        entrySueldo = Entry(self.parent, width=25, textvariable=self.sueldo)
        entrySueldo.place(x=595, y=485)

        labelDireccion = Label(self.parent, text="Corte:")
        labelDireccion.config(font=("David", 9))
        labelDireccion.place(x=520, y=455)
        entryDireccion = Entry(self.parent, width=25, textvariable=self.direccion)
        entryDireccion.place(x=595, y=455)

#============  # CRUD METHODS # ==============================================================

    # Añadir Personal

    def addStaff(self):

        try:
            if self.puesto.get() == 1:
                self.personalPeluquero = Peluquero(nombre=self.nombre.get(), apellido=self.apellido.get(),dni=self.dni.get(),direccion=self.direccion.get(),telefono=self.telefono.get(), email=self.email.get(),sueldo=self.sueldo.get(), añosDeExpe=self.años_experiencia.get())
                self.personalPeluquero.guardarPeluquero()
                messagebox.showinfo(message="Se agrego correctamente el personal con ID: " + self.personalPeluquero.crearCodigo(), title="Título")
            else:
                self.personalRecepcionista = Recepcionista(nombre=self.nombre.get(), apellido=self.apellido.get(),dni=self.dni.get(),direccion=self.direccion.get(),telefono=self.telefono.get(), email=self.email.get(),sueldo=self.sueldo.get())
                self.personalRecepcionista.guardarRecepcionista()
                messagebox.showinfo(message="Se agrego correctamente el personal con ID: " + self.personalRecepcionista.crearCodigo(), title="Título")
            self.showStaff()
            self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo agregar el nuevo registro a la base de datos")


    # Modificar Personal
    def updateStaff(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea modificar el personal: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                if self.ID.get()[:2] == "PQ":
                    self.personalPeluquero = Peluquero(nombre=self.nombre.get(), apellido=self.apellido.get(),dni=self.dni.get(),direccion=self.direccion.get(),telefono=self.telefono.get(), email=self.email.get(),sueldo=self.sueldo.get(), añosDeExpe=self.años_experiencia.get())
                    self.personalPeluquero.modificarPeluquero(self.ID.get())
                elif self.ID.get()[:2]== "RC": 
                    self.personalRecepcionista = Recepcionista(nombre=self.nombre.get(), apellido=self.apellido.get(),dni=self.dni.get(),direccion=self.direccion.get(),telefono=self.telefono.get(), email=self.email.get(),sueldo=self.sueldo.get())
                    self.personalRecepcionista.modificarRecepcionista(self.ID.get())
                self.showStaff()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo modificar el registro.")


    # Mostrar Personal
    def showStaff(self):
        registrosPers = self.staffTree.get_children()
        for elemento in registrosPers:
            self.staffTree.delete(elemento)
        try:
            miCursor = Personal().mostrarPersonal()
            for row in miCursor:
                self.staffTree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
            messagebox.showerror("Error", "No se pudo acceder a la BBDD.")

    def deleteStaff(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea eliminar el personal: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                
                if self.ID.get()[:2] == "PQ":
                    self.personalPeluquero = Peluquero(nombre=self.nombre.get(), apellido=self.apellido.get(),dni=self.dni.get(),direccion=self.direccion.get(),telefono=self.telefono.get(), email=self.email.get(),sueldo=self.sueldo.get(), añosDeExpe=self.años_experiencia.get())
                    self.personalPeluquero.eliminarPeluquero(self.ID.get())
                elif self.ID.get()[:2]== "RC":
                    self.personalRecepcionista = Recepcionista(nombre=self.nombre.get(), apellido=self.apellido.get(),dni=self.dni.get(),direccion=self.direccion.get(),telefono=self.telefono.get(), email=self.email.get(),sueldo=self.sueldo.get())
                    self.personalRecepcionista.eliminarRecepcionista(self.ID.get())
                self.showStaff()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro.")


    def loadList(self):
        try:
            self.showDogs()
            messagebox.showinfo(title="Conexión exitosa", message="Se ha conectado correctamente a la base de datos")
        except:
            messagebox.showerror(title="Error", message="No se pudo establecer la conexión con la base de datos.")
    
    
    def clearSets(self):
        self.ID.set("")
        self.puesto.set("")
        self.nombre.set("")
        self.apellido.set("")
        self.dni.set("")
        self.telefono.set("")
        self.años_experiencia.set("")
        self.email.set("")
        self.direccion.set("")
        self.sueldo.set("")
        self.dueño.set("")
        self.baño.set(False)
        self.corte.set(False)
        self.comportamiento.set("(vacio)")

    def filterSalary(self):
        registrosPers = self.staffTree.get_children()
        filter = self.entryFilter.get()
        
        for elemento in registrosPers:
            self.staffTree.delete(elemento)
        try:
            miCursor = Personal().__str__(filter)
            for row in miCursor:
                    self.staffTree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        except:
                messagebox.showerror("Error", "No se pudo acceder a la BBDD.")

            
  
    def exitApp(self):
        showinfo(title='Information', message="hola")
        valor=messagebox.askquestion("Salir","¿Está seguro que desea salir de la Aplicación?")
        if valor=="yes":
            self.parent.destroy()

    def selectOnClick(self, event):
        item = self.staffTree.identify('item', event.x, event.y)

        self.ID.set(self.staffTree.item(item, "text"))
        self.nombre.set(self.staffTree.item(item, "values")[0])
        self.apellido.set(self.staffTree.item(item, "values")[1])
        self.dni.set(self.staffTree.item(item, "values")[2])
        self.telefono.set(self.staffTree.item(item, "values")[3])
        self.años_experiencia.set(self.staffTree.item(item, "values")[4])
        self.email.set(self.staffTree.item(item, "values")[5])
        self.direccion.set(self.staffTree.item(item, "values")[6])
        self.sueldo.set(self.staffTree.item(item, "values")[7])

    def showDogs(self):
        registros = self.dogTree.get_children()
        for elemento in registros:
            self.dogTree.delete(elemento)
        try:
            
            miCursor = Perro().mostrarPerros()
            for row in miCursor:
                self.dogTree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        except:
            messagebox.showerror("Error", "No se pudo acceder a la BBDD")

    def addDog(self):
            newDog = Perro(self.nombre.get(), self.dueño.get(), self.direccion.get(), self.telefono.get())
            if self.corte.get() and self.baño.get():
                newDog.guardar(1,1,self.comportamiento.get())
            elif self.baño.get() and self.corte.get() == False:
                newDog.guardar(1,0,self.comportamiento.get())
            elif self.corte.get() and self.baño.get() == False:
                newDog.guardar(0,1,self.comportamiento.get())
            else:
                newDog.guardar(0,0,self.comportamiento.get())
            self.showDogs()
            self.clearSets()


    def updateDog(self):
        try:
            if messagebox.askyesno(message="¿Realmente desea modificar el perro: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                self.newDog = Perro(nombre=self.nombre.get(), dueño=self.dueño.get(), direccion=self.direccion.get(), telefono=self.telefono.get())
                if self.baño.get():
                    self.newDog = self.updateDog(1, 0, self.comportamiento.get(),self.ID.get())
                elif self.corte.get():
                    self.newDog = self.updateDog(0, 1, self.comportamiento.get(),self.ID.get())
                if self.corte.get() and self.baño.get():
                    self.newDog = self.updateDog(1, 1, self.comportamiento.get(),self.ID.get())
                else:
                    self.newDog = self.updateDog(0,0, self.comportamiento.get(),self.ID.get())
                self.showDogs()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo modificar el registro")

    def deleteDog(self):
        try:
           if messagebox.askyesno(message="¿Realmente desea eliminar el perro: {}?".format(self.nombre.get()),
                                   title="ADVERTENCIA"):
                self.newDog = Perro(self.nombre.get(), self.dueño.get(), self.direccion.get(), self.telefono.get())
                self.newDog = self.deleteDog(self.ID.get())
                self.showDogs()
                self.clearSets()
        except:
            messagebox.showerror("Error", "No se pudo eliminar el registro")

    def button_clicked(self):
        showinfo(title='Information', command=self.exitApp)



if __name__ == "__main__":
  root = tk.Tk()
  run = App(root)
  root.mainloop()