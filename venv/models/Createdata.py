import numpy as np
import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry

def main2():
    root = Tk()
    gui = CreateData(root)
    gui.root.mainloop()
    return None

class CreateData:
    def __init__(self, root):
        self.root = root
        self.root.geometry("524x514")
        self.root.title('Formulario de registro de datos')
        self.root.resizable(False, False)

        self.nombre_label = ttk.Label(self.root, text='NOMBRE DEL EVENTO')
        self.nombre_label.place(x=20,y=20)

        self.nombre_ev = Entry(self.root, width=80)
        self.nombre_ev.place(x=20,y=70)

        self.tipo_label = ttk.Label(self.root, text='TIPO DE EVENTO')
        self.tipo_label.place(x=20, y=110)

        self.tipo_ev = Entry(self.root, width=80)
        self.tipo_ev.place(x=20, y=160)

        self.desc_label = ttk.Label(self.root, text='DESCRIPCIÓN DEL EVENTO')
        self.desc_label.place(x=20, y=200)

        self.desc_ev = Text(self.root, height = 7, width = 60)
        self.desc_ev.place(x=20,y=250)

        self.fecha_label = ttk.Label(self.root, text='FECHA DEL EVENTO')
        self.fecha_label.place(x=20, y=380)

        self.fecha_ev = DateEntry(self.root, selectmode='day', width=40)
        self.fecha_ev.place(x=20,y=420)

        self.registrar_data = ttk.Button(self.root, text='Registrar datos', command=self.registrar_data)
        self.registrar_data.place(x=390, y=460)
        #self.data_pd = {'Nombre del evento': [], 'Tipo de evento': [],
        #                'Descripcion': [], 'Fecha': [], 'Estado': [],
        #                'Gestion': []
        #                }
        #self.df = pd.DataFrame(self.data_pd)
        self.df = pd.read_csv((r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv'), index_col=[0])
    def registrar_data(self, event=None):
        self.df = pd.concat([self.df, pd.DataFrame(
            {'Nombre del evento': self.nombre_ev.get(), 'Tipo de evento': self.tipo_ev.get(),
             'Descripcion': self.desc_ev.get("1.0", 'end-1c'), 'Fecha': self.fecha_ev.get(), 'Estado': 'Sin revisar',
             'Gestion': ''}, index=[0])], ignore_index=True)
        self.df.update(self.df)
        self.df.to_csv(r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv')
        messagebox.showinfo('Registro exitoso!', 'Información ingresada')


if __name__ == "__main__":
    main2()