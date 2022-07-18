from cProfile import label
from email import message
from tkinter import ttk
import pymongo
from tkinter import *
def Buscar():
    mensaje= Label(root, text='\n\ncargando resultados... ', fg='red')
    mensaje.pack()
    ventanaEmergente=Toplevel()
    ventanaEmergente.title('DATOS DEL CIUDADANO... ')
    #ventanaEmergente.resizable(0,0)
    ventanaEmergente.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\PROYECTO GRUPAL\tkinter_vienvenido\folder.ico')
    frame2 = Frame(ventanaEmergente ,width=250, height= 250)
    frame2.grid()
# rellenar fill
# expand expandir
    frame2.config(bg='lightblue')
    frame2.config(bd= 75)
    datosPuestos = (mycol.find_one({'nombre':'Juan'},{'_id':0,'nombre':1}))
    Label(ventanaEmergente, text=datosPuestos).grid(row=0, column=0)
    Entry(ventanaEmergente, text=datosPuestos, state='disable').grid(row=0, column=1)

micliente=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=micliente["datosparaforo"]
mycol=mydb["ciudadanos"]
root =Tk()
root.title('Verificación de Ciudadanos.')
#agrandar la ventana, abajo arriba, izquierda derecha

root.resizable(0,0)
root.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\programa2\programming_117944.ico')

frame = Frame(root ,width=500, height= 500)
frame.pack()

# rellenar fill
# expand expandir
frame.config(bg='lightblue')
frame.config(bd= 100)
Label(frame, text='NOMBRE: ').grid(row=1, column=0)
#INGRESAR NOMBRE
name = Entry(frame)
name.focus()
name.grid(row=1, column=1)
#INGRESAR APELLIDO
Label(frame, text='APELLIDO: ').grid(row=2, column=0)
apellido = Entry(frame)
apellido.focus()
apellido.grid(row=2, column=1)

ttk.Button(frame, text='Buscar', command=Buscar).grid(row=3, columnspan=2, sticky=W + E)

root.mainloop()