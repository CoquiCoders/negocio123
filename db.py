from app import db, Step

db.drop_all()
db.create_all()

steps = []

steps.append(Step(full_title='Departamento de Estado', short_title='Dept Estado', description='Es el primer paso para incorporar tu negocio'))
steps.append(Step(full_title='IRS (Internal Revenue Service)', short_title='IRS', description='Es el segundo paso para incorporar tu negocio'))
steps.append(Step(full_title='Departamento de Hacienda', short_title='Hacienda', description='Es el tercer paso para incorporar tu negocio'))
steps.append(Step(full_title='Municipios', short_title='municipios', description='Es el cuarto paso para incorporar tu negocio'))
steps.append(Step(full_title='Corporacion del Fondo de Seguro', short_title='Corporacion', description='Es el quinto paso para incorporar tu negocio'))
steps.append(Step(full_title='Departamento del Trabajo', short_title='Dept Trabajo', description='Es el sexto paso para incorporar tu negocio'))
steps.append(Step(full_title='Cuenta Bancaria', short_title='Banco', description='Es el ultimo paso para incorporar tu negocio'))

for step in steps:
  db.session.add(step)

db.session.commit()
