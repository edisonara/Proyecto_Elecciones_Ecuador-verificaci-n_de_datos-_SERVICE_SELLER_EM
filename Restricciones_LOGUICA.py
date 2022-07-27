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
    def __init__(self, nombre, apellido, numCedula, ocupacion, recidencia, nacionalidad, fechaDeNacimiento, discapacidad ):
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
        self.lugarDeRecidencia = recidencia
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
    
    Métodos.
    -------
     - def ComprobarEcuatoriano(self ): Metodo que nos ayuda a comprobar si el ciudadano es Ecuatoriano o no.
     - def Mayor18(self): Metodo que prueba si es el metodo anterior es True, y si es mayor de edad. 
     - def EsParaVotoFacultativo(self): Metodo que comprueba si la versona votante puedetener voto facultativo. 
     '''
    def ComprobarEcuatoriano(self , nacionalidad):
        '''Método ComprobarEcuatoriano (metodo de la clase VotanteSiNo), el cual nos ayuda con la comprobación si la persona es o no Ecuatoriano.\n
        
        Parametro.
        ---------
        -  nacionalidad: De tipo str.\n
                Es la restriccion de este metodo. 
        Retorna.
        --------
        
        True:  
        ---
        Si cumple las siguientes condiciones.
        - if self.nacionalidad == nacionalidad:
        
        False: 
        ---
        - Si no cumple las condiciones anteriores retorna false.
        '''
        if self.nacionalidad == nacionalidad:                                                                 # CondicionCIudadano
            return True
        return False
    
    def Mayor18(self, mayorEdad, nacionalidad):
        '''Método Mayor18 (metodo de la clase VotanteSiNo), que nos ayuda a comprobar si es mayor de edad para ser votente normal. \n
            Siempre y cuando el metodo ComprobarEcuatoriano() se cumpla.\n
            Este metodo es el principal.\n 
            
        Recíbe Datos de:
        ----------------
        - self.ComprobarEcuatoriano(): Metodo. \n
                Condicion Principal. >>> if self.ComprobarEcuatoriano() == True:
        - self.fechaDeNacimiento: atributo. \n 
                El cual compara con la fecha actual para saber la edad exacta de una persona.\n
        
        Parametro.
        -------
        - mayorEdad: De tipo str. 
                Dato de una base de datos. 
        - nacionalidad: De tipo str. 
                Dato de una base de datos.
                
        Retorna. 
        ----
        
        True
        ----
        - Si cumple que (diferenciaTiempo > int(mayorEdad)). 
        - Si cumple que self.ComprobarEcuatoriano(nacionalidad=nacionalidad) == True. 
        
        False
        ----
        - Si no cumple lo anterior propuesto. '''
        if self.ComprobarEcuatoriano(nacionalidad=nacionalidad) == True:
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
            return (diferenciaTiempo > int(mayorEdad))                                                                     # CondicionEdad
        else:
            return False

    def EsParaVotoFacultativo(self, mayorEdad, nacionalidad, ocupacion, TerceraEdad, AdolescenteEdad):
        '''Metodo EsParaVotoFacultativo de la clase VotanteSiNo, el cual nos calcula si una persona tendria que serpara voto facultativo o no. 
        
        Parametros
        -----------
        - mayorEdad: De tipo str. \n
                Recibe datos de una base de datos. 
        - nacionalidad: De tipo str. \n
                Recibe datos de una base de datos. 
        - ocupacion: De tipo str. \n
                Recibe datos de una base de datos. 
        - TerceraEdad: De tipo str. \n
                Recibe datos de una base de datos. 
        - AdolescenteEdad: De tipo str. \n
                Recibe datos de una base de datos. 
                
        Retorna.
        -----
        - True: Si cumple que: \n
                self.Mayor18( mayorEdad, nacionalidad) es verdadero (True). \n
                Si esta dentro de las ocupaciones permitidas para voto facultativo. 
                si es de entre (self.Edad >= int(AdolescenteEdad) and self.Edad < int(mayorEdad)) or (self.Edad > int(TerceraEdad)). 
                
        - False: Si no cumple lo anterior mandaria un False o falso. '''
        dato = self.Mayor18( mayorEdad, nacionalidad)
        if dato == True:
            for Ocupaciones in ocupacion:
                if Ocupaciones == self.ocupacion:
                    return True
            if self.discapacidad == True:
                return True
            elif (self.Edad >= int(AdolescenteEdad) and self.Edad < int(mayorEdad)) or (self.Edad > int(TerceraEdad)):                                     #TerceraEdad                   
                return True                                                                                    # AdolescentePermitido
            else:
                return False
        else:
            return False


            

class MiembroDeMesa:
    '''Clase MiembroDeMesa (clase padre), el cual nos ayuda a verifiar si es candidato para ser miembro de mesa. 
    
    Métodos.
    ----
    - def EsVotante(self, Mayor18): El cual verifica si es votante gracias a un parametro. \n
    ..
    - def OcupacionImportante(self,ocupacion, Mayor18, confirmacionOcupacion): El cual nos ayuda a retornaar si es candidato o no. '''
    def EsVotante(self, Mayor18):
        '''Método EsVotante (de la clase MiembroDeMesa), el cual nos ayuda con la verificaion si es votante para ser tomado en cuenta. 
        
        Parámetros. 
        -----
        - Mayor18: El cual para un metodo de otra clase que contenga un True o false. 
        
        Retorna. 
        -----
        - Mayor18 == True: El cual si lo es para True y si no False. '''
        return Mayor18 == True

    def OcupacionImportante(self,ocupacion, Mayor18, confirmacionOcupacion):
        '''Método OcupacionImportante (de la clase MiembroDeMesa), el cual es el metodo principal el cual nos ayuda a comprobar si tiene ocupacion importante.
        
        Parámetros.
        ----
        - ocupacion: Pasa una ocupacion de un ciudadano, pasar principalmente el valor de un atributo de un clase anterior. 
        - Mayor18: Valor que  pasa al metodo EsVotante, el cual pasa true o false. 
        - confirmacionOcupacion: De tipo str. \n
                El cual es la lista de las ocupaciones seleccionadas. 
        
        -------
        Retorna. 
        ----
        - True: Si cumple que: \n
                - self.EsVotante(Mayor18) == True, el cual retornaria la funcion un true o false. 
                - if Ocupaciones == ocupacion; el cual verifica si la ocupacion de una persona esta dentro de una lista de ocupaciones seleccionadas.
                
        - False: Si no cumple las condiciones anteriores tendria que hacer pasar False.  '''
        if self.EsVotante(Mayor18) == True:
            for Ocupaciones in confirmacionOcupacion:
                if Ocupaciones == ocupacion:
                    return True
        return False

class Randon(MiembroDeMesa):
    '''Método Randon (clase hija de MiembroDeMesa), el cual de forma  de random seleccionamos si se poseciona o no en la mesa de voto. 
    
    Metodos. 
    ----
    - def EsSeleccionado(self, ocupacion): El cual nos ayuda a definir de una forma random si es o no es. 
    '''
    def EsSeleccionado(self, ocupacion, Mayor18, confirmacionOcupacion):
        ''' Método EsSeleccionado (matodo de la clase Randon), que nos ayuda a poner un true o false de forma que este decida cual. 
        
        Parametro.
        ----
        - ocupacion: Pasa un dato que es un atributo de una clase
        - Mayor18: De tipo int. \n 
                    Pasa la restricciones de edad, de votante normal. 
        - confirmacionOcupacion: De tipo list. \n
                    Pasa una lista que tiene todo las ocupaciones a considerar. 
        
        Retorna. 
        -----
        - dato: De tipo bools. \n
                El cual lo obtenemos de una lista de True y False y con random obtenemos cualesquiera de los dos. 
                
        Utilizamos.
        -----
        - self.OcupacionImportante(ocupacion): El cual fue heredado de la clase anterior. '''
        if self.OcupacionImportante(ocupacion, Mayor18, confirmacionOcupacion)== True:
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
        self[date(year, 2, 5)] = "La elección de autoridades seccionales en Ecuador 2023" 
        self[date(year, 2, 5-1)] = self[date(year, 2, 5)]
        self[date(year, 2, 5-2)] = self[date(year, 2, 5)]
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


def darDatos(mensaje0, mensaje1, mensaje2, descrip, descrip2, descrip3):
    '''Función darDatos, el cual nos da un mensaje como resultado de lo tenemos. 
    
    Parametros.
    ----------
    - mensaje0: De tipo str. \n
                Da un mensaje que acompañara al resultado.       
    - mensaje1: De tipo str. \n
                Da un mensaje que acompañara al resultado.       
    - mensaje2: De tipo str. \n
                Da un mensaje que acompañara al resultado.       
    - descrip: De tipo  bool. \n
                Los resultados obtenidos son metodos de clases que se encuentran en el fichero Registro_LOGUICA.py.      
    - descrip2: De tipo bool. \n
                Los resultados obtenidos son metodos de clases que se encuentran en el fichero Registro_LOGUICA.py.       
    - descrip3: De tipo bool. \n
                Los resultados obtenidos son metodos de clases que se encuentran en el fichero Registro_LOGUICA.py. 
    
    Retorna. 
    ---------
    - Mensaje, uniendo todos los parametros.      '''
    return(f'''
    EL CIUDADANO:
    · {mensaje0} : ({descrip}), 
    · {mensaje1} : ({descrip2}) 
    · {mensaje2} : ({descrip3}). 
    __________________________________________________ ''')


def PrintDeFechaVotacion(mensajeSI, mensajeNO):
    '''Función PrintDeFechaVotacion, el cual dependiendo de la fecha actual verifica sies la fecha de las votaciones. 
    
    Parametros. 
    -----
    - mensajeSI:  De tipo str.\n 
                El cual pasara un mensaje de confirmación. 
    - mensajeNO: De tipo str. \n 
                El cual para un mensaje de desconfirmación. '''
    fechaActual = datetime.now()
    fechaActual = fechaActual.strftime("%Y-%m-%d")
    votaciones = RestriccionVotacion(fechaActual)
    if votaciones.AplicaRestriccion():
        return(f'''
          {mensajeSI} ''')
    else: 
        return(f'''
        {mensajeNO}''')