from flask import Flask, render_template_string
app = Flask(__name__)
restaurant_images = [
    "https://example.com/image1.jpg",
    "https://example.com/image2.jpg",
    "https://example.com/image3.jpg",
]
template = """
"""
@app.route('/gallery')
def gallery():
    return render_template_string(template, images=restaurant_images)
if __name__ == '__main__':
    app.run(debug=True)