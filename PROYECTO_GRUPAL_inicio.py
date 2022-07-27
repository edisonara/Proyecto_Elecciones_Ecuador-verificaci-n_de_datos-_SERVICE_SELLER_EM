'''Pa'''
'''LIsta de restricciones con status. En la base de datos. '''
from datetime import datetime, date
import random
import holidays


class Ciudadano:
    '''Clase Ciudadano (clase padre para saber si es votante), el cual consentra todos los atributos que necesitaremos en nuestro programa.\n
    Aqui en esta clase definimos todas las cualidades de los ciudadanos que son utiles e nuestro programa. 

Atributos.
---------
- nombre: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad de nombre.
- apellido: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad de apellido.
- numCedula: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad de numero de cédula.
- ocupacion: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad de ocupación o trabajo.
- lugarDeRecidencia: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad del Lugar de recidencia. 
- nacionalidad: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad de la nacionalidad.
- fechaDeNacimiento: De tipo str.\n
        Contienen de la persona o ciudadano la cualidad de la fecha de nacimiento. 
- discapacidad: De tipo bool.\n
        Contienen de la persona o ciudadano la cualidad de si tiene o no discapacidad. 

Métodos.
-----
- >>> def __init__(self, nombre, apellido, numCedula, ocupacion, nacionalidad, fechaDeNacimiento, discapacidad ): Metodo constructor.\n
        El cual contiene a todos los atributos de la clase Ciudadano.
- >>> def fechaDeNacimiento(self): Metodo @property.\n 
        Es el metodo getter del atributo fechaDeNacimiento. Permite asignar una valor a un determinado atributo.
- >>> def fechaDeNacimiento(self, parametro): Metodo @getter.\n
        Es el metodo setter del atributo fechaDeNacimiento.  Metodo que permite obtener el atributo "fechaDeNacimiento" de la clase.
'''
    def __init__(self, nombre, apellido, numCedula, ocupacion, nacionalidad, fechaDeNacimiento, discapacidad ):
        '''Método constructor de la clase Ciudadano, el cual contiene atributos de una persona que es ciudadano.\n
        
        Parámetros.
        -----------
        Datos obtenidos principalmente en la cedula.
         - nombre: De tipo str.\n
                Datos ingresado simulando una cualidad llamado nombre, ingresa valores con formato ( NN NN).\n 
         - apellido: De tipo str.\n
                Datos ingresados simulando una cualidad llamado apellido, ingresa valores con formato ( AA AA).\n
         - numCedula: De tipo str.\n
                Datos ingresados para el numero de cedula, ingresa valores con formato ( ##########).\n
         - ocupacion: De tipo str.\n
                Datos ingresados para dar valor a la ocupación, ingresa valores con formato  (Nnn-Nnn-Nnnn-...), ejemplo ( Militar-....).\n
         - nacionalidad: De tipo str.\n
                Datos ingresados que serian la nacionalidad del ciudadano, ingresa valores con formato ( Nnnnnn), ejemplo (Ecuador).\n
         - fechaDeNacimiento: De tipo str.\n
                Datos ingresados para una fecha, ingresa valores con formato ( ####-##-##), ejemplo (2002-02-02).\n
         - discapacidad: De tipo bool.\n
                Datos ingresados que seria True o False, ingresa valores con formato ( True o False). \n

-----  
        Atributos.
        -----------
         - self.nombre: De tipo str. \n
                 Obtiene sus datos del parametro nombre.\n 
         - self.apellido: De tipo str. \n
                 Obtiene sus datos del parametro apellido. \n
         - self.numCedula: De tipo str. \n
                 Obtiene sus datos del parametro numCedula.\n
         - self.ocupacion: De tipo str. \n
                 Obtiene sus datos del parametro ocupacion.\n
         - self.lugarDeRecidencia: De tipo str. \n
                 Obtiene sus datos del parametro numCedula el cual solo obtiene los dos primeros digitos de este. Por lo que los dos primeros digitos muestra el secctor de nacimiento--------------------------.\n 
         - self.nacionalidad: De tipo str. \n
                 Obtiene sus datos del parametro nacionalidad.\n
         - self.fechaDeNacimiento: De tipo str. \n
                 Obtiene sus datos del parametro fechaDeNacimiento.\n
         - self.discapacidad: De tipo bool. \n
                 Obtiene sus datos del parametro discapacidad.\n'''
        self.nombre = nombre  # nn nn
        self.apellido = apellido# aa aa
        self.numCedula = numCedula # str ####################
        self.ocupacion = ocupacion  # ocupacion 
        self.lugarDeRecidencia =  self.numCedula[:2]
        self.nacionalidad = nacionalidad #  # Ecuatoriana
        self.fechaDeNacimiento = fechaDeNacimiento  # NNNN-NN-NN
        self.discapacidad = discapacidad  # true - false

    @property
    def fechaDeNacimiento(self):
        '''Método fechaDeNacimiento (recibe  @property), getter es el cual crea una variable, para ser utiliza en el metodo setter para el mismo atributo. al cual aplica.\n
        Aplica al atributo fechaDeNacimiento.\n
        
        Retorna.
        --------
         - self._edad: Libre para utilizar. '''
        return self._edad

    @fechaDeNacimiento.setter
    def fechaDeNacimiento(self, parametro):
        """Método fechaDeNacimiento. 
        Establece el valor del atributo de fechaDeNacimiento. 

         Parámetros
         ----------
         - parametro: cadena.
                    Pasael valor a la variable insertado por el metodo @property.
        
         Control Error:
         ------
         ValueError:
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)
        """
        try:
            if len(parametro) != 10:
                raise ValueError
            datetime.strptime(parametro, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._edad= parametro


class VotanteSiNo(Ciudadano):
    '''Clase VotanteSiNo (clase hija, recibe los datos heredados declass Ciudadano), el cual nos informaria si el ciudadano es votante o no.
    
------
    Métodos.
    -------
     - def ComprobarEcuatoriano(self ): Metodo que nos ayuda a comprobar si el ciudadano es Ecuatoriano o no.
     - def Mayor18(self): Metodo que prueba si es el metodo anterior es True, y si es mayor de edad. 
     - def EsParaVotoFacultativo(self): Metodo que comprueba si la versona votante puedetener voto facultativo. 
     '''

    def ComprobarEcuatoriano(self ):
        '''Método ComprobarEcuatoriano (metodo de la clase VotanteSiNo), el cual nos ayuda con la comprobación si la persona es o no Ecuatoriano.\n
        
        Retorna.
        --------
        - >>> if self.nacionalidad == 'Ecuatoriano': Si cumple sera True y si no False. 
                Si la nacionalidad en Ecuatoriano sera verdadero. '''
        if self.nacionalidad == 'Ecuatoriano':
            return True
        return False

    
    def Mayor18(self):
        '''Método Mayor18 (metodo de la clase VotanteSiNo), que nos ayuda a comprobar si es mayor de edad para ser votente normal. \n
            Siempre y cuando el metodo ComprobarEcuatoriano() se cumpla.\n
            Este metodo es el principal.\n 
            
        Recíbe Datos de:
        ----------------
        - self.ComprobarEcuatoriano(): Metodo. \n
                Condicion Principal. >>> if self.ComprobarEcuatoriano() == True:
        - self.fechaDeNacimiento: atributo. \n 
                El cual compara con la fecha actual para saber la edad exacta de una persona.\n

        Retorna.
        -------
        >>> (diferenciaTiempo > 18): El cual si es Mayor de 18 es mayor de edad, respondiendo con True y si no False. 

        Código. 
        ------
        Obtener la edad de la persona. Restando la fecha de actual con la fecha de nacimiento. 
            >>> diferenciaTiempo= fechaActual.year - ano

            >>> diferenciaTiempo -= ((fechaActual.month,fechaActual.day)< (mes, dia)): Obtenos un 1 o un 0 por lo que es una operacion lóguica. 
        '''
        
        if self.ComprobarEcuatoriano() == True:
            '''ocupar principalmente edad '''
            fechaActual = datetime.now()
            fechaActual = fechaActual.strftime("%Y-%m-%d")
            '''Dicidimos los datos obtenido el atributo de la fecha de nacimiento, en 3 secciones. '''
            ano = int(self.fechaDeNacimiento[0:4])
            mes = int(self.fechaDeNacimiento[6])
            dia = int(self.fechaDeNacimiento[9])
            fechaActual= datetime.strptime(fechaActual, "%Y-%m-%d")
            '''Operacion decisiva. Para tener la edad de la persona. '''
            diferenciaTiempo= fechaActual.year - ano
            diferenciaTiempo -= ((fechaActual.month,fechaActual.day)< (mes, dia))
            self.Edad= diferenciaTiempo
            
            return (diferenciaTiempo > 18)
        else:
            return False

    def EsParaVotoFacultativo(self):
        '''Método EsParaVotoFacultativo (Metodo de la clase VotanteSiNo), comprueba si el ciudadano tiene cualidades para tener voto facultativo o opcional. \n
        Condicion principal secundaria, que sera llamada el el objeto.

        -----
        -----
        Retorna.
        -----

        Principalmente tiene que ser votante, para poder tener las condiciones.
        - >>> dato = self.Mayor18()
        - >>> if dato == True: 


        True:  
        ---
        Si cumple las siguientes condiciones.
        >>> self.discapacidad == True: Si es discacitado manda True. \n
        >>> self.ocupacion[0:7] == 'Militar': Si la ocupacion es Militar Retorna true. \n
        >>> self.ocupacion[0:7] == 'Policía': Si la ocupacion es Policía Retorna true. \n
        >>> elif (self.Edad >= 16 and self.Edad < 18) or (self.Edad > 65): El cual condiciona si el ecuatoriano es de rango de 16 y 17, tambien que sea mayor de 65 años. Estos serian True.

        False: 
        ---
        - Si no cumple las condiciones anteriores retorna false. '''
        dato = self.Mayor18()
        if dato == True:
            if self.discapacidad == True:
                return True
            elif self.ocupacion[0:7] == 'Militar':
                return True
            elif self.ocupacion[0:7] == 'Policía':
                return True
            elif (self.Edad >= 16 and self.Edad < 18) or (self.Edad > 65):
                return True
            else:
                return False
        else:
            return False
            

class MiembroDeMesa:
    '''Clase MiembroDeMesa (clase padre), el cual nos ayuda a verifiar si es candidato para ser miembro de mesa. 
    
    Métodos.
    ----
    - >>> def EsVotante(self, Mayor18): El cual verifica si es votante gracias a un parametro. \n
    ..
    - >>> def OcupacionImportante(self,ocupacion, Mayor18): El cual nos ayuda a retornaar si es candidato o no. '''
    def EsVotante(self, Mayor18):
        '''Método EsVotante (de la clase MiembroDeMesa), el cual nos ayuda con la verificaion si es votante para ser tomado en cuenta. 
        
        Parámetros. 
        -----
        - Mayor18: El cual para un metodo de otra clase que contenga un True o false. 
        
        Retorna. 
        -----
        - Mayor18 == True: El cual si lo es para True y si no False. '''
        return Mayor18 == True

    def OcupacionImportante(self,ocupacion, Mayor18):
        '''Método OcupacionImportante (de la clase MiembroDeMesa), el cual es el metodo principal el cual nos ayuda a comprobar si tiene ocupacion importante.
        
        Parámetros.
        ----
        - ocupacion: Pasa una ocupacion de un ciudadano, pasar principalmente el valor de un atributo de un clase anterior. 
        - Mayor18: Valor que  pasa al metodo EsVotante, el cual pasa true o false. 
        
        -------
        Retorna. 
        ----
        
        True:
        ----
        Si cumple las siguientes condiciones. 
        >>> ocupacion[: 19] == 'Estudiante-Superior': El cual pasa true si es Estudiante-Superior. 
        >>> ocupacion[:15] == 'Empleado-Publico': El cual pasa true si es Empleado-Publico.
        >>> ocupacion[:15] == 'Empleado-Privado': El cual pasa true si es Empleado-Privado.

        false:
        --------
        - Si no cumple las condiciones anteriores, pasa False. 
        '''
        if self.EsVotante(Mayor18) == True:
            if ocupacion[: 19] == 'Estudiante-Superior':
                return True
            elif ocupacion[:15] == 'Empleado-Publico':
                return True
            elif ocupacion[:15] == 'Empleado-Privado':
                return True
        return False

class Randon(MiembroDeMesa):
    '''Método Randon (clase hija de MiembroDeMesa), el cual de forma  de random seleccionamos si se poseciona o no en la mesa de voto. 
    
    Metodos. 
    ----
    - def EsSeleccionado(self, ocupacion): El cual nos ayuda a definir de una forma random si es o no es. 
    '''
    def EsSeleccionado(self, ocupacion, Mayor18):
        ''' Método EsSeleccionado (matodo de la clase Randon), que nos ayuda a poner un true o false de forma que este decida cual. 
        
        Parametro.
        ----
        - ocupacion: Pasa un dato que es un atributo de una clase
        
        Retorna. 
        -----
        - dato: De tipo bools. \n
                El cual lo obtenemos de una lista de True y False y con random obtenemos cualesquiera de los dos. 
                
        Utilizamos.
        -----
        - self.OcupacionImportante(ocupacion): El cual fue heredado de la clase anterior. '''
        if self.OcupacionImportante(ocupacion, Mayor18)== True:
            ListaBool = [True, False]
            dato = random.choice(ListaBool)
            return dato
        return False
#  ________________________ MANEJO DE HOLIDAYS DE FECHA DE ACCESO _______________________________________    
class FechasVotaciones(holidays.HolidayBase):
    '''Clase FechasVotaciones (clase hija de la clase holidays.HolidayBase), el cual nos ayuda a definir las fechas tentativas de las votaciones oelecciones elctorales en el 2023. 
    
    Atributos.
    ----
    - self.country= El cual constiene el país al cual nos referimos.
    - holidays.HolidayBase.__init__(self, **lista): El cual lo obtenemos de la clase de heradación holidays.HolidayBase.
    
    Metodos.
    -----
    - def __init__(self ): Método constructor, el cual coniene los atributos de la clase a utilizar. 
    - def _populate(self, year=2023): Método que nos ayuda con la creación de las fechas de votación. '''
    def __init__(self ): 
        '''Método constructor(de la clase FechasVotaciones), el cual contiene los atributos a utilizar en el programa. \n
        Declaramos las funciones necesarias para tener nuestrosferiados a la mano.\n
        
        Atributos:
        ----
        - self.country: Que contiene el pais.
        - holidays.HolidayBase.__init__(self): Que nos ayuda a pasar los valores que nesecito para poder crear una nueva fecha.  '''
        self.country = 'ECU'
        
        holidays.HolidayBase.__init__(self)

    def _populate(self, year=2023):
        '''Metodo _populate (de la clase FechasVotaciones), que nos ayuda con la creación de las fechas de nuestro programa a realizarse en 2023. 
        
        Parametros.
        -----
        - year=2023: El cual nos ayuda a no marcar error al momento de pasar los datos, ya que esta funcion nesecita de un parametro. 
        '''
        self[date(2023, 2, 5)] = "La elección de autoridades seccionales en Ecuador 2023" 
        self[date(2023, 2, 5-1)] = self[date(2023, 2, 5)]
        self[date(2023, 2, 5-2)] = self[date(2023, 2, 5)]
####_____________________________________________________________________________________________________
class RestriccionVotacion:
    '''Clase RestriccionVotacion (clase qu recibe los datos de la clase FechasVotaciones), en una de los metodos.\n
    Nos ayuda a confirmar que una fecha ingresada es la misma que hemos creado en la clase FechasVotaciones. 

Atributos.
----
    - self.dia: De tipo Fecha. Dato a comprobar si cumple o no con la restricción. 

Metodos. 
----
    - def __init__ (self, dia): Metodo constructor de la clase RestriccionVotacion, que contiene el atributo. 
    - def dia(self): Metodo @property que nos ayuda crear una nueva variable para utilizar en el metodo setter. 
    - def dia(self, numValor): Metodo @setter que da una restricion al atributo self.dia.
    - def __EsVotacion(self, date): Metodo que comprueba si la fecha que pasamos coincide con la creada. 
    - def AplicaRestriccion(self): Metodo que reune toda la verificación de la fecha y retorna si coincide o no con la creada. 
     '''
    def __init__ (self, dia):
        '''Método constructor de la clase RestriccionVotacion, el cual contiene los metodos de la clase.
        
        Párametros.
        ----
        - dia: Pasa un formato fecha de tipo str. 
        
Atributos: 
---
        - self.dia: De tipo Fecha. Dato a comprobar si cumple o no con la restricción. '''
        self.dia= dia
        

    @property 
    def dia(self):
        '''Método dia (de la clase RestriccionVotacion), que nos ayuda creando una variable y pasandola al metodo  @property que nos ayuda con el setter. 
        
Retorna.
---
        - self._dia: Libre para utilizar.'''
        return self._dia 
    @dia.setter 
    def dia(self, numValor): 
        '''Método dia (de la clase RestriccionVotacion), el cual es el metodo getter del atributo self.dia. El cual nos ayuda a dar restricción en este caso el de evaluar una error. 
        
Parametro.
---
        - numValor: Que recibe dato de fecha.

 Control Error:
------
         ValueError:
             Si la cadena de valor no tiene el formato AAAA-MM-DD (por ejemplo, 2021-04-02)       
'''
        try:
            if len(numValor)!=10:
                raise ValueError 
            datetime.strptime(numValor, '%Y-%m-%d') 
        except ValueError: 
            raise ValueError('error ingrese en formato AAAA-MM_DD ;)') from None
        self._dia=numValor

    def __EsVotacion(self, date):
        '''Metodo __EsVotacion (de la clase RestriccionVotacion), que verifica si la fecha ingresada coincide con la fecha creada anteriormente, el la clase FechasVotaciones().\n
        La clase FechasVotaciones(), esta aqui como instencia o crea un objeto. 
        
Parametro.
----
        - date: De tipo fecha str. Recibe la fecha que se ingresa al momento de instanciar. 

Retorna:
-----
        - retorna true o false dependiendo si la fecha ingresada 'date' se encuentra en los dia de votaciones creadas. '''
        FiestasApi=FechasVotaciones() 
        return date in FiestasApi  
    
    def AplicaRestriccion(self):
        '''función AplicaRestriccion (de la clase RestriccionVotacion),  que decide definitivamente si la fecha es tiempo de votar o no, pasando true o false.
        
Retorna.
-----
        - Retorna True o False si self.__EsVotacion(self.dia), retorna true o false. '''
        if self.__EsVotacion(self.dia):
            return True   
        return False 




def PrintDeFechaVotacion():

    
    '''Procedimiento PrintDeFechaVotacion que nos ayuda a verificar si la fecha actual es la fecha de votación. 
    
    >>> fechaActual = datetime.now()
    >>> fechaActual = fechaActual.strftime("%Y-%m-%d")
    >>> votaciones = RestriccionVotacion(fechaActual)
    >>> if votaciones.AplicaRestriccion():
    >>>     es fecha.
    >>> else: 
    >>>     no es fecha. 
    '''
    '''Mensaje tiene que sere cambiables. '''
    fechaActual = datetime.now()
    fechaActual = fechaActual.strftime("%Y-%m-%d")
    votaciones = RestriccionVotacion(fechaActual)
    if votaciones.AplicaRestriccion():

        return('''
        **** Se le comunica al ciudadano/a que en los tres días previos a las elecciones  *******
        ****    no puede ingerir bebidas alcohólicas                                      *******
        ****    y/o sustancias estupefacientes                                            ******* ''')
    else: 
        return('''
         *****  Muy pronto se realizara esta actividad, gracias *****''')

def Presentacion():
    '''Procedimiento Presentacion que nos ayuda con la impresion de una portada.\n
    Portada encabezado del programa. \n
    >>> \n
    ----                  UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE\n
----                      S E R V E R _ S E L L E R  B M                            --------\n
----    PROGRAMA PARA SABER INFORMACIÓN SOBRE LAS BOTACIONES QUE SERAN EN EL 2023\n
----         REALIZADO POR EDISON ARAMBULO Y MATEO BELTRAN\n
---------------------------------------------------------------------------------------------\n
    '''
    print ('''
----                  UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
----                      S E R V E R _ S E L L E R  B M                            --------
----    PROGRAMA PARA SABER INFORMACIÓN SOBRE LAS BOTACIONES QUE SERAN EN EL 2023
----         REALIZADO POR EDISON ARAMBULO Y MATEO BELTRAN
--------------------------------------------------------------------------------------------- ''')

def pedirDatos(descripcion):
    '''Función pedirDatos, que nos ayuda con pedir datos de forma dinamica. 
    
Parametros.
----
    - descripción: De tipo str.\n
            Recibe una descripción de lo que quiere obtener.

Retorna.
-----
    - dato: De tipo str.\n
            El valor ingresado por el usuario. 
     '''
    dato = input(f'  > Ingrese del cuidadano, {descripcion} : ')
    return dato

def darDatos(descrip, descrip2, descrip3):
    '''Procedimiento que nos ayuda a imprimir los datos obtenidos de una forma visual.
    
    Parámetros.
    ---------
    - descrip: Tipo de dato no definido. 
    - descrip2: Tipo de dato no definido. 
    - descrip3: Tipo de dato no definido. 
    '''
    return(f'''
    EL CIUDADANO:
    · Puede votar : ({descrip}), 
    · Tiene voto facultativo : ({descrip2}) 
    · Pertenece a miembros de mesa : ({descrip3}). 
    __________________________________________________ ''')


if __name__=='__main__':
    ### application = SERVY_SELLER_BM()
    ### application.iniciar()
    ### application.LABEL('ingrese nombre',1,0 )
    ### application.ENTRY(1,1)
    ### application.LABEL('ingrese apellido',2,0 )
    ### application.ENTRY1(2,1)
    ### 
    ### obtenDatos = BuscarEnBaseDato(nombre=application.nombre, apellido=application.apellido,  coleccion="ciudadanos" ,db="datosparaforo")
    ### '''Intancia de la clase VotanteSiNo'''
    ### 
    ### ciudadano = VotanteSiNo(obtenDatos.Buscar('nombre'), obtenDatos.Buscar('apellido'), obtenDatos.Buscar('numeroCedula'), obtenDatos.Buscar('ocupacion'), obtenDatos.Buscar('Nacionalidad'),'2002-08-02' ,True)
    ### #application.VentanaSecundaria(ciudadano.nombre, ciudadano.apellido, ciudadano.numCedula, ciudadano.ocupacion, ciudadano.nacionalidad, ciudadano.fechaDeNacimiento, ciudadano.discapacidad)
    ### application.BUTTON( ciudadano.nombre, ciudadano.apellido, ciudadano.numCedula, ciudadano.ocupacion, ciudadano.nacionalidad, ciudadano.fechaDeNacimiento, ciudadano.discapacidad,3,0)
    ### application.terminar()
### 
### 

    exit()
    '''Funcion principal. Sirve para evitar que este codigo se ejecute en otro lugar. \n
Controla tambien toda la implementacion de las clases y procedimientos que tenemos en todo el programa.

Objetos
----
- ciudadano: Instancia de la clase VotanteSiNo. 
- ciudadanoMas: Instancia de la clase MiembroDeMesa. 

Entrada:
- nombre: De tipo str.\n
        Recibe del usuario el nombre. 
- apellido: De tipo str.\n
        Recibe del usuario el apellido.
- numCedula: De tipo str.\n
        Recibe del usuario el numero de cedula.
- ocupacion: De tipo str.\n
        Recibe del usuario la ocupación.
- nacionalidad: De tipo str.\n
        Recibe del usuario la nacionalidad. 
- fecha: De tipo str.\n
        Recibe del usuario la fecha de nacimiento.
- discapacidad: De tipo bool.\n
        Recibe del usuario el estado de la persona en cuestrion de la discapacidad.

Salida
----
- ciudadano.Mayor18(): Retorna si puede votar.
- ciudadano.EsParaVotoFacultativo(): Retorna si es voto facultativo.
- ciudadanoMas.OcupacionImportante(ciudadano.ocupacion, ciudadano.Mayor18()): Retorna si pertenece a miembros de mesa.'''
    '''Procedimiento de encabezado del programa. '''
    Presentacion()
    '''Para pedir datos para enviarlos en el objeto ciudadano'''
    nombre = pedirDatos('nombre, con formato (NN NN) ')
    '''Para pedir datos para enviarlos en el objeto ciudadano'''
    apellido = pedirDatos('apellido, con formato (AA AA)')
    '''Imprimir los datos ingresados al objeto con __dict__'''
    print(f'''
La persona tiene las siguientes cualidades que utilizamos en el programa:
    {ciudadano.__dict__}''')
    '''Instancia de la clase MiembroDeMesa. '''
    ciudadanoMas = MiembroDeMesa()
    '''Impresion de los resultados obtenidos al momento de utilizar los metodos respectivos '''
    darDatos(ciudadano.Mayor18(), ciudadano.EsParaVotoFacultativo(), ciudadanoMas.OcupacionImportante(ciudadano.ocupacion, ciudadano.Mayor18()))
    PrintDeFechaVotacion()

