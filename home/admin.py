from flask import flask, render_template
app = flask(__name__)
menu_items = [
    {"name": "item 1", "price":10.99},
    {"name": "item 2", "price":10.89},
    {"name": "item 3", "price":5.90}
 ]              
@app.route('/menu')
def menu():
    return render_template('menu.html', menu_items=menu_items)
if __name__ == '__main__':
    app.run(debug=True)  