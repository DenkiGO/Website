from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():  # Измените имя функции на 'home'
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)