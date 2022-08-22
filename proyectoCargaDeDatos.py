import random
import pymongo

micliente=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=micliente["Arambulo_Beltran_DB"]
mycol=mydb["COL_Productos"]
mycol=mydb["COL_Compras"]
#mycol = mydb['COL_Mensajes_Para_Votantes_CNE']
#mycol = mydb['COL_Condiciones_Para_Votantes_CNE']



datosExamen = [{'_id': 0, 'nombre':'musicaCD', 'precio': 23.3,  'tipo': 'entretenimiento'}, 
{'_id': 1, 'nombe':'videoGames', 'precio': 10, 'tipo': 'entretenimiento'}, 
{'_id': 2, 'nombe':'PalaDeJardin', 'precio': 12,  'tipo': 'hogar'},
{'_id': 3, 'nombe':'ComputerGame', 'precio': 5,  'tipo': 'entretenimiento'},
{'_id': 4, 'nombe':'VideoDVD', 'precio': 15, 'tipo': 'entretenimiento'},
{'_id': 5, 'nombe':'HouseholdItem', 'precio': 23, 'tipo': 'hogar'},
{'_id': 6, 'nombe':'GardenItem', 'precio': 23.5, 'tipo': 'entretenimiento'},
{'_id': 7, 'nombe':'Book', 'precio': 20,  'tipo': 'tangible'},
]


listaDatos=mycol.insert_many(datosExamen)
# 
print(listaDatos.inserted_ids)

listaMensajes = [{'_id':0, 'descripcion': 'Mensaje_Votante', 'dato': '¿Usted en las proximas votaciones puede votar? '}, 
{'_id':1, 'descripcion': 'Mensaje_Votante_Facultativo', 'dato': '¿Usted es considerado para un voto facultativo? '},
{'_id':2, 'descripcion': 'Mensaje_Miembro_Mesa', 'dato': '¿Usted pertenece a miembros de mesas electorales? '},
{'_id':3, 'descripcion': 'Mensaje_SI_DIA', 'dato': ' * Se le comunica al ciudadano/a que estamos en tiempo de elecciones * \n es tiempo de toque de queda. '},
{'_id':4, 'descripcion': 'Mensaje_NO_DIA', 'dato': '  * Muy pronto se realizara esta actividad, gracias *'},
{'_id':5, 'descripcion': 'lugar_votacion', 'dato': 'Su lugar de votación es: '}]

listaCondiciones = [
    {'_id':6,'descripcion': 'ciudadania', 'dato':'Ecuatoriano'},
    {'_id':7,'descripcion':'Mayor_Edad', 'dato':18}, 
    {'_id':8,'descripcion':'Facultativo_Ocupacion', 'dato': ['Militar' ,'Policia']} ,
    {'_id':9,'descripcion':'Tercera_Edad', 'dato':65}, 
    {'_id':10,'descripcion':'Adolescente_Edad', 'dato':16},
    {'_id':11,'descripcion':'OcupacicionParaMesa_1', 'dato': ['Estudiante Superior', 'Ingeniero', 'Contador']},
]

dicccionario=[{'_id' :0, 'nombre':'Dylan Moises' , 'apellido':'Torres Gimenez','fecha de nacimiento':"1990-01-28",'cedula de identidad':'23000000001','ocupacion':'Policia', 'residencia ':'Cañar/Azogues','nacionalidad':'Ecuatoriano','discapacidad':True}]

exit()
listaNumeros = ['0','1','2','3','4','5','6','7','8','9']
listaNombre = ['Hugo','Lucas','Mario','Marcos','Javier','Bruno','Gonzalo','Gael','Dylan','Adam','Iker','Jaime','Ian','Rafael','Rayan','Biel','Luka','Omar','Mauro','Leonardo','David','Emilio','Felipe','Jacob','Samuel','Kevin','Ezequiel','Jeremias','Jeremy','Gerardo','Amancio','Mike', 'Luis','Martin','Mateo','Andres','Juan','Pablo','Tobias','Franciso','Pedro','Santiago','Matias','Edu','Theo','Victor','Alejandro','Sebastian','Jorge','Joao','Jhon','Paul','Moises','Raul','Daniel','Rodrigo','Fernando','Nicolas','Josue','Axel','Joseph','Fabricio','Andy','Vladimir']
listaApellido=['Alvarez','Andrade','Benitez','Castillo','Castro','Contreras','De Leon','Diaz','Duarte','Espinoza','Fernandez','Flores','Garcia','Gimenez','Gomez','Gonzales','Gutierrez','Hernandez','Jimenez','Lopez','Mamani','Martínez','Mejia','Mora','Morales','Moreno','Muñoz','Perez','Pereira','Pineda','Portillo','Quispe', 'Ramirez','Reyes','Rivas','Rivera','Rodriguez','Rojas','Salazar','Sanchez','Sanchez','Santana','Santos','Silva','Sosa','Soto','Torres','Vargas','Vera','Villalba','Zambrano','Beltran','Bohorquez','Bravo','Urdaneta','Cruz','Govea','Velarde','Rincon','Badillo','Balsa','Arreaga','Arteaga','Baes']
listaOcuapacion=['Militar','Policia','Agente de Transito','Estudiante Superior','Piloto','Ingenier Mecanico','Arquitecto','Abogado','Licenciado','Fiscal','Medico','Estudiante Superior','Estudiante Superior','Ingeniero Industrial','Comerciante','Policia','Estudiante Superior','Estudiante Superior','Pastelero','Bombero','Dentista','Chef','Veteriano','Diseñador','Actor','Enfermero','Agricultor','Panadero','Escultor','Escritor','Barbero','Contador']
listaFechas=['2000-02-15','1999-01-28','2002-06-06','1971-06-25','1988-07-26','1991-09-28','1997-10-01','1993-05-25','1994-06-05','1990-09-08','2001-09-23','1995-08-17','1954-11-15','1960-03-12','1967-02-24','1999-01-27','2004-05-01','2001-10-19','1963-08-22','1969-09-30','1988-07-12','1982-09-15','2004-08-28','1973-06-21','1965-04-13','2004-09-18','2005-09-19','1977-01-16','1984-06-11','1975-03-25','1996-08-16','2000-06-29']
listaResidencia=['Azogues','Latacunga','La Libertad','Tulcan','Milagro','Duran','Esmeraldas','La Troncal','Ventanas','Babahoyo','Naranjal','Ibarra','Salcedo','Ambato','Riobamba','Baños','Turi','Tarqui','Sangolqui','Loja','Nueva Loja','Manta','Portoviejo','Quevedo','Guayaquill','Quito','Machala','Cuenca','Guaranda','El Carmen','Chone','Santo Domingo']
listaProvincias=['Azuay/Cuenca','Bolivar/Guaranda','Cañar/Azogues','Chimborazo/Riobamba','Cotopaxi/Latacunga','El Oro/Arenillas','Esmeraldas/Esmeraldas','Galapagos/San Cristóbal','Guayas/Guayaquil','Imbabura/Ibarra','Loja/Valle de Loja','Los Rios/Babahoyo','Manabi/Manta','Morona Santiago/Gualaquiza','Napo/Quijos','Orellana/Francisco de Orellana','Pastaza/Puyo','Pichincha/Quito','Santa Elena/Salinas','Santo Domingo de los Tsáchilas/Santo Domingo','Sucumbios/Nueva Loja','Tungurahua/Ambato','Zamora Chinchipe/El Pangui']
listaNacionalidad=['Ecuatoriano']
Provincias = ['Manabí' , 'Guayas']
listaDiscapacidad=[True,False]
dicccionario2= {}
listaA= []
listaN = []
for a in range (0,400000):
    listaN.append((random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)+random.choice(listaNumeros)) )
contador = 0
for a in listaN:
    dicccionario = {'_id':contador, 
    'nombre': (random.choice(listaNombre)+' '+random.choice(listaNombre)), 
    'apellido':(random.choice(listaApellido)+ ' '+ random.choice(listaApellido)),
    'fecha_de_nacimiento':random.choice(listaFechas),
    'cedula_de_identidad':a,
    'ocupacion':random.choice(listaOcuapacion), 
    'residencia':random.choice(listaProvincias),
    'nacionalidad':random.choice(listaNacionalidad),
    'discapacidad':random.choice(listaDiscapacidad)}
    dicccionario2.update(dicccionario)
    listaA.append(dicccionario)
    contador+= 1





# for diccionarioA in listaA:
#     print(diccionarioA)

listaDatos=mycol.insert_many(listaA)

print(listaDatos.inserted_ids)

#listaDatos=listaA
# 
#for dato in listaDatos:
#    print(dato)

'''Formato----'''
#    Provincia/Ciudad