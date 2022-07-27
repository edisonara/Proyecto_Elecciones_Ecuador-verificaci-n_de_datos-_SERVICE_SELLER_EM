import random
import pymongo

micliente=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=micliente["DB_CiudadanosEcuadorCNE"]
mycol=mydb["COL_Mensajes_Para_Votantes_CNE"]

listaMensajes = [{'_id':0, 'descripcion': 'Mensaje Votante', 'dato': '¿Usted en las proximas votaciones puede votar? '}, 
{'_id':1, 'descripcion': 'Mensaje Votante_Facultativo', 'dato': '¿Usted es considerado para un voto facultativo? '},
{'_id':2, 'descripcion': 'Mensaje Miembro_Mesa', 'dato': '¿Usted pertenece a miembros de mesas electorales? '},
{'_id':3, 'descripcion': 'Mensaje SI_DIA', 'dato': ' *** Se le comunica al ciudadano/a que estamos en tiempo de elecciones *** \n es tiempo de toque de queda. '},
{'_id':4, 'descripcion': 'Mensaje NO_DIA', 'dato': ' *** Muy pronto se realizara esta actividad, gracias ***'}]


listaCondiciones = [
    {'_id':0,'descripcion': 'ciudadania', 'dato':'Ecuatoriano'},
    {'_id':1,'descripcion':'Mayor_Edad', 'dato':18}, 
    {'_id':2,'descripcion':'Facultativo_Ocupacion', 'dato': ['Militar' ,'Policia']} ,
    {'_id':3,'descripcion':'Tercera_Edad', 'dato':65}, 
    {'_id':4,'descripcion':'Adolescente_Edad', 'dato':16},
    {'_id':5,'descripcion':'OcupacicionParaMesa_1', 'dato': ['Estudiante Superior', 'Ingeniero', 'Contador']},
]

listaDatos=mycol.insert_many(listaMensajes)
# 
print(listaDatos.inserted_ids)




exit()
mydb=micliente["DB_CiudadanosEcuadorCNE"]
mycol=mydb["COL_CiudadanosEcuadorCNE"]




listaNumeros = ['0','1','2','3','4','5','6','7','8','9']
listaNombre = ['Hugo','Lucas','Mario','Marcos','Javier','Bruno','Gonzalo','Gael','Dylan','Adam','Iker','Jaime','Ian','Rafael','Rayan','Biel','Luka','Omar','Mauro','Leonardo','David','Emilio','Felipe','Jacob','Samuel','Kevin','Ezequiel','Jeremias','Jeremy','Gerardo','Amancio','Mike', 'Luis','Martin','Mateo','Andres','Juan','Pablo','Tobias','Franciso','Pedro','Santiago','Matias','Edu','Theo','Victor','Alejandro','Sebastian','Jorge','Joao','Jhon','Paul','Moises','Raul','Daniel','Rodrigo','Fernando','Nicolas','Josue','Axel','Joseph','Fabricio','Andy','Vladimir']
listaApellido=['Alvarez','Andrade','Benitez','Castillo','Castro','Contreras','De Leon','Diaz','Duarte','Espinoza','Fernandez','Flores','Garcia','Gimenez','Gomez','Gonzales','Gutierrez','Hernandez','Jimenez','Lopez','Mamani','Martínez','Mejia','Mora','Morales','Moreno','Muñoz','Perez','Pereira','Pineda','Portillo','Quispe', 'Ramirez','Reyes','Rivas','Rivera','Rodriguez','Rojas','Salazar','Sanchez','Sanchez','Santana','Santos','Silva','Sosa','Soto','Torres','Vargas','Vera','Villalba','Zambrano','Beltran','Bohorquez','Bravo','Urdaneta','Cruz','Govea','Velarde','Rincon','Badillo','Balsa','Arreaga','Arteaga','Baes']
listaOcuapacion=['Militar','Policia','Agente de Transito','Estudiante Superior','Piloto','Ingenier Mecanico','Arquitecto','Abogado','Licenciado','Fiscal','Medico','Estudiante Superior','Estudiante Superior','Ingeniero Industrial','Comerciante','Policia','Estudiante Superior','Estudiante Superior','Pastelero','Bombero','Dentista','Chef','Veteriano','Diseñador','Actor','Enfermero','Agricultor','Panadero','Escultor','Escritor','Barbero','Contador']
listaFechas=['2000-02-15','1999-01-28','2002-06-06','1971-06-25','1988-07-26','1991-09-28','1997-10-0','1993-05-25','1994-06-05','1990-09-08','2001-09-23','1995-08-17','1954-11-15','1960-03-12','1967-02-24','1999-01-27','2004-05-01','2001-10-19','1963-08-22','1969-09-30','1988-07-12','1982-09-15','2004-08-28','1973-06-21','1965-04-13','2004-09-18','2005-09-19','1977-01-16','1984-06-11','1975-03-25','1996-08-16','2000-06-29']
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
    'fecha de nacimiento':random.choice(listaFechas),
    'cedula de identidad':a,
    'ocupacion':random.choice(listaOcuapacion), 
    'residencia ':random.choice(listaProvincias),
    'nacionalidad':random.choice(listaNacionalidad),
    'discapacidad':random.choice(listaDiscapacidad)}
    dicccionario2.update(dicccionario)
    listaA.append(dicccionario)
    contador+= 1





# for diccionarioA in listaA:
#     print(diccionarioA)


# listaDatos=mycol.insert_many(liA)
# 
# print(listaDatos.inserted_ids)

'''Formato----'''
#    Provincia/Ciudad