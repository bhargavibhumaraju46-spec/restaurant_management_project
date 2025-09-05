from flask import Flask, render_template
app = Flask(__name__)
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403
if __name__ == '__main__':
    app.run(debug=True)    