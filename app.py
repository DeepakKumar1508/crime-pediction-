```python
from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return """
    <h1>Crime Prediction System</h1>

    <form action="/predict" method="get">

        <input type="number"
               name="population"
               placeholder="Population"
               required><br><br>

        <input type="number"
               name="unemployment"
               placeholder="Unemployment Rate"
               required><br><br>

        <input type="number"
               name="poverty"
               placeholder="Poverty Rate"
               required><br><br>

        <button type="submit">Predict</button>

    </form>
    """

@app.route("/predict")
def predict():

    population = float(request.args.get("population"))
    unemployment = float(request.args.get("unemployment"))
    poverty = float(request.args.get("poverty"))

    features = np.array([[population,
                          unemployment,
                          poverty]])

    prediction = int(model.predict(features)[0])

    if prediction == 1:
        status = "High Crime Risk Area"
    else:
        status = "Low Crime Risk Area"

    return f"""
    <html>
    <body style='font-family:Arial;padding:40px;'>

    <h1>Prediction Result</h1>

    <h2>{status}</h2>

    <p><b>Population:</b> {population}</p>
    <p><b>Unemployment Rate:</b> {unemployment}%</p>
    <p><b>Poverty Rate:</b> {poverty}%</p>

    <br>

    <a href="/">Back</a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
```
