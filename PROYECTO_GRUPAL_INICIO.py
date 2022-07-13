
from datetime import datetime, date
import random
import holidays

class Ciudadano:
    def __init__(self, nombre, apellido, numCedula, ocupacion, nacionalidad, fechaDeNacimiento, discapacidad ):
        self.nombre = nombre  # nn nn
        self.apellido = apellido# aa aa
        self.numCedula = numCedula # str ####################
        self.ocupacion = ocupacion  # ocupacion 
        self.lugarDeRecidencia =  self.numCedula[:3]
        self.nacionalidad = nacionalidad #  # Ecuatoriana
        self.fechaDeNacimiento = fechaDeNacimiento  # NNNN-NN-NN
        self.discapacidad = discapacidad  # true - false

    @property
    def fechaDeNacimiento(self):
        return self._edad
    @fechaDeNacimiento.setter
    def fechaDeNacimiento(self, parametro):
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
            if len(parametro) != 10:
                raise ValueError
            datetime.strptime(parametro, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                'La fecha debe tener el siguiente formato: AAAA-MM-DD (por ejemplo: 2021-04-02)') from None
        self._edad= parametro


class VotanteSiNo(Ciudadano):

    def ComprobarEcuatoriano(self, ):
        if self.nacionalidad == 'Ecuatoriano':
            return True
        return False

    
    def Mayor18(self):
        '''condicion principal '''
        
        if self.ComprobarEcuatoriano() == True:
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
            return (diferenciaTiempo > 18)
        else:
            return False

    def EsParaVotoFacultativo(self):
        '''condicion principal secundaria '''
        dato = self.Mayor18()
        if dato == True:
            if self.discapacidad == True:
                return True
            elif self.ocupacion[0:7] == 'Militar':
                return True
            elif self.ocupacion[0:7] == 'Policía':
                return True
            #elif self.lugarDeRecidencia[0: 7] != 'Ecuador':
            #    return True

            elif (self.Edad > 16 and self.Edad < 18) or (self.Edad > 65):
                return True
            else:
                return False
        else:
            return False
            

class MiembroDeMesa:
    
    def EsVotante(self, Mayor18):
        return Mayor18 == True
    def OcupacionImportante(self,ocupacion, Mayor18):
        if self.EsVotante(Mayor18) == True:
            if ocupacion[: 19] == 'Estudiante-Superior':
                return True
            elif ocupacion[:15] == 'Empleado-Publico':
                return True
            elif ocupacion[:15] == 'Empleado-Privado':
                return True

class Randon(MiembroDeMesa):
    def EsSeleccionado(self, ocupacion):
        if self.OcupacionImportante(ocupacion)== True:
            ListaBool = [True, False]
            dato = random.choice(ListaBool)
            return dato

def pedirDatos(descripcion):
    dato = input(f'  > Ingrese del cuidadano, {descripcion} : ')
    return dato

def darDatos(descrip, descrip2, descrip3):
    print(f'''
    El ciudadano puede votar ({descrip}), 
    tiene voto facultativo ({descrip2}) 
    y pertenece a miembros de mesa ({descrip3}).  ''')



#  ________________________ MANEJO DE HOLIDAYS DE FECHA DE ACCESO _______________________________________    
class FechasVotaciones(holidays.HolidayBase):
    
    #provincia=['EC-SD'] 
    def __init__(self ,**lista): 
        '''declaramos las funciones necesarias para tener nuestrosferiados a la mano'''
        self.country = 'ECU'
        
        holidays.HolidayBase.__init__(self, **lista)

    def _populate(self, year=2023):
        self[date(2023, 2, 5)] = "La elección de autoridades seccionales en Ecuador 2023" 
        self[date(2023, 2, 5-1)] = self[date(2023, 2, 5)]
        self[date(2023, 2, 5-2)] = self[date(2023, 2, 5)]
####_____________________________________________________________________________________________________
class RestriccionVotacion:
   
    def __init__ (self, dia):
       
        self.dia= dia
        

    @property 
    def dia(self):
       
        return self._dia 
    @dia.setter 
    def dia(self, numValor): 
        
        try:
            if len(numValor)!=10:
                raise ValueError 
            datetime.strptime(numValor, '%Y-%m-%d') 
        except ValueError: 
            raise ValueError('error ingrese en formato AAAA-MM_DD ;)') from None
        self._dia=numValor

    def __EsVotacion(self, date):
        #if enLinea: # condicion si es enLinea tru
        #else: # nos conecta con los feriados personalizados o creados 
        FiestasApi=FechasVotaciones(prov='EC-SD') # instencia o crea un objeto de la clases feriadoTschilas con un parametro el cual es la cuadad de Santo Domingo
        return date in FiestasApi # retorna true o false dependiendo si la fecha ingresada 'date' se en cunetra en los feriados creados. 
    
    def AplicaRestriccion(self): # funcion que decide definitivamente
        if self.__EsVotacion(self.dia):
            return True   
        return False 


def PrintDeFechaVotacion():
    fechaActual = datetime.now()
    fechaActual = fechaActual.strftime("%Y-%m-%d")
    #fechaActual= datetime.strptime(fechaActual, "%Y-%m-%d")
    votaciones = RestriccionVotacion(fechaActual)
    if votaciones.AplicaRestriccion():
        print('''
        **** Se le comunica al ciudadano/a que en los tres días previos a las elecciones  *******
        ****    no puede ingerir bebidas alcohólicas                                      *******
        ****    y/o sustancias estupefacientes                                            ******* ''')
    else: 
        print('''
         *****  Muy pronto se realizara esta actividad, gracias *****''')

def Presentacion():
    print ('''
----                  UNIVERSIDAD DE LAS FUERZAS ARMADAS ESPE
----                      S E R V E R _ S E L L E R  B M                            --------
----    PROGRAMA PARA SABER INFORMACIÓN SOBRE LAS BOTACIONES QUE SERAN EN EL 2023
----         REALIZADO POR EDISON ARAMBULO Y MATEO BELTRAN
--------------------------------------------------------------------------------------------- ''')

if __name__=='__main__':
    '''
       (nombre, apellido, numCedula, ocupacion, nacionalidad, fechaDeNacimiento, discapacidad)'''
    Presentacion()
    nombre = pedirDatos('nombre, con formato (NN NN) ')
    apellido = pedirDatos('apellido, con formato (AA AA)')
    numCedula = pedirDatos('numero, de cedula con formato (##########)')
    ocupacion = pedirDatos('ocupacion, con formato ejemplo (Estudiante-Superior)')
    nacionalidad = pedirDatos('nacionalidad, con formato ejemplo(Ecuatoriano)')
    fecha = pedirDatos('fecha de nacimiento, en el formato año-mes-dia : ')
    discapacidad = bool(pedirDatos('si tiene discapacidad con (True o False)'))
    ciudadano = VotanteSiNo(nombre, apellido, numCedula, ocupacion, nacionalidad, fecha, discapacidad)
    ciudadanoMas = MiembroDeMesa()
    darDatos(ciudadano.Mayor18(), ciudadano.EsParaVotoFacultativo(), ciudadanoMas.OcupacionImportante(ciudadano.ocupacion, ciudadano.Mayor18()))
    PrintDeFechaVotacion()

