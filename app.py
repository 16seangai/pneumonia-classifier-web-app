import os
from flask import Flask, send_from_directory, jsonify, request
from inference import get_prediction

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    print(app.static_folder + '/' + path)
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

@app.route('/predict', methods=['POST'])
def hello():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_name, confidence = get_prediction(img_bytes)
        return jsonify({'class_name': class_name, 'confidence': confidence})

if __name__ == '__main__':
    app.run()