from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)
model = load_model('model.h5')  # Define the model that we need to run

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    img_data = data['image_data']

    # Preprocess the image
    img = cv2.imread(img_data)
    img = cv2.resize(img, (480, 360))
    img = np.expand_dims(img, axis=0)

    # Make a prediction
    prediction = model.predict(img)

    # Return the prediction as JSON
    return jsonify(prediction=prediction.tolist())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3300)
