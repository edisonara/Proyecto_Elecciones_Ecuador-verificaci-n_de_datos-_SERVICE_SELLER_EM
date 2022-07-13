
from datetime import datetime
from tkinter.tix import Tree

class Ciudadano:
    def __init__(self, nombre, apellido, numCedula, ocupacion, lugarDeOcupacion, lugarDeRecidencia, nacionalidad, fechaDeNacimiento, discapacidad ):
        self.nombre = nombre  # nn nn
        self.apellido = apellido# aa aa
        self.numCedula = numCedula # str ####################
        self.ocupacion = ocupacion  # ocupacion 
        self.lugarDeRecidencia = lugarDeRecidencia  # por num cedula 23 
        self.nacionalidad = nacionalidad #  # Ecuatoriana
        self.fechaDeNacimiento = fechaDeNacimiento  # NNNN-NN-NN
        self.discapacidad = discapacidad  # true - false

    @property
    def fechaDeNacimiento(self):
        return self._edad
    @fechaDeNacimiento.setter
    def fechaDeNacimiento(self, value):
        """
        Establece el valor del atributo de fecha
         Parámetros
         ----------
         valor: cadena
        
         aumenta
         ------
         ValorError
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)
        """
        try:
            if len(value) != 10:
                raise ValueError
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._edad= value

    '''@property
    def _nacionalidad(self):
        return self.__recidenciaEcuador
    @_nacionalidad.setter
    def _nacionalidad(self, extrangero):
        if extrangero != 'Ecuatoriana':
            pass'''


class VotanteSiNo(Ciudadano):

    def __ComprobarEcuatoriano(self):
        return self.nacionalidad == 'Ecuatoriano'

    
    def Mayor18(self):
        '''condicion principal '''
        if self.__ComprobarEcuatoriano== True:
            '''ocupar principalmente edad '''
            fechaActual = datetime.now()
            fechaActual = fechaActual.strftime("%Y-%m-%d")
            ano = int(self.fechaDeNacimiento[0:4])
            mes = int(self.fechaDeNacimiento[6])
            dia = int(self.fechaDeNacimiento[9])
            fechaActual= datetime.strptime(fechaActual, "%Y-%m-%d")
            diferenciaTiempo= fechaActual.year - ano
            diferenciaTiempo -= ((fechaActual.month,fechaActual.day)< (mes, dia))
            self.Edad= diferenciaTiempo
            return diferenciaTiempo > 18
        else:
            return False

    def EsParaVotoFacultativo(self):
        '''condicion principal secundaria '''
        if self.Mayor18== True:
            if self.discapacidad == True:
                return True
            elif self.ocupacion == 'Militar':
                return True
            elif self.ocupacion[0:7] == 'Policía':
                return True
            elif self.lugarDeRecidencia[0: 7] != 'Ecuador':
                return True

            elif (self.Edad > 16 and self.Edad < 18) or (self.Edad > 65):
                return True
            else:
                return False
        else:
            return False
            

class MiembroDeMesa():
    def EsVotante(self, parametro ):
        return parametro == True
    def OcupacionImportante(self, ocupacion  ):
        if self.EsVotante == True:
            if ocupacion[: 19] == 'Estudiante-Superior':
                return True
            elif ocupacion[:15] == 'Empleado-Publico':
                return True
            elif self.ocupacion[:15] == 'Empleado-Privado':
                return True

class Randon(MiembroDeMesa):
    def EsSeleccionado():

        pass



#  ________________________ MANEJO DE HOLIDAYS DE FECHA DE ACCESO _______________________________________    
class FeriadosTsachilas(holidays.HolidayBase):
    ''' Esta clase se encarga de definir nuevas fiestas personalisadas ante la necesidad de nosotros.\n
        recibe parametros de Holiday base para poder hacer todo lo necesario en esta clase.\n
        ------------------
        Atributos
        -----------------
        - country - el cual lo heredamos de holiday base, el cual da la forma para definir un pais.
        - provincia1 - el cual es una lista definido en la libreria builtins.pyi
        -  '''
    provincia=['EC-SD'] # guia de nuestro paso de dato 
    def __init__(self ,**lista): # será un diccionario con los argumentos ingresados, con ** hace que la función acepte infinitos argumentos, pero hay que aclarar primero el nombre del argumento.
        '''declaramos las funciones necesarias para tener nuestrosferiados a la mano'''
        self.country = 'ECU'
        self.provincia1=lista.pop('prov', 'ON')
        holidays.HolidayBase.__init__(self, **lista)

    def _populate(self, year):
        '''
            La documetacion se puede encontrar en: 
            https://www.eluniverso.com/noticias/ecuador/ecuador-calendario-de-feriados-nacionales-y-por-provincias-para-el-ano-2022-nota/
            - Cantonización de Santo Domingo: domingo 3 de julio (pasa al lunes 4)
            - Provincialización: domingo 6 de noviembre (pasa al lunes 7)
            ---------
            Parametros
            ----------
            El parametro que pasa a este metodo es el --year-- o año el cual servira para declarar nuevas fiestas con años dinamicos.
            '''

        
        self[date(2023, 2, 5)] = "La elección de autoridades seccionales en Ecuador 2023" #  los parametros son año, mes y dia. 
####_____________________________________________________________________________________________________
class Descuento:
    '''
        En esta clase es donde sucede toda la magia para condicionar los descuentos, aqui hacemos las condiciones para aplicar los datos. 
        
        Parametros
        ------------
        atributos
        ----------------
        - dia - la cual pasa el año mes y dia para saber si es feriado.
        - ApiEnLiena - la cual hacemos que pase el valor de la api y poder controlar el el error ValueError
         
         Metodos
         ------------
         - constructor - contine a los atributos.
         - dia - la cual es un decorador property el cual lo que hace es interpretar la lectura, escritura y borrado de atributos.
                 la cual podemos decir que documenta los mismos.\n 
                 Tambien esta el esta el metodo settter para esta funcion, basicamente se encarga de recibir los datos cuando se escriba.
         - __EsFiesta - este comprueba si un dia es feriado o no para poder hacer losen cuentos, en el menu principal. 
                         este es privado. 
         - ImprimirSiNo - el cual me hace es retornar true o falce, true cuando si exite el feriado y false cuando no. 
                 '''
    def __init__ (self, dia, API=False):
        '''
        este el costructor.

        parametros
        ----------
            - dia - fecha ingresada
            - consideramos la API para saver si el feriado esta en los feriados personalizados o no. 
            '''
        self.dia= dia
        self.ApiEnLinea= API

    @property # primero se define el property para envolver en una funcion al atributo con funciones o codigo que tiene el mismo.
    def dia(self):
        """
            Obtiene el valor del atributo de fecha
        """
        return self._dia 
    @dia.setter ## recibe los datos cuando se escriba
    def dia(self, numValor): 
        ''' metodo para poder dar un valor al atributo dia que esta en el costructor. 
         
         Parametros
         --------------
        numValor - el cual es str 
         
         rotorna una excepcion un mensaje al encontrar el error ValueError
          '''
        try:# en este bloque es donde ejecuteremos nuestro codigo para devolver un mensaje al tener un error, en este caso ValueError.
            if len(numValor)!=10:
                raise ValueError # raice como hacer una excepcion ante este error
            datetime.strptime(numValor, '%Y-%m-%d') # tonces pasa nomas, con lo que estabas. 
        except ValueError: # este bloque se ejecutara si el bloque try nofuncina y sabremos cual es el error. 
            raise ValueError('error ingrese en formato AAAA-MM_DD ;)') from None
        self._dia=numValor # pues si no pasa normal 

    def __EsFiesta(self, date, enLinea ):
        ''' esta parte contine las condiciones para ver si hay feriado o no en un fecha indicada.
            
            parametros
            ------------
            tenemos:
            - date - el cual es la fecha que tenemos o ingresamos.
            - enLinea - el cual pasa por defecto false, es para decir que si el feriado es de la API o las personalizadas. 
            -------
            -------
            la API utilizada es:
            - abstractapi el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
            entrar con previo registro. 
            '''
        ano, maso, menos = date.split('-')
        if enLinea: # condicion si es enLinea true
            ''' 
                se importa los datos de la API conocida como abstract api
                el cual se encuentra  en : https://app.abstractapi.com/api/holidays/documentation
                
                (ejemplo de fechas. https://www.youtube.com/watch?v=wSLbMwNyeLs)'''
            response = requests.get(f"https://holidays.abstractapi.com/v1/?api_key=91616907df7b4e8282a475d32edfa88a&country=EC&year={ano}&month={maso}&day={menos}")
            # pera utilizar este link utilizamos requests el cual nos ayudara a conectar con la API
            print(response.status_code) # retorna en pantalla un codigo 
            print(response.content)# retorna el contenido de dicha fecha consultada
            if response.content== b'[]':# verifica si el contenido es nulo manda una lista vacia o retorna False.
                return False
            return True # pues si no retorna true
        else: # nos conecta con los feriados personalizados o creados 
            FiestasApi=FeriadosTsachilas(prov='EC-SD') # instencia o crea un objeto de la clases feriadoTschilas con un parametro el cual es la cuadad de Santo Domingo
            return date in FiestasApi # retorna true o false dependiendo si la fecha ingresada 'date' se en cunetra en los feriados creados. 
    def ImprimirSiNo(self): # funcion que decide definitivamente
        '''este metodo llama a los metodos anteriores 
        para saber si si es ferido o no

        Datos importados
        ------
        - tenemos a la fecha - esatributo de este metodo
        - y tenemos la ApiEnLienea la cual es atributo de esta clase descuento. 
        - los datos del metodo __EsFiesta - la segunda mas importante en esta clase. '''
        if self.__EsFiesta(self.dia , self.ApiEnLinea): # retorna true dependiento del metodo __EsFiesta como pregunta este reotorna true.
            return True   
        return False # pues si no nada que ver. 
#____________________________ 



fecha = input('ingrese fecha en el formato año-mes-dia : ')
ciudadano = VotanteSiNo('ewe', 'ewew', 230000, 'feefef', 'efefe', 'eed', 'Ecuatori', fecha, True)
print(type(ciudadano.fechaDeNacimiento))

print(ciudadano.Mayor18())


persona= MiembroDeMesa()

help(persona)


'''def _Docord():
    def RecibirDatoClase(cls):
        class RecibeDelPadre(cls):
            Ciudadano.__init__(self, )
    return RecibirDatoClase'''
'''por definir un decorador '''