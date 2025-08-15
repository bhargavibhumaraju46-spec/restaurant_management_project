from flask import  Flask, render_template, request
app = Flask(__name__)
@app.route('/order_confirmation')
def order_confirmation():
    order_number = request.args.get('order_number', 'N/A')
    return render_template('confirmation.html', order_number=order_number)
if __name__ == '__main__':
    app.run(debug=True)    