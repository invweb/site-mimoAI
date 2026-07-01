import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/guyver')
def guyver():
    return render_template('guyver.html', title='Гайвер')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, port=port)
