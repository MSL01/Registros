import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import *
import Createdata as create
from tkinter import messagebox
import verdata as vw

def main():
    root = Tk()
    gui = ModelMenu(root)
    gui.root.mainloop()
    return None


class ModelMenu:
    def __init__(self, root):
        self.root = root
        self.root.geometry("413x416")
        self.root.title("Registro de eventos con python GUI")
        self.root.resizable(False, False)
        #--------------------------registros------------------------
        self.df = pd.read_csv((r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv'), index_col=[0])

        # ---------------------Eventos No revisados ------------------------
        self.title_no_revisados = ttk.Label(self.root, text='EVENTOS SIN REVISAR', font="bold")
        self.title_no_revisados.place(x=100, y=160)

        if 'Sin revisar' in self.df.Estado.values:
            self.select_no_revisado = ttk.Combobox(self.root, values=[self.df['Nombre del evento'].values[i] for i in range(self.df.columns.size)], width=59)
            self.select_no_revisado.place(x=20, y=230)
        else:
            self.select_no_revisado = ttk.Combobox(self.root, values='', width=59)
            self.select_no_revisado.place(x=20, y=230)

        self.idd = np.where(self.df['Nombre del evento'] == self.select_no_revisado.get())
        self.ver_no_revisado = ttk.Button(self.root, text='Ver', command=lambda : print(self.idd))
        self.ver_no_revisado.place(x=160, y=270)

        # ---------------------Eventos revisados ------------------------
        self.title_revisados = ttk.Label(self.root, text='EVENTOS REVISADOS', font="bold")
        self.title_revisados.place(x=100, y=20)

        if 'Revisado' in self.df.Estado.values:
            self.select_revisado = ttk.Combobox(self.root, values=[self.df['Nombre del evento'].values[i] for i in range(self.df.columns.size)], width=59)
            self.select_revisado.place(x=20, y=90)
        else:
            self.select_revisado = ttk.Combobox(self.root, width=59)
            self.select_revisado.place(x=20, y=90)

        self.ver_revisado = ttk.Button(self.root, text='Ver', command=ver_info)
        self.ver_revisado.place(x=160, y=120)



        #-----------------------Registrar eventos-------------------------
        self.registrar = ttk.Button(self.root, text='Registrar un evento', command=gui_registrar_data)
        self.registrar.place(x=10,y=370)

        # -----------------------Actualizar eventos-------------------------
        self.registrar = ttk.Button(self.root, text='Actualizar')
        self.registrar.place(x=290, y=370)

def gui_registrar_data(event=None):
    create.main2()
    pass

def ver_info():
    vw.main3()

if __name__ == "__main__":
    main()