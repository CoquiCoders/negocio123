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
    rv = self.app.get('/3/')
    self.assertEquals(404, rv.status_code)

class LoginTestCase(unittest.TestCase):

  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dump.sqlite3'
    db.create_all()
    self.app = app.test_client()

  def tearDown(self):
    pass

  def login(self, email, password):
    return self.app.post('/login', data=dict(
      email=email,
      password=password)
    , follow_redirects=True)

  def logout(self):
    self.app.get('/logout', follow_redirects=True)

  def test_invalid_login(self):
    rv = self.login('someone@random.com', 'noaccount')
    assert 'Username or Password invalid' in rv.data

  def test_valid_login(self):
    rv = self.login('christian.etpr10@gmail.com', 'sbfamily1')
    assert 'Logged in succesfully' in rv.data

  def test_steps_admin_unaccessible_without_login(self):
    rv = self.app.get('/admin', follow_redirects=True)
    assert 'Step' not in rv.data
    assert 'User' not in rv.data

  def test_steps_admin_accessible_with_login(self):
    self.login('christian.etpr10@gmail.com', 'sbfamily1')
    rv = self.app.get('/admin', follow_redirects=True)
    assert 'Step' in rv.data
    assert 'User' in rv.data


if __name__ == '__main__':
  unittest.main()