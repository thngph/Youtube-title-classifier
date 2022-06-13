import requests
import json

#url = 'http://127.0.0.1:5000/'
url = 'http://127.0.0.1:5000/api'
#url ='https://youtubeclassifier.herokuapp.com/api'
#data = [[-0.27864317, -0.09492307, -0.49458376, -0.6712254 , -0.04244065, 0.46521996,  1.72151211, -0.31812766,  0.51996419, -1.15964614, -0.84471308]]

data = ["bao tiền một mớ bình yên? - 14 Casper & Bon (Official)"]
#data = {'fixed acidity':-0.27864317, 'volatile acidity':-0.09492307, 'citric acid':-0.49458376, 'residual sugar':-0.6712254,'chlorides':-0.04244065, 'free sulfur dioxide':0.46521996, 'total sulfur dioxide':1.72151211, 'density':-0.31812766, 'pH': 0.51996419, 'sulphates':-1.15964614, 'alcohol':-0.84471308}
j_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
#print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#r = requests.get(url,verify=False)
#r = requests.post(url,data = j_data, verify=False)
#print(r.text)

import requests, json
r = requests.post( 
    url,
    data = json.dumps(['bao tiền một mớ bình yên? - 14 Casper & Bon (Official)'],
    ensure_ascii=False).encode('utf-8'))
print(r.json())