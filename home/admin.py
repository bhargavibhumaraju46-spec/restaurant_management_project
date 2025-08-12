from flask import Flask, render_template
app = Flask(__name__)
welcome_message = "welcome to our restaurant enjoy your dining experience"
@app.route('/')
def homepage():
    return render_template('homepage.html', welcome_message=welcome_message)
    if __name__ == '__main__':
        app.run(debug=True)
