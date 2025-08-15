from flask import render_template, request
@app.route('/products/category')
def categry_page():
    breadcrumbs = [
        {'name': 'home', 'url':'/'},
        {'name': 'products', 'url':'/products'},
        {'name': 'category', 'url':'request.path'}
    ]
    return render_template('category.html', breadcrumbs=breadcrumbs)