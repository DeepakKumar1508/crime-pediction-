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
    <h1>Crime Count Prediction</h1>

    <form action="/predict" method="get">

        <input type="number" name="population"
        placeholder="Population" required><br><br>

        <input type="number" name="unemployment"
        placeholder="Unemployment Rate" required><br><br>

        <input type="number" name="poverty"
        placeholder="Poverty Rate" required><br><br>

        <button type="submit">Predict</button>

    </form>
    """

@app.route("/predict")
def predict():

    try:
        population = float(request.args.get("population"))
        unemployment = float(request.args.get("unemployment"))
        poverty = float(request.args.get("poverty"))

        features = np.array([
            [population, unemployment, poverty]
        ])

        prediction = model.predict(features)[0]

        risk = "High Crime Area" if prediction == 1 else "Low Crime Area"

        return f"""
        <h1>Prediction Result</h1>

        <h2>Crime Prediction: {prediction}</h2>

        <h3>{risk}</h3>

        <br>

        <a href="/">Back</a>
        """

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
```
