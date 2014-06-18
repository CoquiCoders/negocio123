import os
import unittest
import tempfile
from negocio123 import app, db, Step

class NoStepsTestCase(unittest.TestCase):

  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/empty.db'
    db.create_all()
    self.app = app.test_client()

  def tearDown(self):
    db.drop_all()

  def test_navbar_is_empty(self):
    rv = self.app.get('/')
    assert 'w-nav-link' not in rv.data

  def test_step_view_returns_404(self):
    rv = self.app.get('/1/')
    self.assertEquals(404, rv.status_code)

class StepsTestCase(unittest.TestCase):

  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/full.db'
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
    db.session.commit()

    self.app = app.test_client()

  def tearDown(self):
    db.drop_all()

  def test_navbar_is_not_empty(self):
    rv = self.app.get('/')
    assert 'w-nav-link' in rv.data

  def test_step_view_returns_200(self):
    rv = self.app.get('/1/')
    self.assertEquals(200, rv.status_code)

  def test_step_view_upper_limit_return_404(self):
    rv = self.app.get('/8/')
    self.assertEquals(404, rv.status_code)

if __name__ == '__main__':
  unittest.main()