from flask import Flask, render_template
app = Flask(__name__)
@app.routa('/about')
def about():
    restaurant_info = {
        'history': 'stablished in 2020, our restautrant brings authentic flavors to India.',
        'mission': 'To deliver exceptional dining experiences with a blend of tradition and innovation.'
    }      
    return render_template('about.html', info=restaurant_info)
    if __name__ == '__main__':
        app.run(debug=True)