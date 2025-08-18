from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///specials.db'
db = SQLAlchemy(app)
class TodaySpecial(db.model):
    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullale=False)
    def __repe__(self):
        return f"TodaysSpecial('{self.item_name}', '{self.description}', {self.price})"
 @app.route('/')
 def homepage():
    specials = TodaysSpecial.query.all()
    return render_template('homepage.html', specials=specials)       