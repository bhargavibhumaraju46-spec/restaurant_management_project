privacy_policy_text = """
"""
from flask importbFlask, render_template_string
from privacy_policy import privacy_policy_text
app = Flask(__name__)
@app.route('/privacy-policy')
def privacy_policy():
    return render_template_string('''
    <h1> privacy policy</h1>
    <p>{{ policy_text|safe }}</p>
    ''',policy_text=privacy_policy_text)
    @app route('/')
    def home():
        return render_template_string('''
        <h1>homepage</h1>
        <footer><a href="/privacy-policy">privacypolicy</a></footer>
        ''')
 if __name__ == '__main__':
    app.run(debug=True)