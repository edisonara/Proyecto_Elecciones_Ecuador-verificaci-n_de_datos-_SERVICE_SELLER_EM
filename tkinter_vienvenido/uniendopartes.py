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
    frame2.config(bg='black')
    frame2.config(bd= 75)
    nombre= name.get().strip()
    apellido1 = apellido.get().strip()
    datosPuestos = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'nombre':1}))
    datosPuestos1 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'apellido':1}))
    datosPuestos2 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'numeroCedula':1}))
    datosPuestos3 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'ocupacion':1}))
    datosPuestos4 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'Residencia':1}))
    datosPuestos5 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'Nacionalidad':1}))
    dato1 = datosPuestos
    dato2 = datosPuestos1
    dato3 = datosPuestos2
    dato4 = datosPuestos3
    dato5 = datosPuestos4
    dato6 = datosPuestos5
    Label(frame2, text=dato1).grid(row=1, column=0)
    Label(frame2, text=dato2).grid(row=2, column=0)
    Label(frame2, text=dato3).grid(row=3, column=0)
    Label(frame2, text=dato4).grid(row=4, column=0)
    Label(frame2, text=dato5).grid(row=5, column=0)
    Label(frame2, text=dato6).grid(row=6, column=0)

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
frame.config(bg='black')
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