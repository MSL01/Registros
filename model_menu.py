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

        self.select_revisado = ttk.Combobox(self.root, width=59)
        self.select_revisado.place(x=20, y=90)

        self.select_no_revisado = ttk.Combobox(self.root, width=59)
        self.select_no_revisado.place(x=20, y=230)
        self.data_no = []
        self.data_si = []
        for i in range(self.df.Estado.size):
            if self.df['Estado'].values[i] == 'Revisado':
                self.data_si.append(self.df['Nombre del evento'].values[i])

            if self.df['Estado'].values[i] == 'Pendiente por revisar':
                self.data_no.append(self.df['Nombre del evento'].values[i])

        for x in self.data_no:
            self.select_no_revisado['values'] = (*self.select_no_revisado['values'], x)

        for x in self.data_si:
            self.select_revisado['values'] = (*self.select_revisado['values'], x)


        self.ver_no_revisado = ttk.Button(self.root, text='Ver', command=self.ver_info)
        self.ver_no_revisado.place(x=160, y=270)

        # ---------------------Eventos revisados ------------------------
        self.title_revisados = ttk.Label(self.root, text='EVENTOS REVISADOS', font="bold")
        self.title_revisados.place(x=100, y=20)

        self.ver_revisado = ttk.Button(self.root, text='Ver', command=self.ver_info2)
        self.ver_revisado.place(x=160, y=120)

        #-----------------------Registrar eventos-------------------------
        self.registrar = ttk.Button(self.root, text='Registrar un evento', command=self.gui_registrar_data)
        self.registrar.place(x=10,y=370)


    def ver_info(self):
        self.idd = self.df.index[self.df['Nombre del evento'] == self.select_no_revisado.get()].tolist()
        self.root.destroy()
        vw.main3(self.idd)


    def ver_info2(self):
        self.idd = self.df.index[self.df['Nombre del evento'] == self.select_revisado.get()].tolist()
        self.root.destroy()
        vw.main3(self.idd)
    def gui_registrar_data(self,event=None):
        self.root.destroy()
        create.main2()


if __name__ == "__main__":
    main()