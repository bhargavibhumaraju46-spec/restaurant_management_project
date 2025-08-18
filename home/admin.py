from flask import Flask, session, request, jsonify
app = Flask(__name__)
app.secret_key = 'your_secret_key'
menu_items = [
    {'id': 1, 'name':'Item 1', 'price': 100},
    {'id': 2, 'name':'Item 2', 'price': 200},
    {'id': 3, 'name':'Item 3', 'price': 300},
]
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.json['item_id']
    if 'cart' not in session:
        session['cart'] = [] 
        for item in session['cart']:
            if item['id'] == item_id:
                item['quantity'] = item.get('quantity', 1) + 1
                session.modified = True
                return jsonify({'message': 'Item quantity updated in cart'})
item = next((i for i in menu_items if i['id'] == item_id), None)
if item:
    session['cart'].append({'id': item['id'], 'name': item['name'], 'price':item['price'], 'quantity':1})
    session.modified = True
    return jsonify({'message': 'Item added to cart'})
    return jsonify({'error': 'Item not found'}), 404
    @app route('/view_cart', methods=['GET'])
    def view_cart():
        if 'cart' in session:
            return jsonify(session['cart'])
            else:
                return jsonify({'message': 'Cart is empty'})
   if __name__ == '__main__':
       app.run(debug=True)                