from flask import Flask, render_template, redirect, url_for

from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from wtforms.fields import TextAreaField


app = Flask(__name__)
app.debug = True


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

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
    return '<Step %r>' % self.title

class MyView(ModelView):
  form_overrides = dict(type_of_process=TextAreaField, papers_to_fill=TextAreaField, attention=TextAreaField,)
  edit_template = 'edit.html'

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
  return render_template('step.html', steps=steps, current_step=current_step)


if __name__ == '__main__':
  app.run()