from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "420blazeit"

@app.route('/')
def index():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 0
    return render_template('index.html', count = session['count'])

@app.route('/', methods=['POST'])
def index2():
    action = request.form['action']
    if action == 'one':
        session['count'] += 1
    elif action == 'two':
        session['count'] += 2
    else:
        session['count'] = 0
    return render_template('index.html', count = session['count'])

app.run(debug=True)