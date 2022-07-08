import addActions
import showActions
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB.base import Personal

class __init__():

    def __init__(self, parent):
        self.init_interface()
        self.parent = parent

    def init_interface(self):

        # configure the root window
        self.parent.title('Paws Grooming and Haircuts')
        self.parent.geometry('900x850')

        # Titulos
        header = ttk.Label(self.parent, text="Paws Grooming and Haircuts")
        header.place(x=255, y=15)
        header.config(font=("Verdana", 20))

        headerOpt = ttk.Label(self.parent, text="- Gestor Sección Perros -")
        headerOpt.place(x=320, y=55)
        headerOpt.config(font=("Verdana", 10))

        # label
        self.label = ttk.Label(self.parent, text='Hello, Tkinter!')
        self.label.pack()

        # Tables

        # buttons

        self.button = ttk.Button(self.parent, text='Tabla Perros')
        self.button['command'] = lambda: [
            showActions.showDogActions.showDogTable(), self.showInputs()]
        self.button.pack()
        self.button.place(x=790, y=90)

        self.button = ttk.Button(self.parent, text='Tabla Personal')
        self.button['command'] = lambda: [
            showActions.showStaffActions.showStaffTable(), self.showInputs()]
        self.button.pack()
        self.button.place(x=790, y=120)

        self.button = ttk.Button(self.parent, text='Inputs')
        self.button['command'] = self.showInputs
        self.button.pack()
        self.button.place(x=790, y=150)

        self.button = ttk.Button(self.parent, text='Mostrar Datos')
        self.button['command'] = showActions.showStaffActions.showStaff
        self.button.pack()
        self.button.place(x=790, y=180)

        ###

        self.button = ttk.Button(self.parent, text='Agregar')
        self.button['command'] = addActions.staffActions.addStaff
        self.button.pack()
        self.button.place(x=790, y=240)

        self.button = ttk.Button(self.parent, text='Limpiar')
        self.button['command'] = self.clearSets
        self.button.pack()
        self.button.place(x=790, y=270)

        self.button = ttk.Button(self.parent, text='Modificar')
        self.button['command'] = addActions.staffActions.updateStaff
        self.button.pack()
        self.button.place(x=790, y=300)

        self.button = ttk.Button(self.parent, text='Borrar')
        self.button['command'] = addActions.staffActions.deleteStaff
        self.button.pack()
        self.button.place(x=790, y=330)


    def showInputs(self):
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
        self.comportamiento.set("(null)")

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
        messagebox.showinfo(title='Information', message="hola")
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


    def button_clicked(self):
        messagebox.showinfo(title='Information', command=self.exitApp)