import tkinter as tk
from tkinter import CENTER, Button, Entry, IntVar, Label, Radiobutton, StringVar, ttk
from tkinter.messagebox import showinfo

from setuptools import Command
from DB.base import Perro, Personal, Peluquero, Recepcionista
from tkinter import messagebox
import views.__init__

class App(tk.Frame, views.__init__):
    
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        views.__init__.__init__(self)
        self.parent = parent

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



if __name__ == "__main__":
  root = tk.Tk()
  run = App(root)
  root.mainloop()