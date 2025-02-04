from flask import Flask,jsonify, render_template_string, render_template,request,redirect,url_for

from newsbot import *


app = Flask(__name__)

c_username = 'bhvym'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username == c_username:
            return redirect(url_for('data'))
        else:
            return "Invalid username"
    return render_template('login.html')

@app.route("/data")
def data():
    data_ = [fetch_nytimes_europe(), 
            fetch_all_nytimes_news(), 
            fetch_nytimes_africa(),
            fetch_nytimes_americas(),
            fetch_nytimes_asiapac(),
            fetch_nytimes_middleast()
            ]
    return jsonify(data_)

if __name__ == "__main__":
    app.run(debug=False)