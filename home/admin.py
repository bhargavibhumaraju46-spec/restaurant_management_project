from flask import Flask, session, render_template
app = Flask(__name__)
app.secret_key = 'your secret_key'
@app.before_request
def make_session_permanent()
if 'cart' not in session:
    session['cart'] = []
    @app.route('/add_to_cart/<item_id>')
def add_to_cart(item_id):
    session['cart'].append(item_id)
    session.modified = True
    return 'Item added to cart'
@app.route('/')
def homepage():
    total_items_in_cart = len(session['cart'])
    return render_template('homepage.html', total_items=total_items_in_cart)
if__name__ == '__main__':
    app.run(debug=True)            

