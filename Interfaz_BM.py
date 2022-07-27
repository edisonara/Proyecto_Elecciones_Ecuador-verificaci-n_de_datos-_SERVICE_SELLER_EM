import webbrowser
from cProfile import label
from logging import root
import re
from tkinter import ttk, messagebox
from tkinter import *
from turtle import color
from urllib.response import addinfo
#from PROYECTO_GRUPAL_inicio import *
from mondb import *
from Restricciones_LOGUICA import *
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


''''Numero de mesas, vocales, ciudadanos por ciudades, x = tiempo, y= dato. 

hacer graficos de la distribucion, datos ordinales. '''

class SERVY_SELLER_BM:
    '''Clase SERVY_SELLER_BM, el cual es el principal, por donde se ejecutara el programa. Es la interfas que podra interactuar el usuario con el programa.\n
    Por motivos de que el programa interactua en bloques se hizo un poco complejo implementar atributos principales en esta clase.  
    
    Metodos
    ----
    - def iniciar(self): Metodo que crea el Rooter y el frame principal del programa. 
    - def LABEL(self, texto, fila, columna): Maqueta de el  label para pedir datos. 
    - def ENTRY(self, fila, columna): Maqueta para pedir datos de nombre.  
    - def ENTRY1(self, fila, columna): Maqueta para pedir datos de apellido. 
    - def BUTTON(self, fila , columna): Maqueta de un botton.
    - def VentanaSecundaria(self): Ventana secundaria del programa y coneccion con el mongoDB. 
    - def MenuSuperior(self, rooter): Maqueta para el munu superior del programa. 
    - def terminar(self): Termina el programa.'''

    def iniciar(self):
        '''Metodo iniciar, que crea el Rooter y el frame principal del programa. 
        
        Utiliza 
        -----
        - Tk: para el root. 
        - Frame. Para el frame del programa. 
        - self.MenuSuperior(self.root): Para poner le menu superior del programa.  '''
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
        '''CLase LABEL, el cual crea label o textos que ayudan con la interaccion del usuario y el programa. 
        
        Parametros.
        -------
        - texto: Es el texto del Label.  
        - fila: Es el fila del Label. 
        - columna: Es el  columna del Label. '''
        Label(self.frame, text=texto).grid(row=fila, column=columna)

    def ENTRY(self, fila, columna):
        '''Clase ENTRY, para recibir el nombre ingresado, el cual se manejara con dato. 
        
        Parametros.
        -----
        - fila: Es el fila del entry. 
        - columna: Es el  columna del entry '''
        self.nombre = StringVar()
        self.nombreRetorna = StringVar()
        self.variableNombre = Entry(self.frame, justify='center',textvariable=self.nombre)
        self.variableNombre.focus()
        self.variableNombre.grid(row=fila, column=columna)
       
    def ENTRY1(self, fila, columna):
        '''Clase ENTRY1, para recibir el apellido ingresado, el cual se manejara con dato. 
        
        Parametros.
        -----
        - fila: Es el fila del entry. 
        - columna: Es el  columna del entry '''
        self.apellido = StringVar()
        self.apellidoRetorna= StringVar()
        self.variableApellido = Entry(self.frame, justify='center',textvariable=self.apellido)
        self.variableApellido.focus()
        self.variableApellido.grid(row=fila, column=columna)
        

    def BUTTON(self, fila , columna):
        '''Clase BUTTON, Para hacer una accion, en este caso el de ventana secundaria, haciendolo ejecutar. 
        
        Parametros.
        -----
        - fila: Es el fila del boton. 
        - columna: Es el  columna del boton.  '''
        ttk.Button(self.frame, text='Buscar', command=self.VentanaSecundaria).grid(row=fila, column=columna, sticky=W + E)
    def VentanaSecundaria(self):
        '''Metodo VentanaSecundaria, el cual crea una ventana nueva y secundaria. Se le pasa los datos del mongoDB con respecto de de los datos ingresados. \n
        Contiene tre objetos para poder pasar esos datos. 
        Pasa todos los datos de estos Imprimiendo los datos en Labels y enrtys. 

        
        Instancias.
        ----
        - obtenDatos: El cual es Instancia de la clase BuscarEnBaseDato.
        - ciudadano: El cual es Instancia de la clase VotanteSiNo.
        - seleccionado: El cual es Instancia de la clase Randon.


        '''
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

        '''Instancias 
        '''
        '''Instancia de la clase BuscarEnBaseDato. '''
        obtenDatos = BuscarEnBaseDato(  coleccion="COL_CiudadanosEcuadorCNE" ,db="DB_CiudadanosEcuadorCNE")
        obtenDatos.RecibirNombre(nombre= nombre, apellido= apellido1)
        restricciones = BuscarEnBaseDato( coleccion="COL_Condiciones_Para_Votantes_CNE" ,db="DB_CiudadanosEcuadorCNE")
        restricciones.recibirDatoBusqueda('ciudadania')
        Ciudadania = restricciones.BuscaRestriccion()        
        restricciones.recibirDatoBusqueda('Mayor_Edad')
        Mayor_Edad = restricciones.BuscaRestriccion()
        restricciones.recibirDatoBusqueda('Facultativo_Ocupacion')
        Facultativo_Ocupacion = restricciones.BuscaRestriccion()
        restricciones.recibirDatoBusqueda('Tercera_Edad')
        Tercera_Edad = restricciones.BuscaRestriccion()
        restricciones.recibirDatoBusqueda('Adolescente_Edad')
        Adolescente_Edad = restricciones.BuscaRestriccion()
        restricciones.recibirDatoBusqueda('OcupacicionParaMesa_1')
        Ocupacicion_Para_Mesa = restricciones.BuscaRestriccion()

        '''Instancia de la clase VotanteSiNo. '''
        ciudadano = VotanteSiNo(obtenDatos.Buscar('nombre'), obtenDatos.Buscar('apellido'), obtenDatos.Buscar('cedula de identidad'), obtenDatos.Buscar('ocupacion'), obtenDatos.Buscar('residencia '), obtenDatos.Buscar('nacionalidad'),obtenDatos.Buscar('fecha de nacimiento'),obtenDatos.Buscar('discapacidad'))
        '''Instancia de la clase Randon. '''
        seleccionado = Randon()

        '''
        Se da una etiqueta para los diferentes posiciones de nuestra
        interfaz gráfica, por ende los datos de cada ciudadano tendrá
        una nueva etiqueta que no se va a repetir.
        '''
        self.nombreImprime = StringVar()
        self.nombreImprime.set(str(ciudadano.nombre))
        self.apellidoImprime = StringVar()
        self.apellidoImprime.set(str(ciudadano.apellido))
        self.numeroCedulaImprime = StringVar()
        self.numeroCedulaImprime.set(str(ciudadano.numCedula))
        ocupacionImprime= StringVar()
        ocupacionImprime.set(str(ciudadano.ocupacion))
        nacionalidadImprime = StringVar()
        nacionalidadImprime.set(str(ciudadano.nacionalidad))
        fechaDeNacimientoImprime = StringVar()
        fechaDeNacimientoImprime.set(str(ciudadano.fechaDeNacimiento))
        discapacidadImprime = StringVar()
        discapacidadImprime.set(str(ciudadano.discapacidad))


        '''Recibe los datos de los mensajes a ser utilizados en la impresion de datos. '''
        mensajesPrint = BuscarEnBaseDato( coleccion="COL_Mensajes_Para_Votantes_CNE" ,db="DB_CiudadanosEcuadorCNE")
        mensajesPrint.recibirDatoBusqueda('Mensaje Votante')
        MSGVotate = mensajesPrint.BuscaRestriccion()
        mensajesPrint.recibirDatoBusqueda('Mensaje Votante_Facultativo')          
        MSGFacultativo = mensajesPrint.BuscaRestriccion()
        mensajesPrint.recibirDatoBusqueda('Mensaje Miembro_Mesa')
        MSGMesa = mensajesPrint.BuscaRestriccion()
        mensajesPrint.recibirDatoBusqueda('Mensaje SI_DIA')
        MSGDiaSI = mensajesPrint.BuscaRestriccion()
        mensajesPrint.recibirDatoBusqueda('Mensaje NO_DIA')
        MSGDiaNO = mensajesPrint.BuscaRestriccion()
        mensajesPrint.recibirDatoBusqueda('lugar_votacion')
        mensajeLugar = mensajesPrint.BuscaRestriccion()



        fechaDeVotacion = StringVar()
        '''Función para ver si es fecha de votaciones....'''
        fechaDeVotacion.set(str(PrintDeFechaVotacion(MSGDiaSI,MSGDiaNO )))
        '''Funcion para dar los datos que se nesecita saber al momento de ir a votar. ....'''
        verificacionVotante = darDatos(MSGVotate, MSGFacultativo,MSGMesa, ciudadano.Mayor18(Mayor_Edad,Ciudadania ),  ciudadano.EsParaVotoFacultativo(Mayor_Edad, Ciudadania,Facultativo_Ocupacion, Tercera_Edad, Adolescente_Edad ), seleccionado.EsSeleccionado(ciudadano.ocupacion , ciudadano.Mayor18(Mayor_Edad,Ciudadania), Ocupacicion_Para_Mesa))
        self.verificacionVotante2 = StringVar()
        self.verificacionVotante2.set(str(verificacionVotante))
        self.verificacionVotante3 = StringVar()
        lugar = (str(mensajeLugar)+str(ciudadano.lugarDeRecidencia)+'.')
        self.verificacionVotante3.set(str(lugar))
        '''Impresion de los datos en pantalla---- con la label para el info de la informacion que se presenta en entry. '''
        Label(frameEmergente, justify='left',text='                  nombre ').grid(row=0, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=self.nombreImprime).grid(row=0, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=0, column=1)
        Label(frameEmergente, justify='left',text='                apellido ').grid(row=1, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=self.apellidoImprime).grid(row=1, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=1, column=1)
        Label(frameEmergente, justify='left',text='     Numero de Cédula ').grid(row=2, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=self.numeroCedulaImprime).grid(row=2, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=2, column=1)
        Label(frameEmergente, justify='left',text='          Ocupación ').grid(row=3, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=ocupacionImprime).grid(row=3, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=3, column=1)
        Label(frameEmergente, justify='left',text='       Nacionalidad ').grid(row=4, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=nacionalidadImprime).grid(row=4, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=4, column=1)
        Label(frameEmergente, justify='left',text='Fecha de Nacimiento ').grid(row=5, column=0)
        Entry(frameEmergente, justify='center' ,state= 'disabled',textvariable=fechaDeNacimientoImprime).grid(row=5, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=5, column=1)
        Label(frameEmergente, justify='left',text='       Discapacidad ').grid(row=6, column=0)
        Entry(frameEmergente, justify='center', state= 'disabled',textvariable=discapacidadImprime).grid(row=6, column=2)
        Label(frameEmergente, justify='left',text='.').grid(row=6, column=1)
        Label(ventanaEmergente, justify='center',textvariable=self.verificacionVotante2, fg='blue').grid()
        Label(ventanaEmergente, justify='center',textvariable=self.verificacionVotante3, fg='blue').grid()
        Ultim = Label(ventanaEmergente, justify='center',textvariable=fechaDeVotacion)
        Ultim.grid()
        #messagebox.showinfo('INFO DE VOTACION','gracias')

    def link_clicked(self):
        '''Metodo link_clicked, que abre un link al ejecutarlo. '''
        webbrowser.open("https://aceproject.org/ace-es/topics/lf/lfc/lfc24")
  

    def MenuSuperior(self, rooter):
        '''Metodo MenuSuperior, el cual contiene el esquema del menu superior del programa, con dos  campos el de archivos, ayuda. 
        
        Parametro.
        ----
        - rooter: El cual seria el root de la ventana principal o secundaria. '''
        menuBar = Menu(rooter)
        rooter.config(menu = menuBar)
        '''Se crea una sección para archivo, con dos subsecciones. '''
        fileMenu = Menu(menuBar, tearoff= 0)
        fileMenu.add_command(label= 'Descargrar Info', command=self.PDFGuardar)
        fileMenu.add_separator()
        fileMenu.add_command(label='Salir', command= rooter.quit)
        #-------------------------------------------------
        '''Se crea una sección para Ayuda, con una  subsección. '''
        helpMenu = Menu(menuBar, tearoff= 0)
        helpMenu.add_command(label= 'Base Legal', command= self.link_clicked)
        helpMenu.add_separator()
        #-------------------------------------------------
        #------------------------------------------------
        menuBar.add_cascade(label = 'Archivo', menu= fileMenu)
        menuBar.add_cascade(label = 'Ayuda', menu= helpMenu)
        

    def terminar(self):
        '''Metodo terminar, para poder encapsular el programa y salte la ejecución del programa al momento de iniciar. '''
        self.root.mainloop()

    def PDFGuardar(self):
        '''Metodo PDFGuardar, para guardar los datos '''
        PDF = canvas.Canvas("HHHHHHHHHHHHHHHHH.pdf")
        texto = PDF.beginText(50, 50)
        texto.setFont("Times-Roman", 12)
        texto.textLine(f"El ciudadano: {self.apellidoImprime} {self.numeroCedulaImprime}, con numero de cedula {self.numeroCedulaImprime}. ")
        texto.textLine(str(self.verificacionVotante2))
        texto.textOut(str(self.verificacionVotante3))
        PDF.drawText(texto)
        PDF.save()



if __name__=='__main__':
    '''Instacia del metodo SERVY_SELLER_BM'''
    application = SERVY_SELLER_BM()
    '''Inicia el programa. '''
    application.iniciar()
    '''Ingresa el nombre. '''
    application.LABEL('Ingrese Nombre',1,0 )
    application.ENTRY(1,1)
    '''Ingresa el apellido. '''
    application.LABEL('Ingrese Apellido',2,0 )
    '''Ingresar en entry'''
    application.ENTRY1(2,1)
    '''Ejecuta la ventana secundaria. '''
    application.BUTTON( 3,0)
    '''Construye el programa. '''
    application.terminar()