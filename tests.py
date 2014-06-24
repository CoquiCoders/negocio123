import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from flask import Flask
from negocio123 import app, db, Step
from flask.ext.testing import TestCase

class NoStepsTestCase(TestCase):

  def create_app(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/empty.db'
    return app

  def setUp(self):
    db.create_all()

  def tearDown(self):
    db.drop_all()

  def test_navbar_is_empty(self):
    rv = self.client.get('/')
    assert 'w-nav-link' not in rv.data

  def test_step_view_returns_404(self):
    rv = self.client.get('/1/')
    self.assertEquals(404, rv.status_code)

class StepsTestCase(TestCase):

  def create_app(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/full.db'
    return app

  def setUp(self):
    db.create_all()
    steps = []
    steps.append(Step(full_title='Departamento de Estado', short_title='Dept Estado', description='Es el primer paso para incorporar tu negocio.', time_period='El tramite se realiza en el dia.', online=True, step_cost='150 USD para corporaciones con fines de lucro. 5 USD para corporaciones sin fines de lucro. 10 USD por el tramite de certificado de existencia'))
    steps.append(Step(full_title='IRS (Internal Revenue Service)', short_title='IRS', description='Es el segundo paso para incorporar tu negocio. En este paso obtendras el EIN ( Numero de Identificacion de Empleador)', time_period='El tramite se realiza en el dia.', online=True, step_cost='El tramite es gratuito'))
    for step in steps:
      db.session.add(step)
    db.session.commit()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_navbar_is_not_empty(self):
    rv = self.client.get('/')
    assert 'w-nav-link' in rv.data

  def test_step_view_returns_200(self):
    rv = self.client.get('/1/')
    self.assertEquals(200, rv.status_code)

  def test_step_view_upper_limit_return_404(self):
    rv = self.client.get('/3/')
    self.assertEquals(404, rv.status_code)

class LoginTestCase(TestCase):

  def create_app(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dump.sqlite3'
    return app

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def login(self, email, password):
    return self.client.post('/login', data=dict(
      email=email,
      password=password)
    , follow_redirects=True)

  def logout(self):
    return self.client.get('/logout', follow_redirects=True)

  def test_invalid_login(self):
    rv = self.login('someone@random.com', 'noaccount')
    assert 'Username or Password invalid' in rv.data

  def test_valid_login(self):
    rv = self.login('crodriguez@codeforamerica.org', 'coquicoders')
    assert 'Logged in succesfully' in rv.data

  def test_admin_unaccessible_without_login(self):
    rv = self.client.get('/admin', follow_redirects=True)
    assert 'Step' not in rv.data

  def test_admin_accessible_with_login(self):
    self.login('crodriguez@codeforamerica.org', 'coquicoders')
    rv = self.client.get('/admin', follow_redirects=True)
    assert 'Step' in rv.data

  def test_unauthenticated_admin_should_redirect_to_login(self):
    rv = self.client.get('/admin/')
    self.assertRedirects(rv, '/login?next=%2Fadmin')

  def test_successful_login_redirects_to_next(self):
    rv = self.client.post('/login?next=%2Fadmin', data=dict(
      email='crodriguez@codeforamerica.org',
      password='coquicoders'))
    self.assertRedirects(rv, '/admin')


class MunicipioTestCase(TestCase):

  render_templates = False

  def create_app(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dump.sqlite3'
    return app

  def test_municipio_template_used_on_municipio(self):
    rv = self.client.get('/4/')
    self.assert_template_used('municipios.html')

  def test_municipio_template_not_used_on_other_steps(self):
    rv = self.client.get('/1/')
    self.assert_template_used('step.html')

class NavigationTestCase(TestCase):

  def create_app(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dump.sqlite3'
    return app

  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.close()

  def test_steps_begin(self):
    driver = self.driver
    driver.get('http://localhost:5000/')
    btn = driver.find_element_by_id('comenzar')
    btn.send_keys(Keys.RETURN)
    self.assertEquals('http://localhost:5000/1/', driver.current_url)

if __name__ == '__main__':
  unittest.main()