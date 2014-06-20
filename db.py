from negocio123 import db, Step, User
import bcrypt

db.drop_all()
db.create_all()

steps = []

steps.append(Step(full_title='Departamento de Estado', short_title='Dept Estado', description='Es el primer paso para incorporar tu negocio.', time_period='El tramite se realiza en el dia.', online=True, step_cost='150 USD para corporaciones con fines de lucro. 5 USD para corporaciones sin fines de lucro. 10 USD por el tramite de certificado de existencia'))

steps.append(Step(full_title='IRS (Internal Revenue Service)', short_title='IRS', description='Es el segundo paso para incorporar tu negocio. En este paso obtendras el EIN ( Numero de Identificacion de Empleador)', time_period='El tramite se realiza en el dia.', online=True, step_cost='El tramite es gratuito'))

steps.append(Step(full_title='Departamento de Hacienda', short_title='Hacienda', description='Es el tercer paso para incorporar tu negocio. En este paso obtendras el registro de comerciante.', time_period='Incluso si se realiza el tramite online, el certificado en papel demora aproximadamente 7 dias.', online=True, step_cost='El tramite es gratuito'))

steps.append(Step(full_title='Municipios', short_title='Municipios', description='Es el cuarto paso para incorporar tu negocio. Recuerda que cada municipio tiene diferentes requisitos.', time_period='Varia de acuerdo al municipio.', online=False, step_cost='El tramite varia de acuerdo al tipo de negocio. Entre 25 y 100 USD para la radicacion de la solicitud.'))

steps.append(Step(full_title='Corporacion del Fondo de Seguro', short_title='Corporacion', description='Es el quinto paso para incorporar tu negocio', time_period='Depende', online=False, step_cost='Depende'))

steps.append(Step(full_title='Departamento del Trabajo', short_title='Dept Trabajo', description='Es el sexto paso para incorporar tu negocio', time_period='Depende', online=False, step_cost='Depende'))

steps.append(Step(full_title='Cuenta Bancaria', short_title='Banco', description='Es el ultimo paso para incorporar tu negocio', time_period='Depende', online=False, step_cost='El tramite es gratuito'))

for step in steps:
  db.session.add(step)

email = 'christian.etpr10@gmail.com'
password = bcrypt.hashpw('sbfamily1', bcrypt.gensalt())

db.session.add(User(email=email, password=password))

db.session.commit()
