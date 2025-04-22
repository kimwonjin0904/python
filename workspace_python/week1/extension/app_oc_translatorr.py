import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import numpy as np
import easyocr
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
reader = easyocr.Reader(['ko', 'en'])

@app.route('/upload', methods=['POST'])
def upload_ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image'].read()
    image = Image.open(io.BytesIO(image_file)).convert('RGB')
    image_np = np.array(image)
    result = reader.readtext(image_np, detail=0)
    if result:
        text = ' '.join(result)
        trans = text
    else:
        return jsonify({'result': '', 'translated': "번역 가능 텍스트 없음"})
    return jsonify({'result': text, 'translated': trans})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
