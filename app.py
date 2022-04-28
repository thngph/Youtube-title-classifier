from flask import Flask, jsonify, redirect, render_template, request, url_for
from pytube import YouTube as Youtube
import pickle as p
from . import predict

app = Flask(__name__)

model = p.load(open('mlmodels/svm_model_pkl', 'rb'))
transformer = p.load(open('mlmodels/svm_tfidf_pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html', error="")


@app.route('/title', methods=['POST'])
def title():
    title = request.form['title']
    if title:
        output = predict.final_predict(title, transformer, model)
        return render_template('output.html', output=output)
    return redirect(url_for('error'))

@app.route('/url', methods=['POST'])
def url():
    url = request.form['url']
    if url:
        try:
            yt = Youtube('https://youtube.com/watch?v=' + url)
            title = yt.title
            output = predict.final_predict(title, transformer, model)
            return render_template('output.html', output=output)
        except:
            return redirect(url_for('error'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('index.html', error="Có lỗi xảy ra, vui lòng thử lại.")

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json(force=True).values()
    output = predict.final_predict(data, transformer, model)
    return jsonify(output)

 
if __name__ == '__main__': app.run(debug=True, host='0.0.0.0')