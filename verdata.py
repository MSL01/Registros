import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import edit as ed
import model_menu as mm
import tkinter as tk

def main3(idd):
    root = Tk()
    gui = ViewsEditDelete(root, idd)
    gui.root.mainloop()
    return None

class ViewsEditDelete:
    def __init__(self, root, idd):
        self.root = root
        self.idd = idd
        self.root.geometry("636x591")
        self.root.title("Eventos registrados")
        self.root.resizable(False, False)

        self.df = pd.read_csv((r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv'), index_col=[0])

        self.nombre_title = ttk.Label(self.root, text='Nombre del evento', font=("Arial", 15))
        self.nombre_title.place(x=220, y=20)
        self.nombre_evento_data = ttk.Label(self.root, text=self.df['Nombre del evento'][self.idd].to_string(index=False), width=95, borderwidth=2, relief="groove")
        self.nombre_evento_data.place(x=20, y=70)

        self.nombre_title = ttk.Label(self.root, text='ID:', font=("Arial", 15))
        self.nombre_title.place(x=420, y=20)
        self.nombre_evento_data = ttk.Label(self.root,
                                            text=self.idd,
                                            width=1, borderwidth=2, relief="groove")
        self.nombre_evento_data.place(x=460, y=25)

        self.tipo_title = ttk.Label(self.root, text='Tipo de evento', font=("Arial", 15))
        self.tipo_title.place(x=220, y=130)
        self.tipo_evento_data = ttk.Label(self.root, text=self.df['Tipo de evento'][self.idd].to_string(index=False), width=95, borderwidth=2, relief="groove")
        self.tipo_evento_data.place(x=20, y=180)

        self.desc_label = ttk.Label(self.root, text='Descripción del evento', font=("Arial", 15))
        self.desc_label.place(x=200, y=230)
        self.desc_ev = ttk.Label(self.root, text=self.df['Descripcion'][self.idd].to_string(index=False), width=95, borderwidth=2, relief="groove")
        self.desc_ev.place(x=20, y=290)


        self.fecha_title = ttk.Label(self.root, text='Fecha del evento', font=("Arial", 15))
        self.fecha_title.place(x=20, y=420)
        self.fecha_evento_data = ttk.Label(self.root, text=self.df['Fecha'][self.idd].to_string(index=False), width=20, borderwidth=2, relief="groove")
        self.fecha_evento_data.place(x=20, y=480)

        self.est_title = ttk.Label(self.root, text='Estado del evento', font=("Arial", 15))
        self.est_title.place(x=210, y=420)
        self.est_evento_data = ttk.Label(self.root, text=self.df.Estado[self.idd].to_string(index=False), width=20, borderwidth=2, relief="groove")
        self.est_evento_data.place(x=210, y=480)

        self.gest_title = ttk.Label(self.root, text='Gestión', font=("Arial", 15))
        self.gest_title.place(x=400, y=420)
        self.gest_evento_data = ttk.Label(self.root, text=self.df['Gestion'][self.idd].to_string(index=False), width=20, borderwidth=2, relief="groove")
        self.gest_evento_data.place(x=400, y=480)
        self.btn_edit = ttk.Button(self.root, text='Editar', command=self.editar)
        self.btn_edit.place(x=200, y=550)
        self.btn_delete = ttk.Button(self.root, text='Eliminar', command=self.deletedata)
        self.btn_delete.place(x=330, y=550)
        self.btn_delete = ttk.Button(self.root, text='Regresar', command=self.comeback)
        self.btn_delete.place(x=530, y=550)

    def comeback(self):
        self.root.destroy()
        mm.main()

    def deletedata(self):
        self.df = self.df.drop(self.idd)
        print(self.df.head())
        self.df.update(self.df)
        self.df.to_csv(r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv')
        messagebox.showinfo('Información eliminada!', 'Información eliminada')
        self.root.destroy()
        mm.main()

    def editar(self):
        self.root.destroy()
        ed.main(self.idd)


if __name__ == "__main__":
    main3()