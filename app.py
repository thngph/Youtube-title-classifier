from flask import Flask, redirect, render_template, request, url_for
from pytube import YouTube as Youtube
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', error="")


@app.route('/title', methods=['POST'])
def title():
    title = request.form['title']
    if title:
        return render_template('output.html', title=title)
    return redirect(url_for('error'))

@app.route('/url', methods=['POST'])
def url():
    url = request.form['url']
    if url:
        try:
            yt = Youtube('https://youtube.com/watch?v=' + url)
            title = yt.title
            return render_template('output.html', title=title)
        except:
            return redirect(url_for('error'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('index.html', error="Có lỗi xảy ra, vui lòng thử lại.")

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json(force=True)
    types = ["giải trí", "gaming", "giáo dục", "ẩm thực"]
    output = {"type": types[random.randint(0, 3)]}
    return output

 
if __name__ == '__main__': app.run(debug=True)