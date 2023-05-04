from flask import Flask, jsonify, request
from flask_cors import CORS
from inference import get_prediction

app = Flask(__name__, static_folder='static')
CORS(app, origins=['http://localhost:3000'])

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/predict', methods=['POST'])
def hello():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_name, confidence = get_prediction(img_bytes)
        return jsonify({'class_name': class_name, 'confidence': confidence})

if __name__ == '__main__':
    app.run()