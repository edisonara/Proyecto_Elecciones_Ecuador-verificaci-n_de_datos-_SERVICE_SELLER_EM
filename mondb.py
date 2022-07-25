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
    miCliente=pymongo.MongoClient("mongodb://localhost:27017/")
    def __init__(self, apellido, nombre, coleccion, db):
        self.apellido = apellido
        self.nombre= nombre
        self.coleccion = coleccion
        self.DB = db

    def __ConeccionDB(self):
        mydb=self.miCliente[self.DB]
        myCollection=mydb[self.coleccion]
        return myCollection

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
        elif dato == 'numeroCedula':
            return datoEncontrado['numeroCedula']
        elif dato == 'ocupacion':
            return datoEncontrado['ocupacion']
        elif dato == 'Residencia':
            return datoEncontrado['Residencia']
        elif dato == 'Nacionalidad':
            return datoEncontrado['Nacionalidad']

'''
10 documentos a la colección
'''

