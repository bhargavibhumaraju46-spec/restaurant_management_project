from flask import Flask, render_template
app=Flask(__name__)
Aapp.route('/')
def home():
    return render_template("home.html")
    @app.route('/about/')
    def about():
        return render_template("about.html")
        if__name__=="__main__":
            apprun(debug=True)