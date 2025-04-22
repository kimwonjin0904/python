import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from flask import Flask, request, jsonify
from PIL import Image
from io import BytesIO
import base64
import easyocr
import numpy as np


app = Flask(__name__)
reader = easyocr.Reader(['ko', 'en'])

@app.route('/upload', methods=['POST'])
def upload_ocr():
    data = request.json['image']
    image_data = base64.b64decode(data.split(',')[1])
    image = Image.open(BytesIO(image_data)).convert('RGB')
    result = reader.readtext(np.array(image), detail=0)
    return jsonify({'result': ' '.join(result)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
