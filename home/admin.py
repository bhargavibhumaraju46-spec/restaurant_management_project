from flask import  Flask, render_template
app = Flask(__name__)
@app.route('/')
def restaurant_homepage():
    background_image = 'path/to/background.jpg', 'path/to/food2.jpg']
    return render_template('homepage.html, background_image=background_image, food_images=food_images') 
if __name__ == '__main__':
    app.run(debug=True)    