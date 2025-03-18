from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from newsbot import *

app = Flask(__name__)
app.secret_key = "your_secret_key"

c_username = 'bhvym'
c_password = 'damngood'

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')





@app.route("/data/europe")
def europe_news():
    return jsonify(fetch_nytimes_europe())

@app.route("/data/all")
def all_news():
    return jsonify(fetch_all_nytimes_news())

@app.route("/data/africa")
def africa_news():
    return jsonify(fetch_nytimes_africa())

@app.route("/data/americas")
def americas_news():
    return jsonify(fetch_nytimes_americas())

@app.route("/data/asiapac")
def asiapac_news():
    return jsonify(fetch_nytimes_asiapac())

@app.route("/data/middleeast")
def middleeast_news():
    return jsonify(fetch_nytimes_middleast())

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        cnn_results = search_cnn(query)
        abc_results = search_abcnews(query)
        # return render_template('search.html', query=query, cnn_results=cnn_results, abc_results=abc_results)
        return jsonify(abc_results)
    return render_template('search.html', query=None, cnn_results=None, abc_results=None)

if __name__ == "__main__":
    app.run("10.12.111.246",debug=True)
