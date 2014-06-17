from flask import Flask, render_template, redirect, url_for

from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

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
  step_cost = db.Column(db.String(140))

  def __repr__(self):
    return '<Step %r>' % self.title

admin = Admin(app, name='Negocio123')
admin.add_view(ModelView(Step, db.session))

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