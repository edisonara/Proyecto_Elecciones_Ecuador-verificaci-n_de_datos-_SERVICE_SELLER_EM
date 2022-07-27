from datetime import datetime, date
import random
import holidays

class Ciudadano:
    def __init__(self, nombre, apellido, numCedula, ocupacion, recidencia, nacionalidad, fechaDeNacimiento, discapacidad ):
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
        return self._edad

    @fechaDeNacimiento.setter
    def fechaDeNacimiento(self, parametro):
        try:
            if len(parametro) != 10:
                raise ValueError
            datetime.strptime(parametro, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._edad= parametro

class VotanteSiNo(Ciudadano):
    def ComprobarEcuatoriano(self , nacionalidad):
        if self.nacionalidad == nacionalidad:                                                                 # CondicionCIudadano
            return True
        return False
    
    def Mayor18(self, mayorEdad, nacionalidad):
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
        dato = self.Mayor18( mayorEdad, nacionalidad)
        if dato == True:
            #ocupacion = ocupacion['dato']
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
    def EsVotante(self, Mayor18):
        return Mayor18 == True

    def OcupacionImportante(self,ocupacion, Mayor18, confirmacionOcupacion):
        if self.EsVotante(Mayor18) == True:
            for Ocupaciones in confirmacionOcupacion:
                if Ocupaciones == ocupacion:
                    return True
        return False

class Randon(MiembroDeMesa):
    def EsSeleccionado(self, ocupacion, Mayor18, confirmacionOcupacion):
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
    return(f'''
    EL CIUDADANO:
    · {mensaje0} : ({descrip}), 
    · {mensaje1} : ({descrip2}) 
    · {mensaje2} : ({descrip3}). 
    __________________________________________________ ''')


def PrintDeFechaVotacion(mensajeSI, mensajeNO):
    '''Mensaje tiene que sere cambiables. '''
    fechaActual = datetime.now()
    fechaActual = fechaActual.strftime("%Y-%m-%d")
    votaciones = RestriccionVotacion(fechaActual)
    if votaciones.AplicaRestriccion():
        return(f'''
          {mensajeSI} ''')
    else: 
        return(f'''
        {mensajeNO}''')