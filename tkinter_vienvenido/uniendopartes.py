
from tkinter import ttk
import pymongo
from tkinter import *
'''
Se creó un procedimiento el cual se empleará para 
buscar en la base de datos, previamente creada por nosotros,
si existe el ciudadanoque se quiere buscar.
'''
def Buscar():
    '''
    Variable que presenta la etiqueta del mensaje para cargar los resultados.
    '''
    mensaje= Label(root, text='\n\ncargando resultados... ', fg='red')
    '''
    Ponemos la variable "mensaje" con la opción de un widget llene todo el marco.
    '''
    mensaje.pack()
    '''
    La siguiente línea de código se utiliza para crear una ventana de nivel superior
    encima de las diferentes ventanas.
    '''
    ventanaEmergente=Toplevel()
    '''
    Línea de código que se utiliza para poner un título a nuestra 
    ventana emergente.
    '''
    ventanaEmergente.title('DATOS DEL CIUDADANO... ')
    #ventanaEmergente.resizable(0,0)
    ventanaEmergente.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\PROYECTO GRUPAL\tkinter_vienvenido\folder.ico')
    '''
    Las siguientes líneas de código se utiliza para crear 
    el respectivo marco de nuestra interfaz gráfica.
    '''
    frame2 = Frame(ventanaEmergente ,width=250, height= 250)
    '''
    El marco de nuestra interfaz será de manera cuadrada, para lograrlo 
    se utiliza la función "grid()".
    '''
    frame2.grid()
    '''
    Se personaliza la configuración de nuestra interfaz gráfica, se 
    personaliza con el color y 
    '''
    frame2.config(bg='black')
    frame2.config(bd= 75)
    '''
    Se obtienen los nombres de nuestra base de datos previamente 
    creada, con la función "Get()"
    '''
    nombre= name.get().strip()
    '''
    Se obtienen los diferentes apellidos de nuestra base de datos 
    previamente creada, con la función "Get()".
    '''
    apellido1 = apellido.get().strip()
    '''
    A continuación, se presentan los datos colocados en la base de datos creada.
    '''
    datosPuestos = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'nombre':1}))
    datosPuestos1 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'apellido':1}))
    datosPuestos2 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'numeroCedula':1}))
    datosPuestos3 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'ocupacion':1}))
    datosPuestos4 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'Residencia':1}))
    datosPuestos5 = (mycol.find_one({'nombre':nombre, 'apellido':apellido1},{'_id':0,'Nacionalidad':1}))
    '''
    Se igualan los datos puestos a nuevas variables, para poder referirnos 
    a ellos en nuestra interfaz gráfica, que se utilizará para corroborar 
    los diferentes ciudadanos ingresados.
    '''
    dato1 = datosPuestos
    dato2 = datosPuestos1
    dato3 = datosPuestos2
    dato4 = datosPuestos3
    dato5 = datosPuestos4
    dato6 = datosPuestos5
    '''
    Se da una etiqueta para los diferentes posiciones de nuestra
    interfaz gráfica, por ende los datos de cada ciudadano tendrá
    una nueva etiqueta que no se va a repetir.
    '''
    Label(frame2, text=dato1).grid(row=1, column=0)
    Label(frame2, text=dato2).grid(row=2, column=0)
    Label(frame2, text=dato3).grid(row=3, column=0)
    Label(frame2, text=dato4).grid(row=4, column=0)
    Label(frame2, text=dato5).grid(row=5, column=0)
    Label(frame2, text=dato6).grid(row=6, column=0)
'''
Variable para conectar a nuestra base de datos.
'''
micliente=pymongo.MongoClient("mongodb://localhost:27017/")
'''
Se define el nombre de nuestra de nuestra base de datos.
'''
mydb=micliente["datosparaforo"]
'''
Se define el nombre de nuestra colección, que estará almacenada
en la base de datos.
'''
mycol=mydb["ciudadanos"]
'''
Se presenta nuestra
'''
'''
Se define la ruta de nuestar ventana flotante de nuestra 
interfaz gráfica.
'''
root =Tk()
'''
Se define el título de nuestra interfaz gráfica,
la cual manifiesta la verificación de los ciudadanos
que están en la base de datos.
'''
root.title('Verificación de Ciudadanos.')
#agrandar la ventana, abajo arriba, izquierda derecha
'''
Función que permite agrandar la ventana de todos 
los lados posibles.
'''
root.resizable(0,0)
root.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\programa2\programming_117944.ico')
'''
Se define las dimensiones de nuestro cuadro
que sirve de base para nuestra interfaz gráfica.
'''
frame = Frame(root ,width=500, height= 500)
frame.pack()
'''
Se personaliza nuestra interfaz gráfica de manera 
conveniente.
'''
# rellenar fill
# expand expandir
frame.config(bg='black')
frame.config(bd= 100)
'''
Se permite al usuario verificar al ciudadano si se encuentra o no 
en la base de datos.
'''
Label(frame, text='NOMBRE: ').grid(row=1, column=0)
#INGRESAR NOMBRE
'''
Se ingresa el nombre en la celda que le corresponde a cada 
coordenada.
'''
name = Entry(frame)
name.focus()
name.grid(row=1, column=1)
#INGRESAR APELLIDO
'''
Se permite al usuario verificar al ciudadano si se encuentra o no 
en la base de datos.
'''
Label(frame, text='APELLIDO: ').grid(row=2, column=0)
'''
Se ingresa el apellido en la celda que le corresponde a cada 
coordenada.
'''
apellido = Entry(frame)
apellido.focus()
apellido.grid(row=2, column=1)
'''
Función que permite buscar en la base de datos al ciudadano 
que se desea.
'''
ttk.Button(frame, text='Buscar', command=Buscar).grid(row=3, columnspan=2, sticky=W + E)
'''
Función para ejecutar nuestra interfaz gráfica.
'''
root.mainloop()


