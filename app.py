import os
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pytube import YouTube as Youtube
import pickle as p

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)

classes = ['giáo dục và khoa học công nghệ', 'giải trí và nghệ thuật',
       'tin tức', 'đời sống']
model = p.load(open('mlmodels/Thinh_svm_sgdc_tfidf_pkl', 'rb'))


def make_predict(data, model):
    pred = model.predict_proba(data)[0]
    res = {classes[i]: pred[i] for i in range(len(classes))}
    return dict(sorted(res.items(), key=lambda x: x[1], reverse=True))

@app.route('/')
def index():
    return render_template('index.html', error="")


@app.route('/title', methods=['POST'])
def title():
    title = request.form['title']
    if title:
        res = make_predict([title], model)
        return render_template('output.html', output=[title,res])
    return redirect(url_for('error'))

@app.route('/url', methods=['POST'])
def url():
    url = request.form['url']
    if url:
        try:
            yt = Youtube('https://youtube.com/watch?v=' + url)
            title = yt.title
            res = make_predict([title], model)
            return render_template('output.html', output=[title,res])
        except:
            return redirect(url_for('error'))

@app.route('/error', methods=['GET'])
def error():
    return render_template('index.html', error="Có lỗi xảy ra, vui lòng thử lại.")

@app.route('/api', methods=['POST'])
def api():
    data = [request.get_json(force=True)[0]]
    output = make_predict(data, model)
    return jsonify(output)

 
if __name__ == '__main__': app.run(debug=True, host='0.0.0.0', port=port)