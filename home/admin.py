from flask import Flask, render_template_string
app = Flask(__name__)
privacy_policy_content = """
"""
@app.route('/privacy-policy')
def privacy_policy():
    return render_template_string(privacy_policy_content)
    homepage_content = """
    """
    @app.route('/')
    def home():
        return render_template_string(homepage_content)
        if __name__ == '__main__':
            app.run(debug=True)
                               