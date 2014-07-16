from negocio123 import db, Step, User, Municipio
import bcrypt

# Start with a fresh db

db.drop_all()
db.create_all()

# Add skeleton steps

steps = []

steps.append(Step(nombre_de_agencia='Departamento de Estado', titulo_corto_de_agencia='Dept Estado', descripcion='Es el primer paso para incorporar tu negocio.', duracion='El tramite se realiza en el dia.', tramite_online=True, tramite_offline=False, costo_de_tramite='150 USD para corporaciones con fines de lucro. 5 USD para corporaciones sin fines de lucro. 10 USD por el tramite de certificado de existencia'))

steps.append(Step(nombre_de_agencia='IRS (Internal Revenue Service)', titulo_corto_de_agencia='IRS', descripcion='Es el segundo paso para incorporar tu negocio. En este paso obtendras el EIN ( Numero de Identificacion de Empleador)', duracion='El tramite se realiza en el dia.', tramite_online=True, tramite_offline=False, costo_de_tramite='El tramite es gratuito'))

steps.append(Step(nombre_de_agencia='Departamento de Hacienda', titulo_corto_de_agencia='Hacienda', descripcion='Es el tercer paso para incorporar tu negocio. En este paso obtendras el registro de comerciante.', duracion='Incluso si se realiza el tramite tramite_online, el certificado en papel demora aproximadamente 7 dias.', tramite_online=True, tramite_offline=False, costo_de_tramite='El tramite es gratuito'))

steps.append(Step(nombre_de_agencia='Municipios', titulo_corto_de_agencia='Municipios', descripcion='Es el cuarto paso para incorporar tu negocio. Recuerda que cada municipio tiene diferentes requisitos.', duracion='Varia de acuerdo al municipio.', tramite_online=False, tramite_offline=True, costo_de_tramite='El tramite varia de acuerdo al tipo de negocio. Entre 25 y 100 USD para la radicacion de la solicitud.'))

steps.append(Step(nombre_de_agencia='Corporacion del Fondo de Seguro', titulo_corto_de_agencia='Corporacion', descripcion='Es el quinto paso para incorporar tu negocio', duracion='Depende', tramite_online=False, tramite_offline=True, costo_de_tramite='Depende'))

steps.append(Step(nombre_de_agencia='Departamento del Trabajo', titulo_corto_de_agencia='Dept Trabajo', descripcion='Es el sexto paso para incorporar tu negocio', duracion='Depende', tramite_online=False, tramite_offline=True, costo_de_tramite='Depende'))

steps.append(Step(nombre_de_agencia='Cuenta Bancaria', titulo_corto_de_agencia='Banco', descripcion='Es el ultimo paso para incorporar tu negocio', duracion='Depende', tramite_online=False, tramite_offline=True, costo_de_tramite='El tramite es gratuito'))

for step in steps:
  db.session.add(step)

# Add a couple of users

email = 'crodriguez@codeforamerica.org'
password = bcrypt.hashpw('coquicoders', bcrypt.gensalt())

db.session.add(User(email=email, password=password))

email = 'clara@codeforamerica.org'
password = bcrypt.hashpw('coquicoders', bcrypt.gensalt())

db.session.add(User(email=email, password=password))

# Add Puerto Rico Municipalities

db.session.add(Municipio(name="Aguadilla"))
db.session.add(Municipio(name="Bayamon"))
db.session.add(Municipio(name="Cabo Rojo"))
db.session.add(Municipio(name="Caguas"))
db.session.add(Municipio(name="San juan"))
db.session.add(Municipio(name="Cidra"))
db.session.add(Municipio(name="Humacao"))
db.session.add(Municipio(name="Ponce"))
db.session.add(Municipio(name="Carolina"))
db.session.add(Municipio(name="Adjuntas"))
db.session.add(Municipio(name="Aguada"))
db.session.add(Municipio(name="Aguas Buenas"))
db.session.add(Municipio(name="Aibonito"))
db.session.add(Municipio(name="Anasco"))
db.session.add(Municipio(name="Arecibo"))
db.session.add(Municipio(name="Arroyo"))
db.session.add(Municipio(name="Barceloneta"))
db.session.add(Municipio(name="Barranquitas"))
db.session.add(Municipio(name="Camuy"))
db.session.add(Municipio(name="Canovanas"))
db.session.add(Municipio(name="Catano"))
db.session.add(Municipio(name="Cayey"))
db.session.add(Municipio(name="Ceiba"))
db.session.add(Municipio(name="Ciales"))
db.session.add(Municipio(name="Coamo"))
db.session.add(Municipio(name="Comerio"))
db.session.add(Municipio(name="Corozal"))
db.session.add(Municipio(name="Culebra"))
db.session.add(Municipio(name="Dorado"))
db.session.add(Municipio(name="Fajardo"))
db.session.add(Municipio(name="Florida"))
db.session.add(Municipio(name="Guanica"))
db.session.add(Municipio(name="Guayama"))
db.session.add(Municipio(name="Guayanilla"))
db.session.add(Municipio(name="Gurabo"))
db.session.add(Municipio(name="Hatillo"))
db.session.add(Municipio(name="Hormigueros"))
db.session.add(Municipio(name="Isabela"))
db.session.add(Municipio(name="Jayuya"))
db.session.add(Municipio(name="Juana Diaz"))
db.session.add(Municipio(name="Juncos"))
db.session.add(Municipio(name="Lajas"))
db.session.add(Municipio(name="Lares"))
db.session.add(Municipio(name="Las Marias"))
db.session.add(Municipio(name="Las Piedras"))
db.session.add(Municipio(name="Loiza"))
db.session.add(Municipio(name="Luquillo"))
db.session.add(Municipio(name="Manati"))
db.session.add(Municipio(name="Maricao"))
db.session.add(Municipio(name="Maunabo"))
db.session.add(Municipio(name="Mayaguez"))
db.session.add(Municipio(name="Moca"))
db.session.add(Municipio(name="Morovis"))
db.session.add(Municipio(name="Naguabo"))
db.session.add(Municipio(name="Naranjito"))
db.session.add(Municipio(name="Orocovis"))
db.session.add(Municipio(name="Patillas"))
db.session.add(Municipio(name="Penuelas"))
db.session.add(Municipio(name="Quebradillas"))
db.session.add(Municipio(name="Rincon"))
db.session.add(Municipio(name="Rio Grande"))
db.session.add(Municipio(name="Sabana Grande"))
db.session.add(Municipio(name="Salinas"))
db.session.add(Municipio(name="San German"))
db.session.add(Municipio(name="San Lorenzo"))
db.session.add(Municipio(name="San Sebastian"))
db.session.add(Municipio(name="Santa Isabel"))
db.session.add(Municipio(name="Toa Alta"))
db.session.add(Municipio(name="Toa Baja"))
db.session.add(Municipio(name="Trujillo Alto"))
db.session.add(Municipio(name="Utuado"))
db.session.add(Municipio(name="Vega Alta"))
db.session.add(Municipio(name="Vega Baja"))
db.session.add(Municipio(name="Vieques"))
db.session.add(Municipio(name="Villalba"))
db.session.add(Municipio(name="Yabucoa"))
db.session.add(Municipio(name="Yauco"))

db.session.commit()
