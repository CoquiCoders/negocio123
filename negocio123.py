from flask import Flask, render_template, redirect, url_for, abort

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin
from flask.ext.login import LoginManager, login_user, UserMixin, login_required, current_user
from wtforms.fields import TextAreaField


app = Flask(__name__)
app.debug = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWXD2D256y2'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dump.db'
db = SQLAlchemy(app)


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
  steps = Step.query.all()
  return render_template('index.html', steps=steps)

@app.route('/<step_number>/')
def step(step_number=None):
  steps = Step.query.all()
  if not step_number:
    return redirect(url_for('index'))
  current_step = Step.query.get(step_number)
  if not current_step:
    abort(404)
  return render_template('step.html', steps=steps, current_step=current_step)

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404

if __name__ == '__main__':
  app.run()