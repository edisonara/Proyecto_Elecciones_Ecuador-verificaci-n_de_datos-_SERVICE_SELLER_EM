from tkinter import *
from tkinter import ttk

class MRU:
    velocidad = 0.0
    distancia = 0.0
    tiempo = 0.0
    def __init__(self, velocidad, distancia, tiempo):
        self.velocidad = velocidad
        self.distancia = distancia
        self.tiempo = tiempo
    def procesar(self):
        if self.velocidad == 0.0:
            self.velocidad = self.distancia / self.tiempo
    
        elif self.distancia == 0.0:
            self.distancia = self.velocidad * self.tiempo

        elif self.tiempo == 0.0:
            self.tiempo = self.distancia / self.velocidad

def calcularDistancia():
    velocidad1=float(input("\nIngrese la velocidad: "))
    tiempo1=float(input("\nIngrese el tiempo: "))
    distancia1=float(input("\nIngrese la distacia: "))
    particula = MRU(velocidad1,distancia1,tiempo1)
    particula.procesar()
    print(particula.distancia)

def calcularTiempo():
    velocidad1=float(input("\nIngrese la velocidad: "))
    tiempo1=float(input("\nIngrese el tiempo: "))
    distancia1=float(input("\nIngrese la distacia: "))
    particula = MRU(velocidad1,distancia1,tiempo1)
    particula.procesar()
    print(particula.tiempo)

def calcularVelocidad():
    velocidad1=float(input("\nIngrese la velocidad: "))
    tiempo1=float(input("\nIngrese el tiempo: "))
    distancia1=float(input("\nIngrese la distacia: "))
    particula = MRU(velocidad1,distancia1,tiempo1)
    particula.procesar()
    print(particula.velocidad)

def distancia1():
    opcion3=int(input("***Menú de conversión de distacia***\n 1. Kilometros a metros \n 2. Millas a metros \n 3. Pies a metros\n 0. Salir\n" "Ingrese la opción que desea: "))
    while opcion3 !=0:
        if opcion3==1:
            print("------------------------")
            kilometros=int(input("\n Ingrese la cantidad de kilómetros a convertir: "))
            metros=kilometros*1000
            print(kilometros, " kilómetros equivalen a ", metros, " metros")
        elif opcion3==2:
            print("------------------------")
            millas=int(input("\nIngrese la cantidad de millas convertir: "))
            metros= millas*1609.34
            print(millas, " millas equivalen a ", metros, " metros")
        elif opcion3==3:
            print("------------------------")
            pies=int(input("\nIngrese la cantidad de pies a convertir: "))
            metros= pies *0.3048
            print(pies, " pies equivalen a ", metros, " metros")
        else:
            print("\nIngrese una opción válida.")
        opcion3=int(input("***Menú de conversión de distacia***\n 1. Kilometros a metros \n 2. Millas a metros \n 3. Pies a metros\n 0. Salir\n" "Ingrese la opción que desea: "))
def tiempo1():
    opcion=int(input("***Menú de conversión de tiempo***\n 1. Horas a segundos \n 2. Minutos a segundos \n 3. Días a segundos \n 0. Salir\n" "Ingrese la opción que desea: "))
    while opcion !=0:
        if opcion==1:
            print("------------------------")
            horas=int(input("\nIngrese la cantidad de horas a convertir: "))
            segundos=horas*3600
            print(horas, " horas equivalen a ", segundos, "segundos")
        elif opcion==2:
            print("------------------------")
            minutos=int(input("\nIngrese la cantidad de minutos a convertir: "))
            segundos= minutos*60
            print(minutos, " minutos equivalen a ", segundos, " segundos")
        elif opcion==3:
            print("------------------------")
            dias=int(input("\nIngrese la cantidad de dias a convertir: "))
            segundos= dias * 86400
            print(dias, " días equivalen a ", segundos, " segundos")
        else:
            print("\nIngrese una opción válida.")
        opcion=int(input("***Menú***\n 1. Pulgadas a milímetros \n 2. yardas a metros \n 3. Millas a kilómetros \n 0. Salir\n" "Ingrese la opci+on que desea: "))
def velocidad1():
    while True:
        opcion=int(input("***Menú de conversión de velocidades***\n 1. Km/h a m/s \n 2. millas/h a m/s \n 3. pies/h a m/s \n 0. Salir\n" "Ingrese la opción que desea: "))
        if opcion==1:
            print("------------------------")
            kmm=int(input("\nIngrese la cantidad de km/s a convertir: "))
            mseg=kmm*0.277778
            print(kmm, " Km/h equivalen a ", mseg, " m/s")
        elif opcion==2:
            print("------------------------")
            millah=int(input("\nIngrese la cantidad de millas/h a convertir: "))
            mseg=millah*2.23694
            print(millah, " Km/h equivalen a ", mseg, " m/s")
        elif opcion==3:
            print("------------------------")
            piesh=int(input("\nIngrese la cantidad de pies/h a convertir: "))
            mseg=piesh*11811
            print(piesh, " Km/h equivalen a ", mseg, " m/s")
        elif opcion==0:
            break
        else:
            print("\nIngrese una opción válida.")
        







if __name__=="__main__":
    root =Tk()
    root.title('Verificación de Ciudadanos.')
    root.resizable(1,1)
    root.iconbitmap(r'C:\Users\eaar2\POO___unidad 2\programa2\programming_117944.ico')
    dato1= StringVar()
    numeroResult = StringVar()
    frame = Frame(root ,width=500, height= 500)
    frame.pack()
    label = Label(frame, text='bienvenido edison')
    label.grid(row=0, column=0)
    nombre = Entry(frame, justify='center',textvariable=dato1)
    nombre.focus()
    nombre.grid(row=1, column=0)
    ttk.Button(frame ,text='Buscar').grid(row=3, columnspan=2, sticky=W + E)
    nombre = Entry(frame, justify='center',textvariable=numeroResult)
    nombre.focus()
    nombre.grid(row=1, column=1)
    root.mainloop()
