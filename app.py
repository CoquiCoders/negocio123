from flask import Flask, request, render_template
from flask.ext.sqlalchemy import SQLAlchemy

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

@app.route('/')
def index():
  steps = Step.query.all()
  return render_template('index.html', steps=steps)


if __name__ == '__main__':
  app.run()