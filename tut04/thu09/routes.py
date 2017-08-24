from flask import render_template, request, redirect, url_for
from server import app, user_input

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        zID = request.form['zID']
        desc = request.form['desc']
        user_input.append((name, zID, desc))
        return redirect(url_for('hello', name=name,id=zID, desc=desc))
    return render_template('index.html')

@app.route('/Hello/<name>/<id>/<desc>')
def hello(name, id, desc):
    return render_template('hello.html', name=name, id=id, desc=desc)

@app.route('/Hello')
def hello_all():
    return render_template('hello_all.html', all_users=user_input)
