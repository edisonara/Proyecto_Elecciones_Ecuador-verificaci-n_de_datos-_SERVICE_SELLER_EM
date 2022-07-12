

from datetime import datetime

from bson import decode_file_iter



class Ciudadano:
    def __init__(self, nombre, apellido, numCedula, ocupacion, lugarDeOcupacion, lugarDeRecidencia, nacionalidad, fechaDeNacimiento, discapacidad ):
        self.nombre = nombre
        self.apellido = apellido
        self.numCedula = numCedula
        self.ocupacion = ocupacion
        self.lugarDeOcupacion = lugarDeOcupacion
        self.lugarDeRecidencia = lugarDeRecidencia 
        self.nacionalidad = nacionalidad
        self.fechaDeNacimiento = fechaDeNacimiento
        self.discapacidad = discapacidad 

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

    @property
    def _nacionalidad(self):
        return self.__recidenciaEcuador
    @_nacionalidad.setter
    def _nacionalidad(self, extrangero):
        if extrangero != 'Ecuatoriana':
            pass


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
            else:
                return False
        else:
            return False
            




class MiembroDeMesa():
    @VotanteSiNo.Mayor18
    def EsVotante(self):
        return 
    def OcupacionImportante(self):
        pass
    def TrabajaDondeVive(self):
        pass


class OcupacionMiembroMesa():
    pass

fecha = input('ingrese fecha en el formato año-mes-dia : ')
ciudadano = VotanteSiNo('ewe', 'ewew', 230000, 'feefef', 'efefe', 'eed', 'Ecuatori', fecha, True)
print(type(ciudadano.fechaDeNacimiento))

print(ciudadano.Mayor18())


persona= MiembroDeMesa()




'''def _Docord():
    def RecibirDatoClase(cls):
        class RecibeDelPadre(cls):
            Ciudadano.__init__(self, )
    return RecibirDatoClase'''
'''por definir un decorador '''