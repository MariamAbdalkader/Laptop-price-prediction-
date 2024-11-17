from flask import Flask, request, render_template
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


def predict(inputs):
    with open('regression2.pkl', 'rb') as file:
        gbr, scaler = pickle.load(file)

    input_features_scaled = scaler.transform(inputs)

    # Use the model to predict
    prediction = gbr.predict(input_features_scaled)

    # Print the prediction result
    return np.round(prediction)


@app.route('/')
def home():
    return render_template('laptop.html')

@app.route('/predict-price')
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict_route():
    # Collect simplified input values
    device_type = request.form['device_type']
    brand = request.form['brand']
    storage_type = request.form['storage_type']
    os_type = request.form['os_type']
    cpu_model = request.form['cpu_model']
    gpu_memory = int(request.form['gpu_memory'])
    gpu_brand = request.form['gpu_brand']
    ram = float(request.form['ram'])
    storage = int(request.form['storage'])
    resolution = request.form['resolution'].split('x')
    resolution_width = float(resolution[0])
    resolution_height = float(resolution[1])

    # Initialize input features based on user input
    features = {
        "SSD": 1.0 if storage_type.lower() == "ssd" else 0.0,
        "18_GPU": 1.0 if gpu_memory == 18 else 0.0,
        "_DELL": 1.0 if brand.lower() == "dell" else 0.0,
        "_HDD": 1.0 if storage_type.lower() == "hdd" else 0.0,
        "AMD": 1.0 if "amd" in cpu_model.lower() else 0.0,
        "Intel": 1.0 if "intel" in cpu_model.lower() else 0.0,
        "_Dos": 1.0 if os_type.lower() == "dos" else 0.0,
        "AMD_GPU": 1.0 if "amd" in gpu_brand.lower() else 0.0,
        "14_GPU": 1.0 if gpu_memory == 14 else 0.0,
        "10_GPU": 1.0 if gpu_memory == 10 else 0.0,
        "NVIDIA_GPU": 1.0 if "nvidia" in gpu_brand.lower() else 0.0,
        "_Notebook": 1.0 if device_type.lower() == "notebook" else 0.0,
        "Intel_GPU": 1.0 if "intel" in gpu_brand.lower() else 0.0,
        "30_GPU": 1.0 if gpu_memory == 30 else 0.0,
        "_Apple": 1.0 if brand.lower() == "apple" else 0.0,
        "_Mac": 1.0 if "mac" in os_type.lower() else 0.0,
        "_Ultrabook": 1.0 if device_type.lower() == "ultrabook" else 0.0,
        "M3": 1.0 if cpu_model.lower() == "m3" else 0.0,
        "ResolutionWidth": resolution_width,
        "ResolutionHeight": resolution_height,
        "Memory Amount": storage * 1000 if storage =='512'or'256' else storage * 100000 ,  # Convert GB to MB
        "RAM": ram
    }

    # Convert features to an array for prediction
    input_array = np.array(list(features.values())).reshape(1, -1)



    # Get prediction
    prediction = predict(input_array)

    # Render the same page with the prediction result
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
