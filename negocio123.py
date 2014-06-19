from flask import Flask, render_template, redirect, url_for, abort, request, flash

from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin

from flask.ext.login import LoginManager, login_user, UserMixin, login_required, current_user, logout_user
import bcrypt

from flask.ext.sqlalchemy import SQLAlchemy
from wtforms.fields import TextAreaField


app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWXD2D256y2'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dump.sqlite3'
db = SQLAlchemy(app)

#
# Flask-login
#

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))
login_manager.login_view = 'login'

# 
# Database
# 
class Step(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  full_title = db.Column(db.String(80), unique=True)
  short_title = db.Column(db.String(16), unique=True)
  description = db.Column(db.String(140))
  time_period = db.Column(db.String(140))
  online = db.Column(db.Boolean)
  step_cost = db.Column(db.String)
  type_of_process = db.Column(db.String)
  papers_to_fill = db.Column(db.String)
  attention = db.Column(db.String)
  step_url = db.Column(db.String(80))

  def __repr__(self):
    return '<Step: %r>' % self.title

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(50), unique=True, index=True)
  password = db.Column(db.String)

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return unicode(self.id)

  def __repr__(self):
    return "<User %r>" % self.email

# 
# Flask-admin
# 
class MyView(ModelView):  
  form_overrides = dict(type_of_process=TextAreaField, papers_to_fill=TextAreaField, attention=TextAreaField,)
  edit_template = 'admin/edit.html'
  list_template = 'admin/list.html'
  create_template = 'admin/create.html'


admin = Admin(app, name='Negocio123')
admin.add_view(MyView(Step, db.session))

@app.route('/')
def index():
  logout_user()
  steps = Step.query.all()
  print current_user
  return render_template('index.html', steps=steps)

@app.route('/<step_number>/')
@login_required
def step(step_number=None):
  steps = Step.query.all()
  if not step_number:
    return redirect(url_for('index'))
  current_step = Step.query.get(step_number)
  if not current_step:
    abort(404)
  return render_template('step.html', steps=steps, current_step=current_step)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return render_template('login.html')
  email = request.form['email']
  password = request.form['password']
  registered_user = User.query.filter_by(email=email).first()
  if registered_user is None:
    flash('Username or Password invalid', 'error')
    return redirect(url_for('login'))
  elif bcrypt.hashpw(str(password), str(registered_user.password)) != str(registered_user.password):
    flash('Password wrong', 'error')
    return redirect(url_for('login'))
  login_user(registered_user)
  flash('Logged in succesfully')
  return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404

if __name__ == '__main__':
  app.run()