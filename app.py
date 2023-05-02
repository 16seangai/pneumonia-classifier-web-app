from flask import Flask, jsonify, request
from inference import get_prediction

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def hello():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_name = get_prediction(img_bytes)
        return jsonify({'class_name': class_name})

if __name__ == '__main__':
    app.run()