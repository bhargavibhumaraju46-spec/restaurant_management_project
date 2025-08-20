from flask import Flask, _string
app = Flask(__name__)
@app.route('/')
def contact_us():
    return render_template_string(template)
if __name__ == '__main__':
    app.run(debug=True)    