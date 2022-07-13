
from datetime import datetime
import random

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

    def ComprobarEcuatoriano(self):
        return (self.nacionalidad == 'Ecuatoriano')

    
    def Mayor18(self):
        '''condicion principal '''
        dato = self.ComprobarEcuatoriano()
        if dato == True:
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
    def EsVotante(self):
        datoBooleano = VotanteSiNo.Mayor18(self)
        return datoBooleano == True
    def OcupacionImportante(self,ocupacion):
        if self.EsVotante() == True:
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

if __name__=='__main__':
    '''
       (nombre, apellido, numCedula, ocupacion, nacionalidad, fechaDeNacimiento, discapacidad)'''
    nombre = pedirDatos('nombre, con formato (NN NN) ')
    apellido = pedirDatos('apellido, con formato (AA AA)')
    numCedula = pedirDatos('numero, de cedula con formato (##########)')
    ocupacion = pedirDatos('ocupacion, con formato ejemplo (Estudiante-Superior)')
    nacionalidad = pedirDatos('nacionalidad, con formato ejemplo(Ecuatoriano)')
    fecha = pedirDatos('fecha de nacimiento, en el formato año-mes-dia : ')
    discapacidad = bool(pedirDatos('si tiene discapacidad con (True o False)'))
    ciudadano = VotanteSiNo(nombre, apellido, numCedula, ocupacion, nacionalidad, fecha, discapacidad)
    ciudadanoMas = Randon()
    darDatos(ciudadano.Mayor18(), ciudadano.EsParaVotoFacultativo(), ciudadanoMas.EsSeleccionado(ciudadano.ocupacion))
