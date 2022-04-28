import pandas as pd
import re

from underthesea import word_tokenize
from pyvi import ViTokenizer

from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.feature_extraction.text import TfidfVectorizer
import advertools as adv


def preprocess_data(data, transformer):
    data = re.sub(r'\d+', '', str(data).lower())
    data = ViTokenizer.tokenize(data)
    data = data.replace("tiếng anh","tiếng_anh")
    data = re.sub(r'[^\w\s]', '', data)
    data = word_tokenize(data)
    y = lambda x: [w.replace(" ","_") for w in x]
    data = y(data)
    d = {'title': [" ".join(data)]}
    data = pd.DataFrame(data = d)
    return transformer.transform(data.title).toarray()


def make_predict(data, model):
    return model.predict(data)

def map_predict(result):
    classes = ['du lịch', 'giáo dục', 'khoa học và công nghệ', 'làm đẹp',
       'lịch sử', 'phim ảnh', 'thời trang', 'tin tức', 'trò chơi',
       'trẻ em', 'y tế', 'âm nhạc', 'ẩm thực']
    return classes[result[0]]

def final_predict(data, transformer, model):
    data = preprocess_data(data, transformer)
    result = make_predict(data, model)
    return map_predict(result)