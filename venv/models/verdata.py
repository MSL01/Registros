import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry

def main3():
    root = Tk()
    gui = ViewsEditDelete(root)
    gui.root.mainloop()
    return None

class ViewsEditDelete:
    def __init__(self, root):
        self.root = root
        self.root.geometry("636x591")
        self.root.title("Eventos registrados")
        self.root.resizable(False, False)
        self.df = pd.read_csv((r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv'), index_col=[0])

        self.nombre_title = ttk.Label(self.root, text='Nombre del evento', font=("Arial", 15))
        self.nombre_title.place(x=220, y=20)
        self.nombre_evento_data = Entry(self.root, text='', width=85, font=("Arial", 10))
        self.nombre_evento_data.place(x=20, y=70)

        self.tipo_title = ttk.Label(self.root, text='Tipo de evento', font=("Arial", 15))
        self.tipo_title.place(x=220, y=130)
        self.tipo_evento_data = Entry(self.root, text='', width=85, font=("Arial", 10))
        self.tipo_evento_data.place(x=20, y=180)

        self.desc_title = ttk.Label(self.root, text='Descripción del evento', font=("Arial", 15))
        self.desc_title.place(x=200, y=230)
        self.desc_evento_data = ttk.Label(self.root, text='', borderwidth=2, relief="groove")
        self.desc_evento_data.place(x=20, y=290)

        self.fecha_title = ttk.Label(self.root, text='Fecha del evento', font=("Arial", 15))
        self.fecha_title.place(x=20, y=420)
        self.fecha_evento_data = Entry(self.root, text='', width=20, font=("Arial", 10))
        self.fecha_evento_data.place(x=20, y=480)

        self.est_title = ttk.Label(self.root, text='Estado del evento', font=("Arial", 15))
        self.est_title.place(x=210, y=420)
        self.est_evento_data = Entry(self.root, text='', width=20, font=("Arial", 10))
        self.est_evento_data.place(x=210, y=480)

        self.gest_title = ttk.Label(self.root, text='Gestión', font=("Arial", 15))
        self.gest_title.place(x=400, y=420)
        self.gest_evento_data = Entry(self.root, text='', width=20, font=("Arial", 10))
        self.gest_evento_data.place(x=400, y=480)

        self.btn_edit = ttk.Button(self.root, text='Editar')
        self.btn_edit.place(x=200, y=550)
        self.btn_delete = ttk.Button(self.root, text='Eliminar')
        self.btn_delete.place(x=330, y=550)

if __name__ == "__main__":
    main3()