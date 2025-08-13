from flask import Flask, render_template
app = Flask(__name__)
faqs = [] 
    {"question": "what is this website about?", "answer": "this websiteprovides information and reasources on various topics."},
    {"question": "how can i contact support?", "answer": "you can contact support via email at support@example.com."},
 ]
@app.route('/')
def homepage():
    return render_template('homepage.html')
@app.route('/faq')
def faq():
    return render_template('faq.html', faqs=faqs)
if __name__ == '__main__':
    app.run(debug=True)





    

         
