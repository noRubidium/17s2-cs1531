from flask import Flask, render_template, request, redirect, url_for
from server import app, user_list

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        zID = request.form['zID']
        desc = request.form['desc']
        user_list.append((name, zID, desc))
        return redirect(url_for('hello', name=name, zID=zID, desc=desc))
    return render_template('index.html')


@app.route('/Hello/<name>/<zID>/<desc>')
def hello(name, zID, desc):
    return render_template('hello.html', name=name, zID=zID, desc=desc)


@app.route('/Hello')
def hello_all():
    return render_template('hello_all.html', all_users=user_list)
