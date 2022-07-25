import pymongo

micliente=pymongo.MongoClient("mongodb://localhost:27017/")

mydb=micliente["datosParaProyecto"]

mycol=mydb["CiudadanoSufragantes"]


lista=[
    {"_id": 0000,"nombre": "Michael", "apellido": "Mena","numeroCedula":"1632569874","ocupacion":"Medico","Residencia":"Santo Domingo","Nacionalidad":"Ecuatoriano","Discapacidad":True},
    {"_id": 1000,"nombre": "Francisco", "apellido": "Serrano","numeroCedula":"2365412032","ocupacion":"Comerciante","Residencia":"Nueva Loja","Nacionalidad":"Ecuatoriano","Discapacidad":True},
    {"_id": 2000,"nombre": "Nicolas", "apellido": "Jaramillo","numeroCedula":"1785696523","ocupacion":"Fiscal","Residencia":"Guaranda","Nacionalidad":"Ecuatoriano","Discapacidad":False},
    {"_id": 3000,"nombre": "Elias", "apellido": "Calderon","numeroCedula":"0236532985","ocupacion":"Licenciado ","Residencia":"Ibarra","Nacionalidad":"Ecuatoriano","Discapacidad":False},
    {"_id": 4000,"nombre": "Laura", "apellido": "Tenorio","numeroCedula":"0145632986","ocupacion":"Abogado","Residencia":"Quito","Nacionalidad":"Ecuatoriano","Discapacidad":True},
    {"_id": 5000,"nombre": "Maria", "apellido": "Quiñonez","numeroCedula":"2136549863","ocupacion":"Arquitecta","Residencia":"Manta","Nacionalidad":"Ecuatoriano","Discapacidad":True},
    {"_id": 6000,"nombre": "Anahi", "apellido": "Figueroa","numeroCedula":"1724569865","ocupacion":"Ingeniera Mecanica","Residencia":"El Carmen","Nacionalidad":"Ecuatoriano","Discapacidad":False},
    {"_id": 7000,"nombre": "Camilo", "apellido": "Brito","numeroCedula":"0653265984","ocupacion":"Policia","Residencia":"Quevedo","Nacionalidad":"Ecuatoriano","Discapacidad":False},
    {"_id": 8000,"nombre": "Alex", "apellido": "Constante","numeroCedula":"1758463201","ocupacion":"Piloto","Residencia":"Cuenca","Nacionalidad":"Ecuatoriano","Discapacidad":False},
    {"_id": 9000,"nombre": "Steven", "apellido": "Fonseca","numeroCedula":"1203564890","ocupacion":"Estudiante Superior","Residencia":"Ambato","Nacionalidad":"Ecuatoriano","Discapacidad":True},
    {"_id": 1001,"nombre": "Pablo", "apellido": "Izquierdo","numeroCedula":"0124569856","ocupacion":"Policia","Residencia":"Tena","Nacionalidad":"Ecuatoriano","Discapacidad":False},
    {"_id": 2001,"nombre": "Andres", "apellido": "Astudillo","numeroCedula":"1458796523","ocupacion":"Estudiante Superior","Residencia":"Guayaquill","Nacionalidad":"Ecuatoriano","Discapacidad":True},
]

listaDatos=mycol.insert_many(lista)

print(listaDatos.inserted_ids)

