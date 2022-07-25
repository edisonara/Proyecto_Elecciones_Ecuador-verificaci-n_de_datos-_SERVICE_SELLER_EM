from cProfile import label
from logging import root
import re
from tkinter import ttk
from tkinter import *
from turtle import color
from urllib.response import addinfo
from PROYECTO_GRUPAL_inicio import *
from mondb import *



class SERVY_SELLER_BM:
    def __init__(self):
        #self.nombre = StringVar()
        #self.apellido =StringVar()
        pass

    def iniciar(self):
        self.root = Tk()
        self.root.title('VERIFICACIÓN DE VOTACIÓN DE CIUDADANOS')
        self.root.resizable(1,1)
        self.root.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\programa2\programming_117944.ico')
        self.frame = Frame(self.root ,width=500, height= 500)
        self.frame.pack()
        self.frame.config(bg='black')
        self.frame.config(bd= 150)
        self.MenuSuperior(self.root)
        

    def LABEL(self, texto, fila, columna):
        Label(self.frame, text=texto).grid(row=fila, column=columna)

    def ENTRY(self, fila, columna):
        self.nombre = StringVar()
        self.nombreRetorna = StringVar()
        self.variableNombre = Entry(self.frame, justify='center',textvariable=self.nombre)
        self.variableNombre.focus()
        self.variableNombre.grid(row=fila, column=columna)
       
    def ENTRY1(self, fila, columna):
        self.apellido = StringVar()
        self.apellidoRetorna= StringVar()
        self.variableApellido = Entry(self.frame, justify='center',textvariable=self.apellido)
        self.variableApellido.focus()
        self.variableApellido.grid(row=fila, column=columna)
        

    def BUTTON(self, fila , columna):
        ttk.Button(self.frame, text='Buscar', command=self.VentanaSecundaria).grid(row=fila, column=columna, sticky=W + E)
    def VentanaSecundaria(self):
        '''
        Variable que presenta la etiqueta del mensaje para cargar los resultados.
        '''
        #mensaje= Label(root, text='\n\ncargando resultados... ', fg='red')
        '''
        Ponemos la variable "mensaje" con la opción de un widget llene todo el marco.
        '''
        #mensaje.pack()
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
        ventanaEmergente.resizable(0,0)
        ventanaEmergente.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\PROYECTO GRUPAL\tkinter_vienvenido\folder.ico')
        '''
        Las siguientes líneas de código se utiliza para crear 
        el respectivo marco de nuestra interfaz gráfica.
        '''
        frameEmergente = Frame(ventanaEmergente ,width=250, height= 250)
        '''
        El marco de nuestra interfaz será de manera cuadrada, para lograrlo 
        se utiliza la función "grid()".
        '''
        frameEmergente.grid()
        '''
        Se personaliza la configuración de nuestra interfaz gráfica, se 
        personaliza con el color y 
        '''
        frameEmergente.config(bg='black')
        frameEmergente.config(bd= 100)
        '''
        Se obtienen los nombres de nuestra base de datos previamente 
        creada, con la función "Get()"
        '''
        nombre=self.variableNombre.get().strip()
        '''
        Se obtienen los diferentes apellidos de nuestra base de datos 
        previamente creada, con la función "Get()".
        '''
        apellido1 = self.variableApellido.get().strip()
        obtenDatos = BuscarEnBaseDato(nombre=nombre, apellido=apellido1,  coleccion="ciudadanos" ,db="datosparaforo")
        ciudadano = VotanteSiNo(obtenDatos.Buscar('nombre'), obtenDatos.Buscar('apellido'), obtenDatos.Buscar('numeroCedula'), obtenDatos.Buscar('ocupacion'), obtenDatos.Buscar('Nacionalidad'),'2002-08-02' ,True)
        seleccionado = Randon()

        '''
        Se da una etiqueta para los diferentes posiciones de nuestra
        interfaz gráfica, por ende los datos de cada ciudadano tendrá
        una nueva etiqueta que no se va a repetir.
        '''
        
        nombreImprime = StringVar()
        nombreImprime.set(str(ciudadano.nombre))

        apellidoImprime = StringVar()
        apellidoImprime.set(str(ciudadano.apellido))

        numeroCedulaImprime = StringVar()
        numeroCedulaImprime.set(str(ciudadano.numCedula))

        ocupacionImprime= StringVar()
        ocupacionImprime.set(str(ciudadano.ocupacion))

        nacionalidadImprime = StringVar()
        nacionalidadImprime.set(str(ciudadano.nacionalidad))

        fechaDeNacimientoImprime = StringVar()
        fechaDeNacimientoImprime.set(str(ciudadano.fechaDeNacimiento))

        discapacidadImprime = StringVar()
        discapacidadImprime.set(str(ciudadano.discapacidad))


        fechaDeVotacion = StringVar()
        fechaDeVotacion.set(str(PrintDeFechaVotacion()))

        verificacionVotante = darDatos(ciudadano.Mayor18(),  ciudadano.EsParaVotoFacultativo(), seleccionado.EsSeleccionado(ciudadano.ocupacion , ciudadano.Mayor18()))
        verificacionVotante2 = StringVar()
        verificacionVotante2.set(str(verificacionVotante))
        Label(frameEmergente, justify='center',text='nombre').grid(row=0, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=nombreImprime).grid(row=0, column=1)
        Label(frameEmergente, justify='center',text='apellido').grid(row=1, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=apellidoImprime).grid(row=1, column=1)
        Label(frameEmergente, justify='center',text='Numero de Cédula').grid(row=2, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=numeroCedulaImprime).grid(row=2, column=1)
        Label(frameEmergente, justify='center',text='Ocupación').grid(row=3, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=ocupacionImprime).grid(row=3, column=1)
        Label(frameEmergente, justify='center',text='Nacionalidad').grid(row=4, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=nacionalidadImprime).grid(row=4, column=1)
        Label(frameEmergente, justify='center',text='Fecha de Nacimiento').grid(row=5, column=0)
        Entry(frameEmergente, justify='center' ,state= 'disabled',textvariable=fechaDeNacimientoImprime).grid(row=5, column=1)
        Label(frameEmergente, justify='center',text='Discapacidad').grid(row=6, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=discapacidadImprime).grid(row=6, column=1)
        Label(ventanaEmergente, justify='center',textvariable=verificacionVotante2).grid()
        Label(ventanaEmergente, justify='center',textvariable=fechaDeVotacion).grid()
        
    def MenuSuperior(self, rooter):
        menuBar = Menu(rooter)
        rooter.config(menu = menuBar)
        fileMenu = Menu(menuBar, tearoff= 0)
        fileMenu.add_command(label= 'Descargrar Info')
        fileMenu.add_separator()
        fileMenu.add_command(label='Salir', command= rooter.quit)

        editMenu = Menu(menuBar, tearoff= 0)
        editMenu.add_command(label= 'Reporte de Uso')
        editMenu.add_checkbutton(label= 'check')
        editMenu.add_radiobutton(label= 'radio')
        editMenu.add_separator()
        editMenu.add_command(label='Reporte de Usuario')
        helpMenu = Menu(menuBar, tearoff= 0)
        helpMenu.add_command(label= 'Ayuda')
        helpMenu.add_command(label='Acerca de...')
        menuBar.add_cascade(label = 'Archivo', menu= fileMenu)
        menuBar.add_cascade(label = 'Reporte', menu= editMenu)
        menuBar.add_cascade(label = 'Ayuda', menu= helpMenu)

    def terminar(self):
        self.root.mainloop()




if __name__=='__main__':
    application = SERVY_SELLER_BM()
    application.iniciar()
    application.LABEL('Ingrese Nombre',1,0 )
    application.ENTRY(1,1)
    application.LABEL('Ingrese Apellido',2,0 )
    application.ENTRY1(2,1)
    
    #obtenDatos = BuscarEnBaseDato(nombre=application.nombreRetorna, apellido=application.apellidoRetorna,  coleccion="ciudadanos" ,db="datosparaforo")
    '''Intancia de la clase VotanteSiNo'''
    
    #ciudadano = VotanteSiNo(obtenDatos.Buscar('nombre'), obtenDatos.Buscar('apellido'), obtenDatos.Buscar('numeroCedula'), obtenDatos.Buscar('ocupacion'), obtenDatos.Buscar('Nacionalidad'),'2002-08-02' ,True)
    #application.VentanaSecundaria(ciudadano.nombre, ciudadano.apellido, ciudadano.numCedula, ciudadano.ocupacion, ciudadano.nacionalidad, ciudadano.fechaDeNacimiento, ciudadano.discapacidad)
    application.BUTTON( 3,0)
    application.terminar()