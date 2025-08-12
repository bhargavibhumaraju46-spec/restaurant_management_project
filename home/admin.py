class Restaurant:
    def__init__(self, phone_number):
        self.phone_number = phone_number
restaurant = Restaurant("+91 8465883631")
from flask import Flask, render_template
app = Flask(__name__)
restaurant = Restaurant("+91 8465883631")
@app.route('/')
def homepage():
    return render_template('homepage.html', restaurant=restaurant)
if__name__ == '__main__':
    app.run(debug=True)            

