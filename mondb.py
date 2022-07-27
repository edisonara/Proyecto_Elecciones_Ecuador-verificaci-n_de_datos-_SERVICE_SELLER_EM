'''Modulo para trabajar con la o las bases de datos, que utilizaremos en el programa. El cual contiene clase o clases. 

Clase
-----
- BuscarEnBaseDato(): El cual nos conecta con el la base de datos y hace un busqueda en ella. '''
import pymongo
import json

'''a={"a":10, "b":20}
b={"b":20, "a":10}
c = [json.dumps(a), json.dumps(b)]


set(c)
print(json.dumps(a) in c)
'''
class BuscarEnBaseDato():
    '''Clase BuscarEnBaseDato, el cual hace la conección con el mongoDB y todos los datos en la que agamos la busqueda. 
    
    Atributos
    ---
    - self.apellido: El cual es de la persona el apellido. 
    - self.nombre: El cual es de la persona el nombre
    - self.coleccion: La colección.  
    - self.DB: La base de datos. 

    Metodos
    -----
    def __init__(self, apellido, nombre, coleccion, db): Este es el constructor. 
    def __ConeccionDB(self): Este sirve para hacer la coneccion con el mongoDB. 
    def Buscar(self, dato): Este sirve para buscar en la base de datos. 
    '''
    miCliente=pymongo.MongoClient("mongodb://localhost:27017/")
    def __init__(self, coleccion, db):
        '''Metodo constructor, el cual contiene los atributos de la clase BuscarEnBaseDato.
        
Parametros.
-----
        - apellido: De tipo str. \n 
        - nombre: De tipo str. \n 
        - coleccion: De tipo str. \n 
        - db: De tipo str. \n 
        '''
        self.apellido = None
        self.nombre =None
        self.datoRestriccion = None
        self.coleccion = coleccion
        self.DB = db
    def recibirDatoBusqueda(self, dato):
        self.datoRestriccion = dato
    
    def RecibirNombre(self, nombre, apellido):
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

    def InsertarEnLista(self):
        lista = self.BuscaRestriccion()
        
    def BuscaRestriccion(self):
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
        elif dato == 'Residencia':
            return datoEncontrado['residencia']
        elif dato == 'fecha de nacimiento':
            return datoEncontrado['fecha de nacimiento']
        elif dato == 'nacionalidad':
            return datoEncontrado['nacionalidad']
        elif dato == 'discapacidad':
            return datoEncontrado['discapacidad']

'''
10 documentos a la colección
'''

