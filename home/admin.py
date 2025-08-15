from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/order_placement')
def order_placement():
    return "this is the order placement page!"
if __name__ == '__main__':
    app.run(debug=True)