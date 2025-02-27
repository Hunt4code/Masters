#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)

# Load the trained neural network model
model = keras.models.load_model('fnn_trained_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert input data into NumPy array
        patient_data = np.array([[
            data["family_history"],
            data["gender"],
            data["iodine_deficiency"],
            data["radiation_exposure"],
            data["obesity"],
            data["smoking"],
            data["diabetes"],
            data["age"]
        ]])

        # Predict probability of Malignant
        prob_malignant = model.predict(patient_data)[0, 0]

        # Decision threshold
        threshold = 0.4  # Optimized threshold
        prediction = int(prob_malignant > threshold)

        return jsonify({"prediction": "Malignant" if prediction == 1 else "Benign"})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)


# In[ ]:




