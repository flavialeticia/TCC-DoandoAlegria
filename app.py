from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comodoar')
def comodoar():
    return render_template('comodoar.html')

@app.route('/sobrenos')
def sobrenos():
    return render_template('sobrenos.html')

@app.route('/verongs')
def verongs():
    return render_template('verongs.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')



