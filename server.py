import numpy as np
from flask import Flask, request, jsonify
import pickle

#numpy to create array of requested data, pickle to load trained model for predictions
#create flask instance and load model to variable (conveninently called model)

app = Flask(_name_)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
