'''Modulo para trabajar con la o las bases de datos, que utilizaremos en el programa. El cual contiene clase o clases. 

Clase
-----
- BuscarEnBaseDato(): El cual nos conecta con el la base de datos y hace un busqueda en ella. '''
import pymongo

class BuscarEnBaseDato():
    '''Clase BuscarEnBaseDato, el cual hace la conección con el mongoDB y todos los datos en la que agamos la busqueda. 
    
    Atributos
    ---
    - self.apellido: El cual es de la persona el apellido. 
    - self.nombre: El cual es de la persona el nombre
    - self.datoRestriccion: El cual contiene el dato  buscar en la base de datos.
    - self.coleccion: La colección.  
    - self.DB: La base de datos. 
    - miCliente: el cual es estatico, que contiene la conección al mongoDB. 

    Metodos
    -----
    def __init__(self,  coleccion, db): Este es el constructor. 
    def recibirDatoBusqueda(self, dato): El cual recibe datos la un atributo en específico.
    def RecibirNombre(self, nombre, apellido): El cual pasa los valores que recibe a el atributo nombre y apellido.  
    def __ConeccionDB(self): Este sirve para hacer la coneccion con el mongoDB. 
    def BuscaRestriccion(self): El cual hace una busqueda de los datos a buscar en una  base de datos. 
    def Buscar(self, dato): Este sirve para buscar en la base de datos. 
    '''
    miCliente=pymongo.MongoClient("mongodb://localhost:27017/")
    def __init__(self, coleccion, db):
        '''Metodo constructor, el cual contiene los atributos de la clase BuscarEnBaseDato.
        
        Atributos.
        -----
        - apellido: De tipo inicial None. De tipo str. \n 
        - nombre: De tipo inicial None. De tipo str. \n 
        - datoRestriccion: De tipo inicial None, alberga str. 
        - coleccion: De tipo str. \n 
        - db: De tipo str. \n 

        Parametros.
        ------
        - coleccion: De tipo str. \n 
        - db: De tipo str. \n
        '''
        self.apellido = None
        self.nombre =None
        self.datoRestriccion = None
        self.coleccion = coleccion
        self.DB = db
    def recibirDatoBusqueda(self, dato):
        '''Metodo recibirDatoBusqueda de la clase BuscarEnBaseDato, el cual se encarga de cargar el dato que recibe a un atributo llamdo self.datoRestriccion. 
        
        Parametro.
        ------
        - dato: Tipo str. 
                El cual sirve de puente para pasar los datos al atributo datoRestriccion. '''
        self.datoRestriccion = dato
    
    def RecibirNombre(self, nombre, apellido):
        '''Metodo RecibirNombre de la clase BuscarEnBaseDato, el cual se encarga de cargar los datos a los atributos de nombre y apellido.
        
        Parametros.
        ----
        - nombre: Tipo str.\n
                    Ingresaria el nombre que tenga relacion en la base de datos de los ciudadanos.  
        - apellido: Tipo str.\n
                    Ingresaria el apellido que tenga relacion en la base de datos de los ciudadanos. '''
        self.nombre = nombre
        self.apellido = apellido
    def __ConeccionDB(self):
        '''Metodo pribado __ConeccionDB, el cual contiene la coneccion de la base de datos. 
        
        Retorna 
        ---
        - myCollection: El cual es la coneccion de la base de datos del mongoDB, obteniendo la coleccion a buscar los documentos. '''
        mydb=self.miCliente[self.DB]
        myCollection=mydb[self.coleccion]
        return myCollection
        
    def BuscaRestriccion(self):
        '''Metodo BuscaRestriccion, de la clase BuscarEnBaseDato, el cual hace una busqueda en la base de datos y retornaese valor. 
        
        Retorna.
        ------
        - return datoEncontrado['dato'], el cual rescata de una base de datos en tipo diccionarion el dato de una sección. '''
        coleccion =self.__ConeccionDB()
        datoEncontrado = coleccion.find_one({'descripcion':self.datoRestriccion})
        return datoEncontrado['dato']

    def Buscar(self, dato):
        '''Metodo Buscar de la clase BuscarEnBaseDato, el cual retorna los datos de un ciudadano. 
        
Parametros. 
-----
        - dato: De tipo str.
                ES la cualidad de una persona segun eso retornara algo. \n
                
-----
Ejemplo de dato. 
-----
        -  id: 000,  nombre: Mateo, apellido: Lopez,
        numeroCedula  :  1724564985   ,  ocupacion:Estudiante Superior,
         Residencia: Cuenca,    Nacionalidad : Ecuatoriano
         
-----
Retorna:
----
        - return datoEncontrado['nombre']:\n
                 Nos reotorna el --   nombre     ---- del ciudadano. \n
        - return datoEncontrado['apellido']:\n
                 Nos reotorna el --   apellido     ---- del ciudadano. \n
        - return datoEncontrado['numeroCedula']:\n
                 Nos reotorna el --   numero de cedula     ---- del ciudadano. \n
        - return datoEncontrado['ocupacion']:\n
                 Nos reotorna el --   ocupacion     ---- del ciudadano. \n
        - return datoEncontrado['Residencia']:\n
                 Nos reotorna el --    recidencia    ---- del ciudadano. \n
        - return datoEncontrado['fecha de nacimiento']:\n
                 Nos reotorna el --    fecha de nacimiento    ---- del ciudadano. \n
        - return datoEncontrado['discapacidad']:\n
                 Nos reotorna el --    discapacidad    ---- del ciudadano. \n
        - return datoEncontrado['Nacionalidad']:\n
                 Nos reotorna el --    nacionalidad    ---- del ciudadano.   \n
'''
        coleccion =self.__ConeccionDB()
        datoEncontrado = coleccion.find_one({'nombre':self.nombre, 'apellido':self.apellido})

        if dato == 'nombre':
            return datoEncontrado['nombre']
        elif dato == 'apellido':
            return datoEncontrado['apellido']
        elif dato == 'cedula de identidad':
            return datoEncontrado['cedula de identidad']
        elif dato == 'ocupacion':
            return datoEncontrado['ocupacion']
        elif dato == 'residencia ':
            return datoEncontrado['residencia ']
        elif dato == 'fecha de nacimiento':
            return datoEncontrado['fecha de nacimiento']
        elif dato == 'nacionalidad':
            return datoEncontrado['nacionalidad']
        elif dato == 'discapacidad':
            return datoEncontrado['discapacidad']

