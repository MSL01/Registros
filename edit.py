import pandas as pd
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
import model_menu as mm


def main(idd):
    root = Tk()
    gui = EditData(root, idd)
    gui.root.mainloop()
    return None

class EditData:
    def __init__(self, root, idd):
        self.root = root
        self.idd = idd
        self.root.geometry("636x591")
        self.root.title('Editar datos')
        self.root.resizable(False, False)
        self.df = pd.read_csv((r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv'), index_col=[0])

        self.nombre_label = ttk.Label(self.root, text='NOMBRE DEL EVENTO', font=("Arial", 15))
        self.nombre_label.place(x=220, y=20)
        self.nombre_ev = Entry(self.root, width=97)
        self.nombre_ev.place(x=20, y=70)
        self.nombre_ev.insert(0, self.df['Nombre del evento'][self.idd].to_string(index=False))

        self.tipo_label = ttk.Label(self.root, text='TIPO DE EVENTO', font=("Arial", 15))
        self.tipo_label.place(x=220, y=130)
        self.tipo_ev = Entry(self.root, width=97)
        self.tipo_ev.place(x=20, y=180)
        self.tipo_ev.insert(0, self.df['Tipo de evento'][self.idd].to_string(index=False))

        self.desc_label = ttk.Label(self.root, text='DESCRIPCIÓN DEL EVENTO', font=("Arial", 15))
        self.desc_label.place(x=200, y=230)
        self.desc_ev = Entry(self.root, width=97)
        self.desc_ev.place(x=20, y=290)
        self.desc_ev.insert(0, self.df['Descripcion'][self.idd].to_string(index=False))

        self.fecha_label = ttk.Label(self.root, text='FECHA', font=("Arial", 15))
        self.fecha_label.place(x=20, y=420)
        self.fecha_ev = DateEntry(self.root, width=20)
        self.fecha_ev.place(x=20, y=480)
        self.fecha_ev.delete(0, 'end')
        self.fecha_ev.insert(0, self.df['Fecha'][self.idd].to_string(index=False))

        self.est_title = ttk.Label(self.root, text='Estado del evento', font=("Arial", 15))
        self.est_title.place(x=210, y=420)
        self.est_evento_data = ttk.Combobox(self.root, values=['Pendiente por revisar', 'Revisado'], width=20)
        self.est_evento_data.place(x=210, y=480)
        self.est_evento_data.current(1)

        self.gest_title = ttk.Label(self.root, text='Gestión', font=("Arial", 15))
        self.gest_title.place(x=400, y=420)
        self.gest_evento_data = ttk.Combobox(self.root, values=['Requiere Gestión', 'Sin gestión'], width=20)
        self.gest_evento_data.place(x=400, y=480)
        self.gest_evento_data.current(1)

        self.btn_edit = ttk.Button(self.root, text='Aceptar', command=self.editedone)
        self.btn_edit.place(x=200, y=550)
        self.btn_delete = ttk.Button(self.root, text='Cancelar', command=self.root.destroy)
        self.btn_delete.place(x=330, y=550)

    def editedone(self):
        self.df['Nombre del evento'][self.idd] = self.nombre_ev.get()
        self.df['Tipo de evento'][self.idd] = self.tipo_ev.get()
        self.df['Descripcion'][self.idd] = self.desc_ev.get()
        self.df['Fecha'][self.idd] = self.fecha_ev.get()
        self.df['Estado'][self.idd] = self.est_evento_data.get()
        self.df['Gestion'][self.idd] = self.gest_evento_data.get()
        print(self.df.head())
        self.df.update(self.df)
        self.df.to_csv(r'C:\Users\migue\OneDrive\Escritorio\RegistroGUI\dataframe.csv')
        messagebox.showinfo('Información editada!', 'La información ha sido editada.')
        self.root.destroy()
        mm.main()

if __name__ == '__main__':
    main()