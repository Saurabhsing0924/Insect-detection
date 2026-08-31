# Save this as app.py
from flask import Flask, request, jsonify
import os
from model import classify_image

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Insect Classification API'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Classify the uploaded image
        category = classify_image(file_path)
        
        return jsonify({'category': category}), 200

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
