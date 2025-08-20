from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
@app.route('/contact', methods=['POST'])
def handle_contact_form():
    return redirect(url_for('thank_you'))
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html') 
if __name__ == '__main__':
    app.run(debug=True)                      