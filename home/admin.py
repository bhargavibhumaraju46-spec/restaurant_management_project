from flask import Flask, render_template
from settings import RESTAURANT_PHONE_NUMBER
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('homepage.html', phone_number=RESTAURANT_PHONE_NUMBER)
    if __name__ == '__main__':
        app.run(debug=True)
RESTAURANT_PHONE_NUMBER = "+91 8465883631"        
