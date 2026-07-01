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

@app.route('/guyver/chronology')
def guyver_chronology():
    return render_template('guyver_chronology.html', title='Хронология — Гайвер')

@app.route('/guyver/comparison')
def guyver_comparison():
    return render_template('guyver_comparison.html', title='Сравнение версий — Гайвер')

@app.route('/guyver/lore')
def guyver_lore():
    return render_template('guyver_lore.html', title='Карта лора — Гайвер')

@app.route('/guyver/gallery')
def guyver_gallery():
    return render_template('guyver_gallery.html', title='Галерея трансформаций — Гайвер')

@app.route('/guyver/quiz')
def guyver_quiz():
    return render_template('guyver_quiz.html', title='Какой ты зоаноид? — Гайвер')

@app.route('/guyver/legal')
def guyver_legal():
    return render_template('guyver_legal.html', title='Где смотреть — Гайвер')

@app.route('/totoro')
def totoro():
    return render_template('totoro.html', title='Мой сосед Тоторо')

@app.route('/bleach')
def bleach():
    return render_template('bleach.html', title='Блич')

@app.route('/onepiece')
def onepiece():
    return render_template('onepiece.html', title='One Piece')

@app.route('/ghibli')
def ghibli():
    return render_template('ghibli.html', title='Studio Ghibli')

@app.route('/naruto')
def naruto():
    return render_template('naruto.html', title='Наруто')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, port=port)
